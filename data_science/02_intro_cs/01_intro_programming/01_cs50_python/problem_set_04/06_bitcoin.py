import requests
import sys

def main():
    try:
        if len(sys.argv) == 2:
            value = float(sys.argv[1])
            response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=a6410160f881382c23c547e8452e64048bb400886485f1ee36c2eece1e8b790f")
            resp_json = response.json()
            price = float(resp_json["data"]["priceUsd"])
            print(f"${price * value:,.4f}")
        else:
            sys.exit("Command-line argument is not a number")
    except:
        sys.exit("Missing command-line argument")

if __name__ == "__main__":
    main()
