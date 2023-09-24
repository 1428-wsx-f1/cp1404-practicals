MINIMUM_PASSWORD_LENGTH = 5

password = input("Enter A Password: ")
while len(password) < MINIMUM_PASSWORD_LENGTH:
    print("Password Isn't Long Enough")
    password = input("Enter A Password: ")

print("*" * len(password))
