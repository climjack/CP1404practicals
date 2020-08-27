PASSWORD_PLACEHOLDER = "*"

minimum_password_length = int(input("Please enter the minimum password length: "))
raw_password = input("Please enter your password: ")
if len(raw_password) >= minimum_password_length:
    raw_password_valid = True
else:
    raw_password_valid = False
while not raw_password_valid:
    print("That does not meet the minimum length")
    raw_password = input("Please enter your password: ")
    if len(raw_password) >= minimum_password_length:
        raw_password_valid = True
print(f"Password: {len(raw_password) * PASSWORD_PLACEHOLDER}")
