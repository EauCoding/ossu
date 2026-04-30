import csv
import sys

def main():
    if len(sys.argv) == 3:
        data = get_file_data(sys.argv[1])
        write_file_data(data, sys.argv[2])
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line argumens")
    else:
        sys.exit("Too many command-line arguments")

def get_file_data(in_filename):
    if in_filename.endswith(".csv"):
        try:
            data = [{"first": "first", "last": "last", "house": "house"}]
            with open(in_filename) as in_file:
                reader = csv.DictReader(in_file)
                for row in reader:
                    last_name, first_name = row["name"].split(", ")
                    data.append({"first": first_name, "last": last_name, "house": row["house"]})
            return data
        except FileNotFoundError:
            sys.exit(f"Could not read {in_filename}")
    else:
        sys.exit(f"{in_filename} is not a CSV file")

def write_file_data(data, out_filename):
    if out_filename.endswith(".csv"):
        try:
            with open(out_filename, "w") as out_file:
                writer = csv.DictWriter(out_file, fieldnames=["first", "last", "house"])
                for row in data:
                    writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})
        except FileNotFoundError:
            sys.exit(f"Could not read {out_filename}")
    else:
        sys.exit(f"{out_filename} is not a CSV file")

if __name__ == "__main__":
    main()
