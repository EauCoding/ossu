def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return check_start(s) and check_length(s) and check_number(s) and s.isalnum()

def check_start(s):
    return s[0:2].isalpha()

def check_length(s):
    return 2 <= len(s) <= 6

def check_first_number(s):
    for c in s:
        if c.isdigit():
            if int(c) == 0:
                return False
            else:
                return True
    return True

def check_number(s):
    has_digit = False
    for i in range(len(s)):
        if s[i].isdigit():
            has_digit = True
            break
    if has_digit:
        return s[i:].isdigit() and check_first_number(s)
    else:
        return True

main()
