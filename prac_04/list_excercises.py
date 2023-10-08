"""
CP1404/CP5632 Practical
List Exercises
"""

# Basic List Operations
NUMBER_OF_NUMBERS = 5
numbers = []
for i in range(NUMBER_OF_NUMBERS):
    number = int(input("Number: "))
    numbers.append(number)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average number is {sum(numbers) / NUMBER_OF_NUMBERS}")


# Inadequate Security Checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Username: ")
if username in usernames:
    print("Access Granted")
else:
    print("Access Denied")
