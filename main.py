import json
import requests
import os
from dotenv import load_dotenv
import google.generativeai as genai

# --- Setup ---
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GITHUB_TOKEN or not GITHUB_TOKEN.startswith("ghp_"):
    print("❌ Error: GitHub Token not found or invalid. Please check your .env file.")
    exit()

if not GEMINI_API_KEY:
    print("❌ Error: Gemini API Key not found. Please check your .env file.")
    exit()
# Setup Gemini
genai.configure(api_key=GEMINI_API_KEY)
gemini_model = genai.GenerativeModel('models/gemini-1.5-flash')

# --- Generic Tools ---
def get_api_docs():
    try:
        with open("github_api_docs.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "Error: github_api_docs.txt not found."

def execute_api_call(method, url, headers, json_body):
    print(f"  Executing: {method} {url}...")
    try:
        response = requests.request(method, url, headers=headers, json=json_body, timeout=20)
        response.raise_for_status()
        if response.status_code == 204:
            return {"status": "Success (204 No Content)"}
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": "HTTP Error", "status_code": e.response.status_code, "details": e.response.text}
    except Exception as e:
        return {"error": "Execution failed", "details": str(e)}

# --- Core Agent Logic ---
def run_agent_turn(user_instruction, api_docs):
    planner_prompt = f"""
You are a planner agent. Your job is to convert a user's request into a single, valid GitHub API call by using the provided documentation.

User's request: "{user_instruction}"

API Documentation:
---
{api_docs}
---

Your task:
1. Analyze the user's request.
2. Find the correct endpoint and method in the documentation.
3. Construct the full URL. For endpoints like /repos/{{owner}}/{{repo}}, you must infer the 'owner' from the context (assume it's the authenticated user's name if not specified) and the 'repo' from the user's request. If you need the owner's username, you can't know it, so just use a placeholder like `your-username` and inform the user.
4. Create the request body if required.
5. Return ONLY the JSON object for the API call. Do not add any other text.

The JSON structure MUST be:
{{
  "method": "GET/POST/DELETE",
  "url": "https://api.github.com/...",
  "headers": {{ "Authorization": "Bearer {GITHUB_TOKEN}" }},
  "body": {{ ... }} or null
}}
    """

    print("🧠 Agent thinking... (Planning API call)")
    try:
     response = gemini_model.generate_content(planner_prompt)
     api_call_details_str = response.text

     import re
     match = re.search(r"```json\s*(\{.*?\})\s*```", api_call_details_str, re.DOTALL)
     if not match:
        return f"❌ Error: Could not find a valid JSON block in Gemini response:\n\n{api_call_details_str}"
     api_call_details = json.loads(match.group(1))
    except Exception as e:
        return f"Sorry, I had trouble understanding what to do. Error: {e}"

    api_call_details["headers"]["Authorization"] = f"Bearer {GITHUB_TOKEN}"

    api_result = execute_api_call(
        method=api_call_details.get("method"),
        url=api_call_details.get("url"),
        headers=api_call_details.get("headers", {}),
        json_body=api_call_details.get("body")
    )

    summarizer_prompt = f"""
You are a helpful assistant. Your job is to explain the result of an API call to a user in a clear and friendly way.

Original user request: "{user_instruction}"
API call result (in JSON):
---
{json.dumps(api_result, indent=2)}
---

Your task:
- If there was an error, explain it simply. For example, if a repository already exists or was not found.
- If the action was successful (like creating or deleting), confirm it clearly.
- If the result is a list of items (like repositories or commits), present them in a clean, readable list. Don't show all the raw data; just the important parts (e.g., repo name, commit message).
- Respond naturally.
    """

    print("✍️ Agent thinking... (Summarizing result)")
    try:
        response = gemini_model.generate_content(summarizer_prompt)
        return response.text
    except Exception as e:
        return f"I got a result, but had trouble explaining it. Result: {api_result}"

# --- Main Chat Loop ---
if __name__ == "__main__":
    print("🤖 Hello! I am your GitHub Agent. How can I help you today?")
    print("   You can ask me to: 'list my repos', 'create a new repo named my-project', 'delete the repo my-project', etc.")
    print("   Type 'exit' or 'quit' to end the chat.")
    print("-" * 50)

    api_docs = get_api_docs()
    if "Error:" in api_docs:
        print(f"❌ {api_docs}")
        exit()

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("🤖 Goodbye!")
            break

        if not user_input:
            continue

        agent_response = run_agent_turn(user_input, api_docs)
        print(f"\nAgent: {agent_response}\n" + "-" * 50)
