MINIMUM_PASSWORD_LENGTH = 5


def main():
    password = get_password()
    display_password(password)


def display_password(password):
    print("*" * len(password))


def get_password():
    password = input("Enter A Password: ")
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print("Password Isn't Long Enough")
        password = input("Enter A Password: ")
    return password


main()
