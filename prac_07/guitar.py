import csv
from datetime import datetime

class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar with name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return how old the guitar is in years."""
        return datetime.now().year - self.year

    def is_vintage(self):
        """Determine if the guitar is at least 50 years old."""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Define the less than operator for sorting Guitars by year."""
        return self.year < other.year
