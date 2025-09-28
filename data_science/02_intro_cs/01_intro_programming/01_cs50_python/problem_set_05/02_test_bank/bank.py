def main():
    # Prompt the user for a greeting
    user_input = input("Greeting: ")
    amount = value(user_input)
    print(f"${amount}")

def value(greeting):
    # Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
    greeting = greeting.strip().lower()

    # If the greeting starts with “hello”, output $0
    if greeting.startswith("hello"):
        amount_return = 0
    # If the greeting starts with an “h” (but not “hello”), output $20
    elif greeting.startswith("h"):
        amount_return = 20
    # Otherwise, output $100
    else:
        amount_return = 100

    return amount_return

if __name__ == "__main__":
    main()
