class ProgrammingLanguage:
    """Programming language class to store details about a programming language."""

    def __init__(self, language_name="", typing="", reflection=False, year=0):
        """Initialise the program language class."""
        self.language_name = language_name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return whether the program language is dynamic."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return program language details as a string."""
        return f"{self.language_name}, {self.typing}, {self.reflection}, {self.year}"
