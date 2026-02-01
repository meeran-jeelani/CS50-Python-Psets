import sys
import requests

def main():
    # Check proper number of command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    # Try to convert the argument to float
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Fetch from mocked CoinCap API
    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=YOUR_API_KEY"
        )
    except requests.RequestException:
        sys.exit("Error fetching Bitcoin price")

    data = response.json()

    # Parse price from mock’s JSON structure
    try:
        price = float(data["data"]["priceUsd"])
    except (KeyError, TypeError, ValueError):
        sys.exit("Error parsing Bitcoin price")

    total = price * bitcoins

    # Print USD total with thousands separators, 4 decimal places
    print(f"${total:,.4f}")

if __name__ == "__main__":
    main()
