from prac_06.guitar import Guitar


def test():
    """Function to run tests for get_age() and is_vintage() in Guitar class"""
    guitar_1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    other_guitar = Guitar("Another Guitar", 2013, 2000)
    print(f"Gibson L-5 CES get_age() - Expected 100. Got {guitar_1.get_age()}")
    print(f"Another Guitar get_age() - Expected 9. Got {other_guitar.get_age()}")
    print(f"Gibson L-5 CES is_vintage() is_vintage() - Expected True. Got {guitar_1.is_vintage()}")
    print(f"Another Guitar is_vintage() is_vintage() - Expected False. Got {other_guitar.is_vintage()}")


test()
