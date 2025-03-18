# 🏷️ GitHub Repository Renamer
This script allows you to rename GitHub repositories using the GitHub API. It takes a list of repositories and allows you to input a new name for each one directly from the terminal.

## 🚀 Features
✅ Rename multiple repositories automatically

✅ Prompt user for custom new repository names

✅ Skip renaming if no input is provided

✅ Handles errors and provides clear feedback

## 📥 Requirements
Python (Version 3.6+)
GitHub Personal Access Token with repo scope
## 🛠️ Setup
###1. Clone the Repository
git clone https://github.com/abdulw786/Self_Hosted_Github_Action_Runner.git
cd repo-renamer

### 2. Install Dependencies
pip install requests

### 3. Set Up GitHub Token
Set the GitHub token in your environment:

export GITHUB_TOKEN="your-github-token"
Make sure the token has the necessary permissions to update repository settings.

## 💻 Usage
Add repositories to the repos list in the format "owner/repo":

repos = ["myorg/myrepo", "anotherorg/anotherrepo"]

Run the script:

python main.py

Enter the new name for each repository when prompted:

Enter new name for myorg/myrepo: new-repo-name  
Renaming completed for myorg/myrepo to new-repo-name  
If no input is provided, the script will skip the renaming step for that repository.

## 🏆 Example Output

Enter new name for myorg/myrepo: new-repo-name  
Renaming completed for myorg/myrepo to new-repo-name  

Enter new name for anotherorg/anotherrepo:  
Skipping anotherorg/anotherrepo - No input provided.

## 📄 Code Overview
The script sends a PATCH request to the GitHub API using the requests library.
It updates the name property of the repository with the new value.
Handles status codes and provides meaningful feedback in case of failure.


## ❗ Notes
Ensure that the GitHub token has the necessary repo permissions.
The token should not be shared publicly for security reasons.
