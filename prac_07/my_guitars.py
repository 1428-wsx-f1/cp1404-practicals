"""
Intermediate Exercise, My Guitars
Estimate: 60 minutes
Actual: 72 minutes
"""

from prac_07.guitar import Guitar
import csv

FILENAME = "guitars.csv"


def main():
    """Read guitar file and save guitars objects to display."""
    print("My Guitars!")
    guitars = load_guitars()
    guitars.sort()
    for guitar in guitars:
        print(guitar)
    guitars = get_guitars(guitars)
    save_guitars(guitars)


def load_guitars():
    """Load guitars from csv file."""
    guitars = []
    with open(FILENAME, 'r', newline='') as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            # Name, Year, Cost
            guitars.append(Guitar(row[0], int(row[1]), float(row[2])))
    return guitars


def get_guitars(guitars):
    """Get guitars details from user."""
    name = input("Name: ")
    while name != "":
        year = get_valid_number("Year: ")
        cost = get_valid_number("Cost: $")
        guitar = Guitar(name, int(year), cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        name = input("Name: ")
    return guitars


def get_valid_number(prompt):
    """Get a valid integer input."""
    try:
        number = float(input(prompt))
        if number <= 0:
            print("Enter A Number > 0")
            number = float(input(prompt))
    except ValueError:
        print("Enter A Valid Number")
        number = float(input(prompt))
    return number


def save_guitars(guitars):
    with open(FILENAME, 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            # Name, Year, Cost
            writer.writerow((guitar.name, guitar.year, guitar.cost))
    return guitars


main()
