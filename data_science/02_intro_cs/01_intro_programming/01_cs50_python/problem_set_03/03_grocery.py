def main():
    grocery_dct = {}
    while True:
        try:
            grocery_item = input()
            grocery_dct[grocery_item] = grocery_dct.get(grocery_item, 0) + 1
        except EOFError:
            sorted_dct = dict(sorted(grocery_dct.items()))
            print()
            for key, value in sorted_dct.items():
                print(f"{value} {key.upper()}")
            break

main()
