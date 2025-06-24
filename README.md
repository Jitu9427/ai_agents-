🔧 Setup Instructions
✅ Step 1: Clone the Project
git clone https://github.com/your-username/github-ai-agent.git
cd github-ai-agent

✅ Step 2: Install Dependencies
pip install -r requirements.txt


✅ Step 3: Get API Keys
🔑 GitHub Token
Go to: https://github.com/settings/tokens

Click “Generate new token (classic)”

Select all permissions:


🔑 Gemini API Key
Go to: https://makersuite.google.com/app/apikey

Sign in with your Google account

Copy the API key

✅ Step 4: Create a .env File
In the root folder of your project, create a file named .env with the following:

GITHUB_TOKEN=your_github_token_here
GEMINI_API_KEY=your_gemini_api_key_here
Replace the values with your actual keys.

✅ Step 5: Run the Agent

python main.py



