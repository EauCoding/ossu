def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    check = 1
    for c in s:
        if c.isdigit():
            if int(c) == 0:
                check_first_number = False
                check = 0
                break
            else:
                check_first_number = True
                check = 0
                break
    if check:
        check_first_number = True

    has_digit = False
    for i in range(len(s)):
        if s[i].isdigit():
            has_digit = True
            break
    if has_digit:
        check_number = s[i:].isdigit() and check_first_number
    else:
        check_number = True

    return (s[0:2].isalpha()) and (2 <= len(s) <= 6) and check_number and (s.isalnum())

if __name__ == "__main__":
    main()
