def main():
    """Create a dictionary of emails and names"""
    emails = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        emails[email] = name
        email = input("Email: ")
    for email, name in emails.items():
        print(f"{name} ({email})")


def get_name(email):
    """Get name from email"""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
