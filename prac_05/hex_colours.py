
COLOUR_TO_CODE = {"Absolute Zero": "#0048ba", "Amaranth": "#e52b50", "Amethyst": "#9966cc",
                  "Aquamarine": "#7fffd4", "Ash Grey": "#b2beb5", "Aureolin": "#fdee00",
                  "Battleship Gray": "#848482", "Black Coffee": "#3b2f2f", "Bole": "#79443b",
                  "Byzantium": "#702963"}

colour = input("Enter a colour: ").title()
while colour != "":
    try:
        print(colour, "is", COLOUR_TO_CODE[colour])
    except KeyError:
        print("Invalid colour")
    colour = input("Enter a colour: ").title()
