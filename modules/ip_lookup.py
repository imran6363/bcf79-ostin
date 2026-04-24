import requests
from rich import print
from modules.save import save_result

def ip_lookup(ip):
    res = requests.get(f"http://ip-api.com/json/{ip}").json()

    output = f"""
IP: {res.get('query')}
Country: {res.get('country')}
City: {res.get('city')}
ISP: {res.get('isp')}
"""

    print("[green]IP INFO[/green]", output)
    save_result(output)
