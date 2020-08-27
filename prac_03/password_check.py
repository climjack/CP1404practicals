PASSWORD_PLACEHOLDER = "*"


def main():
    minimum_password_length = int(input("Please enter the minimum password length: "))
    raw_password = get_password(minimum_password_length)
    print_hidden_password(raw_password)


def print_hidden_password(raw_password):
    print(f"Password: {len(raw_password) * PASSWORD_PLACEHOLDER}")


def get_password(minimum_password_length):
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
    return raw_password


main()
