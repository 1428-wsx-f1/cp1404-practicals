MINIMUM_PASSWORD_LENGTH = 5


def main():
    """Program to get and display password"""
    password = get_password()
    display_password(password)


def display_password(password):
    """Displays the password as *'s"""
    print("*" * len(password))


def get_password():
    """Gets the password and determines if it is long enough"""
    password = input("Enter A Password: ")
    while len(password) <= MINIMUM_PASSWORD_LENGTH:
        print("Password Isn't Long Enough")
        password = input("Enter A Password: ")
    return password


main()
