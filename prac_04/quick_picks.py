import random

SIZE_OF_QUICK_PICKS = 6
LOWEST_QUICK_PICK = 1
HIGHEST_QUICK_PICK = 45


def main():
    number_of_quick_picks = int(input("How many quick picks do you wish to generate? "))
    quick_picks = quick_picks_gen(number_of_quick_picks)
    print_quick_picks(quick_picks)


def quick_picks_gen(number_of_rolls):
    quick_picks = []

    for roll in range(number_of_rolls):
        random_numbers = []
        set_numbers = 0
        while set_numbers < SIZE_OF_QUICK_PICKS:
            potential_number = random.randint(LOWEST_QUICK_PICK,HIGHEST_QUICK_PICK)
            if potential_number not in random_numbers:
                random_numbers.append(potential_number)
                set_numbers += 1
        sorted_numbers = sorted(random_numbers)

        quick_picks.append(sorted_numbers)
    
    return quick_picks


def print_quick_picks(quick_picks):
    for roll in quick_picks:
        for number in roll:
            print(f"{number:>2} ", end="")
        print("\r")


main()