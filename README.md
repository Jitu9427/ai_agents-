# GitHub API Agent

A Python-based AI agent that interacts with the GitHub API to perform various repository management tasks using natural language commands.

## ✨ Features

- **Natural Language Processing**: Understands plain English commands for GitHub operations
- **Comprehensive API Coverage**: Supports 26 different GitHub API endpoints  
- **Error Handling**: Provides clear error messages when things go wrong
- **User-Friendly Output**: Summarizes API responses in easy-to-understand language

## 🛠 Supported Operations

### Repository Management
- Create, delete, update, list repositories
- Fork repositories
- Star/unstar repositories

### Code Management
- Create, update, delete files
- List commits
- Manage branches

### Collaboration
- Add/remove collaborators  
- Manage issues (create, list, close)
- Handle pull requests (create, list, merge)

### Notifications
- View notifications
- Mark notifications as read

## ⚙️ Prerequisites

- Python 3.7+
- GitHub Personal Access Token (with repo permissions)
- Google Gemini API key

## 🚀 Installation & Usage

```bash
# Clone the repository
git clone https://github.com/your-username/github-api-agent.git
cd github-api-agent

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "GITHUB_TOKEN=your_token_here" > .env
echo "GEMINI_API_KEY=your_key_here" >> .env

# Run the agent
python main.py
