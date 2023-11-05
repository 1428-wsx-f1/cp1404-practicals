
class Project:
    """Project class to storing details for projects."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise project class."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """Return project details."""
        return (f"{self.name}, Start: {self.start_date.strftime('%d/%m/%Y')}, Priority {self.priority}, "
                f"Estimate ${self.cost_estimate:,.2f}, Completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Compare priority for sorting."""
        return self.priority < other.priority

    def is_after_date(self, date):
        """Determine if project is after user specified date."""
        return self.start_date >= date
