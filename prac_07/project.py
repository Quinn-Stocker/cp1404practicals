"""CP1404 Practical - project class file."""
import datetime

class Project:
    """Represent a Project object."""

    def __init__(self, name="", start_date=datetime, priority=0, cost_estimate=0, completion_percentage=0):
        """Initialise a Guitar instance."""

        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.date}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%")

    def is_completed(self):
        if self.completion_percentage == 100:
            return True
        else:
            return False
