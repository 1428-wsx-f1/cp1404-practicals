"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    """Program to take a score and grade it"""
    score = float(input("Enter score: "))
    print(f"{determine_score_grading(score)}")
    score = random.randint(0, 100)
    print(f"{score}\n{determine_score_grading(score)}")


def determine_score_grading(score):
    """Determines grade based on score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
