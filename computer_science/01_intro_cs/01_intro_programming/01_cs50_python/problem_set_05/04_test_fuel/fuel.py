def main():
    while True:
        fuel_fraction = input("Fraction: ")
        result = convert(fuel_fraction)
        final_result = gauge(result)
        if final_result:
            break
    print(final_result)

def convert(fraction):
    x, y = fraction.split("/")
    if y == "0":
        raise ZeroDivisionError("Cannot divide by zero!")
    elif (not x.isdigit()) or (not y.isdigit()):
        raise ValueError("Either one or both of the entries are not digits.")
    elif (int(x) > int(y)):
        raise ValueError("X is greater than Y.")
    else:
        return round(int(x) / int(y) * 100)


def gauge(calc):
    if calc >= 99:
        return "F"
    elif calc <= 1:
        return "E"
    return f"{calc}%"

if __name__ == "__main__":
    main()
