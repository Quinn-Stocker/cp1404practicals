"""CP1404 Practical - guitar class example."""


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""

        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        return 2023 - self.year

    def is_vintage(self):
        if self.get_age() > 50:
            return True
        else:
            return False




