from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a taxi with fanciness."""
    flag_fall = 4.5

    def __init__(self, fanciness, **kwargs):
        """Initialise a specialised taxi, based on parent class Taxi."""
        super().__init__(**kwargs)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * self.fanciness

    def __str__(self):
        """Return string with flag fall added"""
        return f"{super().__str__()} plus flag fall of ${self.flag_fall:.2f}"

    def get_fare(self):
        """Get current fare."""
        return super().get_fare() + self.flag_fall
