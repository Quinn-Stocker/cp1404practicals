from project import Project
from datetime import datetime

"""Define constants for the menu options and the file name"""
MENU = ("- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit\n")

FILENAME = "projects.txt"

"""Define the main function, the entry point of the program."""


def main():
    """Main function to manage the song list application."""

    """Print the main menu."""
    print(MENU)

    """Extract the song list from a CSV file."""
    projects = load_file(FILENAME)

    """Get user command."""
    command = str(input(">>> "))

    """Read the user's command until 'Q' (Quit) is entered."""
    while command.upper() != "Q":
        if command.upper() == "L":
            """If 'L' is entered, Prompt the user for a filename to load projects from and load them."""
            """Get file name from user input."""
            file_name = get_file_name()
            projects = load_file(file_name)

        if command.upper() == "S":
            """If 'S' is entered, Prompt the user for a filename to save projects to and save them."""
            """Get file name from user input."""
            file_name = get_file_name()
            save_file(file_name, projects)

        elif command.upper() == "D":
            """If 'D' is entered, display the list of projects seperated by completion status."""
            display_projects(projects)

        elif command.upper() == "F":
            """If 'F' is entered, Ask the user for a date and display projects that start after that date in order."""
            filter_data(projects)

        elif command.upper() == "A":
            """If 'A' is entered, add a new project to the list."""
            print("Let's add a new project.")

            """Get user input for the project's info."""
            name = get_name_input("Name: ")
            year = get_date_input("Start date (dd/mm/yy): ")
            priority = get_num_float_input("Priority: ", False)
            cost = get_num_float_input("Cost estimate: $", False)
            percent_complete = get_num_float_input("Percent complete: ", False)

            """add all data into Project object"""
            project_info = Project(name, year, priority, cost, percent_complete)

            """add project info into project list"""
            projects.append(project_info)

        elif command.upper() == "U":
            """If 'U' is entered, Choose a project, then modify the completion % and/or priority"""
            update_project(projects)

        else:
            """Handle an invalid menu choice."""
            print("Invalid menu choice")

        """Print the menu again and read the next command"""
        print(MENU)
        command = str(input(">>> "))
    save_file(FILENAME, projects)
    print("Thank you for using custom-built project management software.")


def load_file(file_name):
    projects = []
    with open(file_name, "r") as in_file:
        in_file.readline()
        for line in in_file:
            line = line.split("\t")
            line[-1] = (line[-1]).strip()
            start_date = datetime.strptime(line[1], '%d/%m/%Y').date()
            project_info = Project(line[0], start_date, line[2], line[3], int(line[4]))
            projects.append(project_info)
    return projects


def save_file(file_name, projects):
    with open(file_name, "w") as in_file:
        in_file.write("Name	Start Date	Priority	Cost Estimate	Completion Percentage\n")
        for project in projects:
            in_file.write(project.write_string())


def get_file_name():
    wrong_file_name = True
    file_name = ""
    while wrong_file_name:
        file_name = input("File Name: ")
        if file_name != FILENAME:
            print("Provide a valid file")
        else:
            wrong_file_name = False
    return file_name


def display_projects(projects):
    print("Incomplete projects:")
    for project in projects:
        if not project.is_completed():
            print(project)

    print("\nCompleted projects:")
    for project in projects:
        if project.is_completed():
            print(project)
    print("\n")


def update_project(projects):
    for project_num, project in enumerate(projects):
        print(f"{project_num} - {project}")
    project_choice = int(get_num_float_input("Project choice: ", False))
    print(projects[project_choice])
    percentage = get_num_float_input("New Percentage: ", True)
    priority = get_num_float_input("New Priority: ", True)
    project_info = projects[project_choice]
    if percentage != '':
        project_info.completion_percentage = percentage
    if priority != '':
        project_info.priority = priority
    projects[project_choice] = project_info


def filter_data(projects):
    date = get_date_input("Show projects that start after date (dd/mm/yy): ")
    projects.sort()
    for project in projects:
        if project.start_date >= date:
            print(project)


def get_name_input(input_text):
    user_input = ""
    error = True
    while error:
        user_input = str(input(input_text))
        if user_input == "":
            print("Input cannot be blank.")
        else:
            error = False
    return user_input


def get_date_input(input_text):
    date_input = datetime(1, 1, 1, 0, 0).date()
    error = True
    while error:
        try:
            user_input = input(input_text)
            date_input = datetime.strptime(user_input, '%d/%m/%Y').date()
            if date_input <= datetime(1, 1, 1, 0, 0).date():
                print("Date must be > 00/00/0000.")
            else:
                error = False
        except ValueError:
            print("Invalid input; enter a valid number")
    return date_input


def get_num_float_input(input_text, allow_null):
    user_input = 0
    error = True
    while error:
        try:
            user_input = input(input_text)
            if int(user_input) <= 0:
                print("Number must be > 0.")
            else:
                error = False
        except ValueError:
            if allow_null:
                return ""
            else:
                print("Invalid input; enter a valid number")
    return user_input


main()
