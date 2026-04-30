# prompts the user for the name of a variable in camel case
# outputs the corresponding name in snake case.
# Assume that the user’s input will indeed be in camel case.

user_input = input("camelCase: ")

print("snake_case: ", end="")
for s in user_input:
    if s.isupper():
        print(f"_{s.lower()}", end="")
    else:
        print(s, end="")

print()
