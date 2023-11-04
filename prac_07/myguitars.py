"""
CP1404/CP5632 Practical
Guitar Task
"""
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read file of guitars.csv details, save as objects, choose to add to list or display. update csv when done"""

    guitars = []
    # Open the file for reading
    with open(FILENAME, "r") as in_file:
        # loop through all lines in file
        for guitar_info in in_file:
            # split to get list of info
            guitar_info = guitar_info.split(",")
            # assign list of info to object
            guitar = Guitar(guitar_info[0], guitar_info[1], guitar_info[2])
            # add object to a list of all objects
            guitars.append(guitar)

    # sort through the guitars
    guitars.sort()
    # Get a user input
    user_input = input(">>> ")
    # Loop until solo enter key is pressed
    while user_input != "":
        # Print all Guitars in list if input is D
        if user_input.upper() == "D":
            for guitar in guitars:
                print(guitar, end="")
        # Get user input for a new guitar if input is A
        elif user_input.upper() == "A":
            name = get_name_input("Guitar Name: ")
            year = str(get_number_input("Year: "))
            price = str(get_float_input("Price: ")) + "\n"
            guitar = Guitar(name, year, price)
            guitars.append(guitar)
        user_input = input("\n>>> ")

    # write all changes in the list to the csv File
    with open(FILENAME, "w") as in_file:
        for guitar_info in guitars:
            guitar = [guitar_info.name, guitar_info.year, guitar_info.cost]
            guitar = ",".join(guitar)
            in_file.write(guitar)


def get_name_input(input_text):
    """Get a name input with error checking"""
    user_input = ""
    error = True
    # loop until no error
    while error:
        user_input = str(input(input_text))
        if user_input == "":
            print("Input cannot be blank.")
        else:
            error = False
    return user_input


def get_number_input(input_text):
    """Get a number input with error checking"""
    user_input = 0
    error = True
    # loop until no error
    while error:
        try:
            user_input = int(input(input_text))
            if user_input <= 0:
                print("Number must be > 0.")
            else:
                error = False
        except ValueError:
            print("Invalid input; enter a valid number")
    return user_input


def get_float_input(input_text):
    """Get a float input with error checking"""
    user_input = 0
    error = True
    # loop until no error
    while error:
        try:
            user_input = float(input(input_text))
            if user_input <= 0:
                print("Number must be > 0.")
            else:
                error = False
        except ValueError:
            print("Invalid input; enter a valid number")
    return user_input


main()
