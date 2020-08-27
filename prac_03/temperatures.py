"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def convert_fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def get_user_input(variable):
    variable_input = float(input(f"{variable}: "))
    return variable_input


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            print(f"Result: {convert_celsius_to_fahrenheit(get_user_input('Celsius')):.2f} F")
        elif choice == "F":
            print(f"Result: {convert_fahrenheit_to_celsius(get_user_input('Fahrenheit')):.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


main()
