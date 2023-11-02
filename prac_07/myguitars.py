"""
DOCSTRING
"""
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = []

    with open(FILENAME, "r") as in_file:
        for guitar_info in in_file:
            guitar_info = guitar_info.split(",")
            guitar = Guitar(guitar_info[0],guitar_info[1],guitar_info[2])
            guitars.append(guitar)

    guitars.sort()

    for guitar in guitars:
        print(guitar,end="")


main()
