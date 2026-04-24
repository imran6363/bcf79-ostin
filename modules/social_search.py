from rich import print
from modules.save import save_result

def social_search(query):
    links = [
        f"https://facebook.com/search/top/?q={query}",
        f"https://instagram.com/{query}",
        f"https://twitter.com/{query}",
        f"https://linkedin.com/search/results/all/?keywords={query}"
    ]

    print("[green]SOCIAL SEARCH[/green]")

    for link in links:
        print(link)
        save_result(link)
