"""
Do-From-Scratch Exercises, Guitars!
Estimate: 80 minutes
Actual: 102 minutes
"""

from prac_06.guitar import Guitar


def main():
    """Get guitars referencing the guitars class and display them"""
    guitars = []
    print("My Guitars!")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    name = input("Name: ")
    while name != "":
        prompt = "Year: "
        year = get_valid_number(prompt)
        prompt = "Cost: $"
        cost = get_valid_number(prompt)
        guitar = Guitar(name, int(year), cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        name = input("Name: ")

    display_guitars(guitars)


def display_guitars(guitars):
    """Display formatted list of guitars"""
    for i, guitar in enumerate(guitars, 1):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = " (vintage)"
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


def get_valid_number(prompt):
    """Get a valid integer input"""
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
