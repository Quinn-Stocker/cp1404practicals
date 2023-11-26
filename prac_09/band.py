"""
CP1404/CP5632 Practical
Band class
"""


class Band:
    """Class called Band used for storing details of a band"""

    def __init__(self, name=""):
        """Initialise Band."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string for Band."""
        return f"{self.name} ({', '.join([str(musician) for musician in self.musicians])})"

    def __repr__(self):
        """Return a string for Band."""
        return str(self)

    def add(self, musician):
        """Add musician to the band"""
        self.musicians.append(musician)

    def play(self):
        """Play band."""
        return '\n'.join([musician.play() for musician in self.musicians])
