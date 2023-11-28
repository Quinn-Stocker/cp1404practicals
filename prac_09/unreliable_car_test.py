"""
CP1404/CP5632 Practical
Unreliable Car Test Task
"""
from unreliable_car import UnreliableCar


def main():
    """test code for UnreliableCar"""
    my_car = UnreliableCar("Prius 1", 100, 60)
    my_car.drive(40)
    print(my_car)
    my_car.drive(100)
    print(my_car)


main()
