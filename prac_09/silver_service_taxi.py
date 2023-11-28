"""
CP1404/CP5632 Practical
SilverServiceTaxi class
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness."""
    price_per_km = 1.23
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness: float):
        """Initialise a SilverServiceTaxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.price_per_km = self.price_per_km * fanciness

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()} plus flagfall of %{self.flagfall}"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall
