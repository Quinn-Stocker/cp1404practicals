"""
CP1404/CP5632 Practical
UnreliableCar class
"""
from car import Car
from random import randint


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""
    def __init__(self, name, fuel, reliability: float):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()}, Reliability: {self.reliability}%"

    def drive(self, distance):
        """Drive like parent Car but only if random number < reliability."""
        if self.reliability <= randint(0, 100):
            distance = 0
            print("Car Failed")
        driven_distance = super().drive(distance)
        return driven_distance
