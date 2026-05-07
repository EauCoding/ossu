def main():
    while True:
        fuel_fraction = input("Fraction: ")
        try:
            x, y = fuel_fraction.split("/")
            x = int(x)
            y = int(y)
            if y != 0 and x <= y:
                percentage(x, y)
                break
        except ValueError:
            pass

def percentage(x, y):
    calculation = round((x / y) * 100)
    if calculation >= 99:
        print("F")
    elif calculation <= 1:
        print("E")
    else:
        print(f"{calculation}%")

main()
