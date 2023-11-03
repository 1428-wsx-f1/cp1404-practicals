"""
Do-From-Scratch Exercises, Guitars!
Estimate: 80 minutes
Actual: 102 minutes
"""

from prac_06.guitar import Guitar


def main():
    """Get guitars referencing the guitars class and display them."""
    guitars = []
    print("My Guitars!")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    name = input("Name: ")
    while name != "":
        year = get_valid_number("Year: ")
        cost = get_valid_number("Cost: $")
        guitar = Guitar(name, int(year), cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        name = input("Name: ")

    display_guitars(guitars)


def display_guitars(guitars):
    """Display formatted list of guitars."""
    print("These Are My Guitars:")
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{is_vintage(guitar)}")


def is_vintage(guitar):
    vintage_string = ""
    if guitar.is_vintage():
        return "(vintage)"
    return vintage_string


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


main()
