import requests
import sys

def main():
    try:
        if len(sys.argv) == 2:
            value = float(sys.argv[1])
            api_key = "api_key"
            response = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}")
            resp_json = response.json()
            price = float(resp_json["data"]["priceUsd"])
            print(f"${price * value:,.4f}")
        else:
            sys.exit("Command-line argument is not a number")
    except:
        sys.exit("Missing command-line argument")

if __name__ == "__main__":
    main()
