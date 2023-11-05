"""
Intermediate Exercise, My Guitars
Estimate: 170 minutes
Actual: 307 minutes
"""

from prac_07.project import Project
from datetime import datetime

FILENAME = "projects.txt"
MENU_STRING = ("-(L)oad projects\n-(S)ave projects\n-(D)isplay projects\n-(F)ilter projects by date"
               "\n-(A)dd new project)\n-(U)pdate project\n-(Q)uit")


def main():
    """Program to load, save, filter, display and update projects"""
    print(MENU_STRING)
    choice = input(">>> ").upper()
    projects = format_data()
    while choice != "Q":
        if choice == "L":
            projects = format_data()
        elif choice == "S":
            save_projects(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_project_by_date(projects)
        elif choice == "A":
            projects = add_project(projects)
        elif choice == "U":
            projects = update_project(projects)
        else:
            print("Invalid Menu Choice")
        print(MENU_STRING)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def format_data():
    """Read projects from file and create a list"""
    projects = []
    with open(FILENAME, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            date = datetime.strptime(parts[1], "%d/%m/%Y")
            project = Project(parts[0], date, int(parts[2]), float(parts[3]), float(parts[4]))
            projects.append(project)
    return projects


def display_projects(projects):
    """Display complete and incomplete projects sorted by priority"""
    incomplete_projects = []
    complete_projects = []
    for project in projects:
        if project.completion_percentage == 100:
            complete_projects.append(project)
        else:
            incomplete_projects.append(project)
    incomplete_projects.sort()
    complete_projects.sort()
    print(f"Incomplete Projects:")
    for project in incomplete_projects:
        print(project)
    print(f"Complete Projects:")
    for project in complete_projects:
        print(project)


def save_projects(projects):
    """Save projects to file"""
    with open(FILENAME, 'w', newline='') as out_file:
        # Header
        print("Name", "Start Date", "Priority", "Cost Estimate",
              "Completion Percentage", sep="\t", file=out_file)
        for project in projects:
            print(project.name, project.start_date.strftime("%d/%m/%Y"),
                  project.priority, project.cost_estimate,
                  project.completion_percentage, sep="\t", file=out_file)


def add_project(projects):
    """Add project to projects list"""
    name = input("Name: ")
    date_string = input("Start date (dd/mm/yy): ")
    start_date = datetime.strptime(date_string, "%d/%m/%Y").date()
    priority = get_valid_number("Priority: ")
    cost_estimate = get_valid_number("Cost estimate: $")
    completion_percentage = get_valid_number("Percent complete: ")
    projects.append(Project(name, start_date, int(priority), cost_estimate, completion_percentage))
    return projects


def filter_project_by_date(projects):
    """Display projects after user specified date"""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    date = datetime.strptime(date_string, "%d/%m/%Y").date()
    for project in projects:
        if project.is_after_date(date):
            print(project)


def update_project(projects):
    """Update percent completion and priority for user specified project"""
    for index, project in enumerate(projects, 0):
        print(f"{index:2} {project}")

    is_finished = False
    while not is_finished:
        try:
            choice = get_valid_number("Project Choice: ")
            print(projects[int(choice)])
        except IndexError:
            print("Invalid Choice")
            choice = int(input("Project Choice: "))
        else:
            is_finished = True
    new_percentage = get_valid_number("New Percentage: ")
    if new_percentage != "":
        new_percentage = get_valid_number("New Percentage: ")
        projects[int(choice)].new_percentage = float(new_percentage)
    new_priority = get_valid_number("New Priority: ")
    if new_priority != "":
        new_priority = get_valid_number("New Priority: ")
        projects[int(choice)].new_priority = int(new_priority)
    return projects


def get_valid_number(prompt):
    """Get a valid integer input."""
    try:
        number = float(input(prompt))
        if number < 0:
            print("Number Can Not Be Negative")
            number = float(input(prompt))
    except ValueError:
        print("Enter A Valid Number")
        number = float(input(prompt))
    return number


main()
