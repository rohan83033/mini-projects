import requests
from pprint import PrettyPrinter

printer = PrettyPrinter()
BASE_URL = "https://open.er-api.com/v6"

def get_currencies():
    url = f"{BASE_URL}/latest/USD"
    resp = requests.get(url).json()
    if resp.get("result") != "success":
        print("Failed to fetch data:", resp.get("error-type"))
        return {}
    return resp.get("rates", {})

def print_currencies(rates):
    for code in sorted(rates.keys()):
        print(code)

def exchange_rate(currency1, currency2):
    rates = get_currencies()
    if not rates:
        return None
    r1 = rates.get(currency1)
    r2 = rates.get(currency2)
    if r1 is None or r2 is None:
        print("Invalid currency code.")
        return None
    rate = r2 / r1
    print(f"{currency1} → {currency2} = {rate:.6f}")
    return rate

def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return
    try:
        amt = float(amount)
    except ValueError:
        print("Invalid amount.")
        return
    converted = amt * rate
    print(f"{amt} {currency1} = {converted:.6f} {currency2}")
    return converted

def main():
    print("Currency converter using Exchangerate-API (Open Access)")
    print("Commands: list, rate, convert, q to quit")
    while True:
        cmd = input("Enter command: ").strip().lower()
        if cmd == "q":
            break
        elif cmd == "list":
            rates = get_currencies()
            print_currencies(rates)
        elif cmd == "rate":
            c1 = input("Base currency: ").strip().upper()
            c2 = input("Target currency: ").strip().upper()
            exchange_rate(c1, c2)
        elif cmd == "convert":
            c1 = input("Base currency: ").strip().upper()
            amt = input(f"Amount in {c1}: ").strip()
            c2 = input("Target currency: ").strip().upper()
            convert(c1, c2, amt)
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
