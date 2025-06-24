# GitHub API Agent

A Python-based AI agent that interacts with the GitHub API to perform various repository management tasks using natural language commands.




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
