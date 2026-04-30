import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if matches := re.search(r"^([0-9][0-9]?[0-9]?)\.([0-9][0-9]?[0-9]?)\.([0-9][0-9]?[0-9]?)\.([0-9][0-9]?[0-9]?)$", ip):
        digit1 = int(matches[1])
        digit2 = int(matches[2])
        digit3 = int(matches[3])
        digit4 = int(matches[4])
        if (0 < digit1 < 256) and (0 < digit2 < 256) and (0 < digit3 < 256) and (0 < digit4 < 256):
            return True
    return False

if __name__ == "__main__":
    main()
