from datetime import date, datetime, time
import sys

import inflect

p = inflect.engine()

def main():
    user_dob = check_dob_format(input("Date of Birth: "))
    dob_to_date_minute = get_time_difference(user_dob)
    print(get_time_str_formatted(dob_to_date_minute))

def check_dob_format(dob_str):
    try:
        return datetime.strptime(dob_str, "%Y-%m-%d")
    except ValueError:
        sys.exit("Invalid date")

def get_time_difference(dob_dt):
    today_date = datetime.combine(date.today(), time.min)
    time_diff = today_date - dob_dt
    return round(time_diff.total_seconds() / 60)

def get_time_str_formatted(time_minute):
    str_out = p.number_to_words(time_minute)
    str_out_formatted = str_out.replace(" and ", " ").capitalize()
    return f"{str_out_formatted} {p.plural_noun('minute', time_minute)}"

if __name__ == "__main__":
    main()
