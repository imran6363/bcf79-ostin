import whois
from rich import print
from modules.save import save_result

def whois_lookup(domain):
    info = whois.whois(domain)

    print("[green]WHOIS INFO[/green]")
    for k, v in info.items():
        line = f"{k}: {v}"
        print(line)
        save_result(line)
