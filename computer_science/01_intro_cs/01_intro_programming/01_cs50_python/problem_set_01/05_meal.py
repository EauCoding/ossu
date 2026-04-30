def main():
    user_input = input("What time is it? ")
    time = convert(user_input)

    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")


def convert(time):
    hour, minute = time.split(":")
    minute = float(minute) / 60
    hour = float(hour) + minute
    return hour


if __name__ == "__main__":
    main()
