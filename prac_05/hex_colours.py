COLOUR_CODES = {"black": "#000000", "white": "#FFFFFFF", "red": "#FF0000"}
print("Available colours:")
for x in COLOUR_CODES:
    print(x.title(), sep=", ")
print("______________________")
colour_lookup = input("Enter colour: ").lower()
while colour_lookup != "":
    try:
        print(COLOUR_CODES[colour_lookup])
    except KeyError:
        print("Colour not found!")
    colour_lookup = input("Enter colour: ").lower()

