import requests

USERNAME = "Ololade117"
REPO = "ololade-profile-data"

def fetch_all_repo_files():
    api_url = f"https://api.github.com/repos/{USERNAME}/{REPO}/contents/"
    response = requests.get(api_url)
    response.raise_for_status()

    files = response.json()
    all_text = {}

    for file in files:
        if file["type"] == "file":
            raw_url = file["download_url"]
            file_response = requests.get(raw_url)
            file_response.raise_for_status()
            all_text[file["name"]] = file_response.text

    return all_text