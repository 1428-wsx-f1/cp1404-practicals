CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    """Guitar class to storing details for guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise guitar class."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return guitar details as a string."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the guitars age."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage based on age and current year."""
        return self.get_age() >= VINTAGE_AGE
