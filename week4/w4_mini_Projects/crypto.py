"""
5. Fetch Live Cryptocurrency Prices

Uses the free CoinGecko API - no API key or sign-up required.
Install requests if you don't have it:
    pip install requests
"""

import requests

COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price"


def get_crypto_price(coin_ids, currency="usd"):
    params = {"ids": ",".join(coin_ids), "vs_currencies": currency}

    try:
        response = requests.get(COINGECKO_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network error while fetching prices: {e}")
        return
    except ValueError:
        print("Received an invalid response from the server. Try again later.")
        return

    if not data:
        print("Could not fetch prices. Check the coin names and try again.")
        return

    print(f"\nLive Cryptocurrency Prices (in {currency.upper()}):")
    for coin in coin_ids:
        if coin in data:
            print(f"{coin.title()}: {data[coin][currency]}")
        else:
            print(f"{coin.title()}: Not found")


def main():
    print("Live Crypto Price Checker")
    print("(Use CoinGecko IDs, e.g. bitcoin, ethereum, dogecoin, litecoin)")
    coins_input = input("Enter coin names, comma-separated: ")
    coin_ids = [c.strip().lower() for c in coins_input.split(",")]

    currency = input("Enter currency code (default usd): ").strip().lower()
    if not currency:
        currency = "usd"

    get_crypto_price(coin_ids, currency)


if __name__ == "__main__":
    main()