
"""
Estimate: 6 h
Actual:   7 h
"""

import csv
from project import Project
from datetime import datetime


def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header
        for row in csv_reader:
            name, start_date, priority, estimate, completion = row
            projects.append(Project(name, start_date, int(priority), float(estimate), int(completion)))
    return projects


def save_projects(filename, projects):
    with open(filename, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Name', 'Start Date', 'Priority', 'Estimate', 'Completion'])
        for project in projects:
            csv_writer.writerow([project.name, project.start_date, project.priority, project.estimate, project.completion])


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion < 100]
    completed_projects = [project for project in projects if project.completion == 100]

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"{project}")

    print("Completed projects:")
    for project in completed_projects:
        print(f"{project}")


def filter_date():
    date_string = input("Date (d/m/yyyy): ")
    try:
        date = datetime.strptime(date_string, "%d/%m/%Y").date()
        print(f"That day is/was {date.strftime('%A')}")
        print(date.strftime("%d/%m/%Y"))
        return date
    except ValueError:
        print("Invalid date.")
        return None


def new_project(projects):
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))

    projects.append(Project(name, start_date, priority, estimate, completion))


def update_project(projects):
    choice = int(input("Project choice: "))
    if choice < 0 or choice >= len(projects):
        print("Invalid choice.")
        return

    project = projects[choice]
    new_completion = input("New Percentage: ")
    new_priority = input("New Priority: ")

    if new_completion:
        project.completion = int(new_completion)
    if new_priority:
        project.priority = int(new_priority)


def main():
    filename = 'projects.txt'
    projects = load_projects(filename)
    print(f"Welcome to Pythonic Project Management\nLoaded {len(projects)} projects from {filename}")

    while True:
        print("\n(L)oad projects")
        print("(S)ave projects")
        print("(D)isplay projects")
        print("(F)ilter projects by date")
        print("(A)dd new project")
        print("(U)pdate project")
        print("(Q)uit")

        choice = input(">>> ").strip().lower()

        if choice == 'l':
            filename = input("Enter file names to load projects from and load them: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Save projects: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_date(projects)
        elif choice == 'a':
            new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_choice = input("Would you like to save to projects.txt? ").strip().lower()
            if save_choice.startswith('y'):
                save_projects('projects.txt', projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice")


main()
