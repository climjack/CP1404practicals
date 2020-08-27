"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
valid_input = False
while not valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
        valid_input = True
        print("Finished.")
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")

# When will a ValueError occur?
    # If you do not type any number in at all, or if you type with letters
# When will a ZeroDivisionError occur?
    # If the denominator is == 0
# Could you change the code to avoid the possibility of a ZeroDivisionError?
    # Yes, by using a while loop until the user enters a non-zero number