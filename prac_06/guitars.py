from prac_06_classes.guitar import Guitar

print("My guitars!")

my_guitars = []

name = str(input("Name: "))
while name != "":
    try:
        year = int(input("Year: "))
    except ValueError:
        print("Invalid Input")
        continue

    try:
        cost = float(input("Cost: "))
    except ValueError:
        print("Invalid Input")
        continue

    my_guitars.append(Guitar(name, year, cost))
    print(f"{name} ({year}) : ${cost} added")

    name = str(input("Name: "))

print("... snip ...\n")

print("These are my guitars:")

max_guitar_name_len = max(len(guitar.name) for guitar in my_guitars)
max_cost_len = max(len(str(guitar.cost)) for guitar in my_guitars)

for guitar_num, guitar in enumerate(my_guitars):
    if guitar.is_vintage():
        vintage_state = "(vintage)"
    else:
        vintage_state = ""

    print(f"Guitar {guitar_num + 1}:\t {guitar.name:>{max_guitar_name_len}}"
          f" ({guitar.year}), worth $ {guitar.cost:>{max_cost_len}} {vintage_state}")
