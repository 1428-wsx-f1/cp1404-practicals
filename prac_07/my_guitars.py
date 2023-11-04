"""
Intermediate Exercise, My Guitars
Estimate: 60 minutes
Actual:  minutes
"""

from prac_07.guitar import Guitar
import csv

FILENAME = "guitars.csv"


def main():
    """Read guitar file and save guitars objects to display."""
    print("My Guitars!")
    guitars = load_guitars(FILENAME)
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def load_guitars(file_name):
    guitars = []
    with open(FILENAME, 'r', newline='') as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            guitars.append(Guitar(row[0], int(row[1]), float(row[2])))
    return guitars


main()
