from rich import print
from modules.save import save_result

def email_lookup(email):
    domain = email.split("@")[-1]

    output = f"Email: {email}\nDomain: {domain}"

    print("[green]EMAIL INFO[/green]")
    print(output)
    save_result(output)
