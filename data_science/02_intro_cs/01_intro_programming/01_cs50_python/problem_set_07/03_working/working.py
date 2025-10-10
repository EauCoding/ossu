import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(hour_string):
    if matches := re.search(r"^([0-9][0-9]?):?([0-9]?[0-9]?) (AM|PM) to ([0-9][0-9]?):?([0-9]?[0-9]?) (AM|PM)", hour_string, re.IGNORECASE):
        first_hour = int(matches.group(1))
        second_hour = int(matches.group(4))

        if matches.group(2) == '':
            first_minute = 0
        else:
            first_minute = int(matches.group(2))

        if matches.group(5) == '':
            second_minute = 0
        else:
            second_minute = int(matches.group(5))

        if (0 <= first_hour <= 12) and (0 <= first_minute <= 59) and (0 <= second_hour <= 12) and (0 <= second_minute <= 59):
            if matches.group(3) == 'PM':
                first_hour = remove_pm(matches.group(1))

            if matches.group(6) == 'PM':
                second_hour = remove_pm(matches.group(4))

            return f"{first_hour:02d}:{first_minute:02d} to {second_hour:02d}:{second_minute:02d}"
        else:
            raise ValueError("Wrong Values")
    else:
        raise ValueError("Wrong Format")

def remove_pm(hour_digit):
    hour_int = int(hour_digit)
    without_pm = hour_int + 12
    if without_pm == 24:
        return 0
    return without_pm

if __name__ == "__main__":
    main()
