"""
Emails
Estimate: 70 minutes
Actual:   61 minutes
"""


def main():
    """Create a dictionary of emails to names until a blank input"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = retrieve_name(email)
        confirm_name = input(f"Is your name {name}? (y/n) ").lower()
        if confirm_name != "y" and confirm_name != "":
            name = input("Name: ")
        email_to_name[email] = name.title()
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def retrieve_name(email):
    """Retrieve the likely name from the email address"""
    raw_name = email.split("@")[0]
    parts = raw_name.split(".")
    name = "".join(parts).title()
    return name


main()
