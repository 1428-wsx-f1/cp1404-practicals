"""
Intermediate Exercise, Silver Service Taxi
Estimate: 80 minutes
Actual: 93 minutes
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    """Code to show use of silver service taxi class."""
    my_fancy_taxi = SilverServiceTaxi(name='Fancy Car', fuel=100, fanciness=4)
    my_fancy_taxi.drive(10)
    print(f"{my_fancy_taxi} for a total of ${my_fancy_taxi.get_fare():.2f}")
    my_not_fancy_taxi = SilverServiceTaxi(name='Not Fancy Car', fuel=100, fanciness=1)
    my_not_fancy_taxi.drive(10)
    print(f"{my_not_fancy_taxi} for a total of ${my_not_fancy_taxi.get_fare():.2f}")
    my_kinda_fancy_taxi = SilverServiceTaxi(name='Kinda Fancy Car', fuel=100, fanciness=2)
    my_kinda_fancy_taxi.drive(10)
    print(f"{my_kinda_fancy_taxi} for a total of ${my_kinda_fancy_taxi.get_fare():.2f}")


main()
