def main():
    # Prompt the user for input
    user_input = input()

    # Call convert() on input
    results = convert(user_input)

    # Print the results
    print(results)

def convert(user_input):
    return user_input.replace(":)", "\N{slightly smiling face}").replace(":(", "\N{slightly frowning face}")

main()
