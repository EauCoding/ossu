user_input = input("What's the Answer to the Great Question of Life, the Universe, and Everything? ")
user_input = user_input.strip().lower()

match user_input:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
