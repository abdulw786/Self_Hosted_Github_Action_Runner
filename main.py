import requests
import json
import os

# Add the repositories to rename in the format "owner/repo"
repos = ["myorg/myrepo", "anotherorg/anotherrepo"]

headers = {
    'Authorization': f'token {os.getenv("GITHUB_TOKEN")}',
    'Accept': 'application/vnd.github.v3+json'
}

def rename_repositories():
    for repo in repos:
        url = f'https://api.github.com/repos/{repo}'
        
        # Take new repo name as input
        new_name = input(f"Enter new name for {repo}: ").strip()
        if not new_name:
            print(f"Skipping {repo} - No input provided.")
            continue

        data = {'name': new_name}
        response = requests.patch(url, headers=headers, json=data)

        if response.status_code == 200:
            print(f"Renaming completed for {repo} to {new_name}")
        else:
            print(f"Failed to rename {repo}: {response.status_code} - {response.json()}")

rename_repositories()