"""
CP1404/CP5632 Practical
SilverServiceTaxi Test Task
"""
from silver_service_taxi import SilverServiceTaxi


def main():
    """test code for SilverServiceTaxi"""
    my_taxi = SilverServiceTaxi("Prius 1", 100, 2)
    my_taxi.drive(18)
    print(f"{my_taxi}, Total Fare Price: ${my_taxi.get_fare()}\n")


main()
