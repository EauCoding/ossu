import csv
import sys
from tabulate import tabulate

def main():
    if len(sys.argv) == 2:
        headers, table = get_table_data(sys.argv[1])
        print(tabulate(table, headers, tablefmt="grid"))
    elif len(sys.argv) == 1:
        sys.exit("Too few command-line argumens")
    else:
        sys.exit("Too many command-line arguments")

def get_table_data(file_name):
    if file_name.endswith(".csv"):
        try:
            table = list()
            with open(file_name) as file:
                reader = csv.reader(file)
                for i, line in enumerate(reader):
                    if i == 0:
                        headers = [line[0], line[1], line[2]]
                    else:
                        table.append([line[0], line[1], line[2]])
            return headers, table
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()
