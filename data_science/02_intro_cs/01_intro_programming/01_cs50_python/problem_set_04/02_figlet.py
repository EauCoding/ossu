import sys

from pyfiglet import Figlet

def main():
    if len(sys.argv) == 1:
        user_input = input("Input: ")
        f = Figlet(font="slant")
        print(f.renderText(user_input))
    elif len(sys.argv) == 3:
        try:
            if sys.argv[1] in ["-f", "--font"] and Figlet(font=sys.argv[2]):
                user_input = input("Input: ")
                f = Figlet(font=sys.argv[2])
                print(f.renderText(user_input))
            else:
                sys.exit("Not a valid argument.")
        except:
            sys.exit("Not a valid font.")
    else:
        sys.exit("Not a valid number of argument.")

if __name__ == "__main__":
    main()
