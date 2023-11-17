"""
CP1404/CP5632 Practical
Taxi Simulator Task
"""
from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

"""Define constant for the menu options"""
MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """test code for SilverServiceTaxi"""
    print(f"Let's drive!\n{MENU}\n")

    """define variables"""
    current_taxi = None
    current_price = 0.00

    """define taxis"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    """Get user command."""
    command = str(input(">>> "))

    """Read the user's command until 'Q' (Quit) is entered."""
    while command.upper() != "Q":
        if command.upper() == "D":
            """If 'D' is entered, drive the taxi."""
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                taxis[current_taxi].start_fare()
                distance = get_input("Drive how far? ", None)
                cost_dif = taxis[current_taxi].get_fare()
                taxis[current_taxi].drive(distance)
                current_price = current_price + taxis[current_taxi].get_fare()
                print(f"Your {taxis[current_taxi].name} trip cost you ${taxis[current_taxi].get_fare() - cost_dif}")

        elif command.upper() == "C":
            """If 'C' is entered, choose a taxi."""
            print("Taxis available:")
            display_taxis(taxis)
            current_taxi = get_input("Choose taxi: ", len(taxis))
        else:
            """Handle an invalid menu choice."""
            print("Invalid option")

        print(f"Bill to date: ${current_price}")

        """Print the menu again and read the next command"""
        print(MENU)
        command = str(input(">>> "))
    print(f"Total trip cost: ${current_price}")
    print("Taxis are now:")
    display_taxis(taxis)


def get_input(input_text, limit):
    user_input = 0
    error = True
    while error:
        try:
            user_input = int(input(input_text))
            if user_input < 0:
                print("Number must be >= 0.")
            else:
                error = False
            if limit is not None:
                if user_input > (limit-1):
                    print("Invalid taxi choice")
                    error = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return user_input


def display_taxis(taxis):
    for taxi_num, taxi in enumerate(taxis):
        print(f"{taxi_num} - {taxi}")


main()
