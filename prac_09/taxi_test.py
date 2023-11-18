"""
Walkthrough Excercise, Test Taxi
Estimate: 20 minutes
Actual: 15 minutes
"""

from prac_09.taxi import Taxi


def main():
    """Code to show use of taxi class."""
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.start_fare()
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)


main()