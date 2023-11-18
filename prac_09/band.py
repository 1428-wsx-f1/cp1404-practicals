"""
Intermediate Exercise, Band
Estimate: 30 minutes
Actual: 28 minutes
"""


class Band:
    """Band class"""

    def __init__(self, name=""):
        """Construct a Band with a name and empty musician collection."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string of the object."""
        return f"{self.name} ({self.musicians})"

    def add(self, musician):
        """Add band member."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the musician playing their instrument."""
        return "\n".join(musician.play() for musician in self.musicians)
