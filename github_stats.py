import requests
import argparse

GITHUB_API_URL = "https://api.github.com/repos"

def fetch_repo_stats(username, repo_name):
    url = f"{GITHUB_API_URL}/{username}/{repo_name}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"❌ Error: Unable to fetch data for {username}/{repo_name}")
        return None

    data = response.json()
    
    return {
        "Stars": data["stargazers_count"],
        "Forks": data["forks_count"],
        "Open Issues": data["open_issues_count"],
        "Watchers": data["watchers_count"],
    }

def main():
    parser = argparse.ArgumentParser(description="Fetch GitHub repo stats")
    parser.add_argument("username", help="GitHub username or org name")
    parser.add_argument("repo", help="GitHub repository name")

    args = parser.parse_args()
    stats = fetch_repo_stats(args.username, args.repo)

    if stats:
        print("\n📊 GitHub Stats")
        for key, value in stats.items():
            print(f"✅ {key}: {value}")

if __name__ == "__main__":
    main()
