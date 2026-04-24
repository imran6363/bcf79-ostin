from rich import print
from modules.ip_lookup import ip_lookup
from modules.email_lookup import email_lookup
from modules.username_search import username_search
from modules.whois_lookup import whois_lookup
from modules.phone_lookup import phone_lookup
from modules.social_search import social_search
from modules.truecaller import truecaller_search

def banner():
    print("""
[bold green]
██████╗  ██████╗ ██████╗  ██████╗ ███████╗
██╔══██╗██╔═══██╗██╔══██╗██╔════╝ ██╔════╝
██████╔╝██║   ██║██████╔╝██║  ███╗█████╗
██╔═══╝ ██║   ██║██╔══██╗██║   ██║██╔══╝
██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗
╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
[/bold green]

[cyan]Bangladesh Cyber Force 79[/cyan]
Owner: Imran

[yellow]Empowering Ethical Intelligence Gathering[/yellow]
""")

def menu():
    print("""
[1] IP Lookup
[2] Email Lookup
[3] Username Search
[4] WHOIS Lookup
[5] Phone Lookup
[6] Social Media Search
[7] Truecaller Search
[0] Exit
""")

def main():
    while True:
        banner()
        menu()
        choice = input("Select Option: ")

        if choice == "1":
            ip_lookup(input("Enter IP: "))

        elif choice == "2":
            email_lookup(input("Enter Email: "))

        elif choice == "3":
            username_search(input("Enter Username: "))

        elif choice == "4":
            whois_lookup(input("Enter Domain: "))

        elif choice == "5":
            phone_lookup(input("Enter Phone (+880...): "))

        elif choice == "6":
            social_search(input("Enter name/username: "))

        elif choice == "7":
            truecaller_search(input("Enter number: "))

        elif choice == "0":
            print("[red]Goodbye![/red]")
            break

        else:
            print("[red]Invalid Option[/red]")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
