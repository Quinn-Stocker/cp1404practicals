"""CP1404 Practical - project class file."""
from datetime import date


class Project:
    """Represent a Project object."""

    def __init__(self, name="", start_date=date, priority=0, cost_estimate=0, completion_percentage=0):
        """Initialise a Guitar instance."""

        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.day}/{self.start_date.month}/{self.start_date.year}"
                f", priority {self.priority}, estimate: ${self.cost_estimate}, "
                f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        return self.start_date < other.start_date

    def write_string(self):
        return f"{self.name}\t{self.start_date.day}/{self.start_date.month}/{self.start_date.year}\t{self.priority}\t{self.cost_estimate}\t{self.completion_percentage}\n"

    def is_completed(self):
        return self.completion_percentage == 100
