import random
import sys

def main():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
        except:
            pass

    number = random.randint(1, level)
    guess = None

    while guess != number:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                if guess < number:
                    print("Too small!")
                elif guess > number:
                    print("Too large!")
                else:
                    print("Just right!")
                    sys.exit()
        except:
            pass


if __name__ == "__main__":
    main()
