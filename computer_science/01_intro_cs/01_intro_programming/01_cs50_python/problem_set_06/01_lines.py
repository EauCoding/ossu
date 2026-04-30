import sys

def main():
    if len(sys.argv) == 2:
        total_line = count_line(sys.argv[1])
        print(total_line)
    elif len(sys.argv) == 1:
        sys.exit("Too few command-line argumens")
    else:
        sys.exit("Too many command-line arguments")

def count_line(file_name):
    if file_name.endswith(".py"):
        try:
            line_count = 0
            with open(file_name) as file:
                for line in file:
                    line = line.strip()
                    if (not line.startswith("#")) and (line != ""):
                        line_count += 1
            return line_count
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a Python file")

if __name__ == "__main__":
    main()
