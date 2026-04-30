def main():
    name_list = []
    while True:
        try:
            user_input = input("Name: ")
            name_list.append(user_input)
        except:
            break
    print()
    if len(name_list) == 1:
        print(f"Adieu, adieu, to {name_list[0]}")
    elif len(name_list) == 2:
        print(f"Adieu, adieu, to {name_list[0]} and {name_list[1]}")
    else:
        print(f"Adieu, adieu, to {", ".join(name_list[:-1])}, and {name_list[-1]}")

if __name__ == "__main__":
    main()
