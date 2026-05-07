user_input = input("Input: ")

print("Output: ", end="")

for s in user_input:
    for c in "aeiouAEIOU":
        if s == c:
            break
        elif c == "U":
            print(s, end="")

print()
