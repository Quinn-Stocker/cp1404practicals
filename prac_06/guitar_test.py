from prac_06_classes.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2013, 16035.40)

guitars = [gibson, another_guitar]

for guitar in guitars:
    print(f"{guitar.name} get_age() - Expected {2023 - guitar.year}. Got {guitar.get_age()}")
    if guitar.get_age() > 50:
        print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
    else:
        print(f"{guitar.name} is_vintage() - Expected False. Got {guitar.is_vintage()}")
