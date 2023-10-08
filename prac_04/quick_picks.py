import random

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 45
NUMBER_OF_RANDOM_NUMBERS = 6


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("Please just enter a proper number")
        number_of_quick_picks = int(input("How many quick picks? "))

    for i in range(number_of_quick_picks):
        quick_picks = []
        for j in range(NUMBER_OF_RANDOM_NUMBERS):
            number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
            while number in quick_picks:
                number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
            quick_picks.append(number)
        quick_picks.sort()
        print(" ".join(f"{number:3}" for number in quick_picks))


main()
