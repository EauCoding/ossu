user_input = input("Expression: ")

user_input = user_input.strip()

number_1, operator, number_2 = user_input.split(" ")

match operator:
    case "+":
        print(f"{float(number_1) + float(number_2):.1f}")
    case "-":
        print(f"{float(number_1) - float(number_2):.1f}")
    case "*":
        print(f"{float(number_1) * float(number_2):.1f}")
    case "/":
        print(f"{float(number_1) / float(number_2):.1f}")
