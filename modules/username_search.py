import requests
from rich import print
from modules.save import save_result

def username_search(username):
    sites = [
        f"https://github.com/{username}",
        f"https://instagram.com/{username}",
        f"https://twitter.com/{username}"
    ]

    print("[green]USERNAME SEARCH[/green]")

    for url in sites:
        r = requests.get(url)
        status = "FOUND" if r.status_code == 200 else "NOT FOUND"
        print(f"{url} → {status}")
        save_result(f"{url} → {status}")
