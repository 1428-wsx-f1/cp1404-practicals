
def main():
    print("(G)et valid score\n(P)rint result\n(S)how stars\n(Q)uit")
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            get_valid_score()
        elif choice == "P":
            print(f"{get_valid_score(score)}")
        elif choice == "S":
            print("*" * get_valid_score())
        else:
            print("Invalid choice")
        print("(G)et valid score\n(P)rint result\n(S)how stars\n(Q)uit")
        choice = input(">>> ").upper()
    print("Code Finished")


def get_valid_score():
    """Function to get a valid score between 0 and 100"""
    score = int(input("Enter Score: "))
    while score < 0 or score > 100:
        print("Invalid Score")
        score = int(input("Enter Score: "))
    return score


def display_score(score):
    """Function to get a valid score between 0 and 100"""
    score = int(input("Enter Score: "))
    while score < 0 or score > 100:
        print("Invalid Score")
        score = int(input("Enter Score: "))
    return score


main()
