"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read data from a file and display the data"""
    subject_data = get_subjects()
    print(subject_data)
    display_subject_data(subject_data)


def get_subjects():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subjects = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        subjects.append(parts)
        print("----------")
    input_file.close()
    return subjects


def display_subject_data(subject_data):
    """Display the subject data"""
    for subject in subject_data:
        print(f"{subject[0]} is taught by {subject[1]:13} and has {subject[2]:3} students.")


main()
