"""
Intermediate Exercise, Unreliable Car
Estimate: 40 minutes
Actual: 68 minutes
"""

from unreliable_car import UnreliableCar


def main():
    """Code to show use of unreliable car class."""
    my_unreliable_car = UnreliableCar(name='My Unreliable Car', fuel=100, reliability=10)
    my_unreliable_car.drive(10)
    print(my_unreliable_car)
    my_reliable_car = UnreliableCar(name='My Reliable Car', fuel=100, reliability=100)
    my_reliable_car.drive(15)
    print(my_reliable_car)


main()
