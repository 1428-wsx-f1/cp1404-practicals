"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A value error occurs when an invalid value is entered. For example if you're supposed to
enter a number but enter a string instead you will get a value error.
2. When will a ZeroDivisionError occur?
A ZeroDivisionError occurs when the user/program tries to divide a number by 0 which is mathematically impossible.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Look before you leap and easy to ask for forgiveness
You could change the code to avoid the error by dividing by 1 instead of 0.
"""


try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if numerator < 1:
        numerator = 1
    if denominator < 1:
        denominator = 1
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
