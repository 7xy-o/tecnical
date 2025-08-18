import csv
import sys
from tabulate import tabulate


def main():
    table = []
    heders = []
    length =len(sys.argv)

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a csv file")
    if length < 2:
        sys.exit("Too few command-line arguments")
    if length > 2:
        sys.exit("Too many command-line arguments")
    try:
        with open(sys.argv[1]) as file:
            pizza = csv.DictReader(file)
            for row in pizza:
                table.append(list(row.values()))
                headers = list(row.keys())
    except FileNotFoundError:
        pass
    print(tabulate(table, headers, tablefmt="grid"))

if __name__ == "__main__":
    main()
