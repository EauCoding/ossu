# Prompt the user for a greeting
user_input = input("Greeting: ")

# Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
user_input = user_input.strip().lower()

# If the greeting starts with “hello”, output $0
if user_input.startswith("hello"):
    print("$0")
# If the greeting starts with an “h” (but not “hello”), output $20
elif user_input.startswith("h"):
    print("$20")
# Otherwise, output $100
else:
    print("$100")
