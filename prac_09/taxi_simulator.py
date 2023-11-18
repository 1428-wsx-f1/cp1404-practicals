"""
Intermediate Exercise, Band
Estimate: 150 minutes
Actual: 184 minutes
"""

from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU_STRING = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi(name="Limo", fuel=100, fanciness=2),
             SilverServiceTaxi(name="Hummer", fuel=200, fanciness=4)]
    current_taxi = None
    bill = 0
    print("Let's Drive")
    print(MENU_STRING)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            print("Taxis Available")
            display_taxis(taxis)
            taxi_choice = int(get_valid_number("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
            except ValueError:
                print("Choice has to be number")
        elif choice == "D":
            if current_taxi:
                current_taxi.start_fare()
                distance = int(get_valid_number("Drive how far? "))
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} cost you {trip_cost}")
                bill += current_taxi.get_fare()
            else:
                print("You need to choose a taxi before you can drive")

        else:
            print("Invalid option")
        print(f"Bill to date: ${bill:.2f}")
        print(MENU_STRING)
        choice = input(">>> ").upper()
    print(f"Bill to date: ${bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display all taxis with a number to choose."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def get_valid_number(prompt):
    """Get a valid integer input."""
    is_valid_input = False
    while not is_valid_input:
        try:
            number = float(input(prompt))
            if number < 0:
                print("Number Can Not Be Negative")
                number = float(input(prompt))
            else:
                is_valid_input = True
        except ValueError:
            print("Enter A Valid Number")
    return number


main()
