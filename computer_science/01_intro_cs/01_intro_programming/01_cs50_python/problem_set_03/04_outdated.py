def main():
    month_list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        try:
            input_date = input("Date: ").strip()
            if "/" in input_date:
                month, date, year = input_date.split("/")
                month, date, year = int(month), int(date), int(year)
                if 1 <= month <= 12 and 1 <= date <= 31:
                    print(f"{year}-{month:02}-{date:02}")
                    break
            elif "," in input_date:
                month_date, year = input_date.split(", ")
                month, date = month_date.split(" ")
                if month in month_list:
                    month = month_list.index(month) + 1
                    date, year = int(date), int(year)
                    if 1 <= month <= 12 and 1 <= date <= 31:
                        print(f"{year}-{month:02}-{date:02}")
                        break
        except ValueError:
            pass
main()
