import random

def main():
    level = get_level()

    next_i = 1
    i = 0
    error = 0
    score = 0

    while i < 10:
        try:
            if i == 0 or i != next_i:
                x, y = generate_integer(level), generate_integer(level)
                i += 1
            result = int(input(f"{x} + {y} = "))
            if result == x + y:
                next_i += 1
                score += 1
                pass
            else:
                error += 1
                print("EEE")
        except ValueError:
            error += 1
            print("EEE")

        if error == 3:
            print(f"{x} + {y} = {x + y}")
            error = 0
            next_i += 1

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    else:
        return random.randint(10**(level - 1), 10**level)

if __name__ == "__main__":
    main()
