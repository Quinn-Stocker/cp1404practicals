COLOUR_NAME_TO_HEX_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "Amber": "#ffbf00", "Banana Yellow": "#ffe135",
            "Cardinal": "#c41e3a", "Amethyst": "#9966cc", "Chamoisee": "#a0785a", "Charcoal": "#36454f",
            "Cotton Candy": "#ffbcd9", "Floral White": "#fffaf0"}

max_colour_name = max(len(name) for name in list(COLOUR_NAME_TO_HEX_CODE.keys()))
for colour_key in COLOUR_NAME_TO_HEX_CODE:
    print(f"{colour_key:{max_colour_name}} -\t{COLOUR_NAME_TO_HEX_CODE[colour_key]}")

colour_name = str(input("Enter Colour Name: "))
while colour_name != "":
    try:
        print(colour_name.capitalize(), "is", COLOUR_NAME_TO_HEX_CODE[colour_name.capitalize()])
    except KeyError:
        print("Invalid Short State")

    colour_name = str(input("Enter Colour Name: "))