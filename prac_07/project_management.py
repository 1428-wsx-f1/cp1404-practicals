"""
Intermediate Exercise, My Guitars
Estimate: 170 minutes
Actual:  minutes
"""

from prac_07.project import Project
from datetime import datetime

FILENAME = "projects.txt"
MENU_STRING = ("-(L)oad projects\n-(S)ave projects\n-(D)isplay projects\n-(F)ilter projects by date"
               "\n-(A)dd new project)\n-(U)pdate project\n-(Q)uit")


def main():
    print(MENU_STRING)
    choice = input(">>> ").upper()
    while choice != "Q":
        # Sort songs based on priority
        # projects.sort(key=itemgetter(YEAR_INDEX, TITLE_INDEX), reverse=False)
        if choice == "L":
            projects = format_data()
        elif choice == "D":
            pass
        elif choice == "A":
            pass
        elif choice == "C":
            pass
        else:
            print("Invalid Menu Choice")
        print(MENU_STRING)
        choice = input(">>> ").upper()


def format_data():
    projects = []
    with open(FILENAME, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            date = datetime.strptime(parts[1], "%d/%m/%Y").date()
            project = Project(parts[0], date, int(parts[2]), float(parts[3]), float(parts[4]))
            projects.append(project)
    print(projects)
    return projects


main()
