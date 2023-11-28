"""
CP1404/CP5632 Practical
Taxi Test Task
"""
from taxi import Taxi


def main():
    """test code for Taxi"""
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(f"{my_taxi}, Total Fare Price: ${my_taxi.get_fare()}\n")
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(f"{my_taxi}, Total Fare Price: ${my_taxi.get_fare()}")


main()
