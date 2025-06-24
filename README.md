GitHub API Agent
A Python-based AI agent that interacts with the GitHub API to perform various repository management tasks using natural language commands.

Features
Natural Language Processing: Understands plain English commands for GitHub operations

Comprehensive API Coverage: Supports 26 different GitHub API endpoints

Error Handling: Provides clear error messages when things go wrong

User-Friendly Output: Summarizes API responses in easy-to-understand language

Supported Operations
Repository management (create, delete, update, list)

File operations (create, update, delete)

Issue tracking (create, list, close)

Pull requests (create, list, merge)

Collaboration management (add/remove collaborators)

Repository starring and forking

Notification management

Prerequisites
Python 3.7+

GitHub Personal Access Token (with appropriate permissions)

Google Gemini API key

Installation
Clone this repository:

bash
git clone https://github.com/your-username/github-api-agent.git
cd github-api-agent
Install dependencies:

bash
pip install -r requirements.txt
Create a .env file in the project directory with your credentials:

text
GITHUB_TOKEN=your_github_personal_access_token
GEMINI_API_KEY=your_google_gemini_api_key
Usage
Run the agent:

bash
python main.py
The agent will start in interactive mode. You can enter commands like:

"List my repositories"

"Create a new private repository named test-project"

"Delete the repository old-project"

"List all issues in my-project"

"Create a new file README.md in my-project"

Type 'exit' or 'quit' to end the session.

Configuration
The agent can be configured by modifying the following:

github_api_docs.txt: Add or modify API endpoints as needed

.env: Update API keys and tokens

main.py: Adjust the Gemini model parameters

Error Handling
The agent will notify you if:

Required environment variables are missing

API calls fail

It doesn't understand your request

GitHub returns an error

Limitations
Currently only supports GitHub REST API (v3)

Requires internet connection to access GitHub and Gemini APIs

Rate limits apply based on your GitHub token permissions

Contributing
Contributions are welcome! Please open an issue or pull request for any improvements.

License
MIT License
