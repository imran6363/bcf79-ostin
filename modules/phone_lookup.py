import phonenumbers
from phonenumbers import geocoder, carrier
from rich import print
from modules.save import save_result

def phone_lookup(number):
    try:
        parsed = phonenumbers.parse(number)

        country = geocoder.description_for_number(parsed, 'en')
        car = carrier.name_for_number(parsed, 'en')

        output = f"""
Valid: {phonenumbers.is_valid_number(parsed)}
Country: {country}
Carrier: {car}
Map: https://www.google.com/maps/search/{country}
"""

        print("[green]PHONE INFO[/green]", output)
        save_result(output)

    except:
        print("[red]Invalid Number[/red]")
