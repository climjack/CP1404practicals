finished = False
result = 0
while not finished:
    try:
        number = int(input("Please enter a number: "))
        finished = True
    except ValueError:  # TODO - add something after except
        print("Please enter a valid integer.")
print("Valid result is:", number)
