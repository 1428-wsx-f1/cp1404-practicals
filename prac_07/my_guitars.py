"""
Intermediate Exercise, My Guitars
Estimate: 60 minutes
Actual:  minutes
"""

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read guitar file and save guitars objects to display."""
    guitars = []
    with open(FILENAME, 'r', newline='') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
    guitars.sort()
    for guitar in guitars:
        print(guitar)


main()
