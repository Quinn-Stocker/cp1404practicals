from project import Project

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

        elif command.upper() == "D":
            """If 'D' is entered, display the list of projects seperated by completion status."""
            display_projects(projects)

        elif command.upper() == "F":
            """If 'F' is entered, Ask the user for a date and display projects that start after that date in order."""

        elif command.upper() == "A":
            """If 'A' is entered, add a new project to the list."""

        elif command.upper() == "U":
            """If 'U' is entered, Choose a project, then modify the completion % and/or priority"""

        else:
            """Handle an invalid menu choice."""
            print("Invalid menu choice")

        """Print the menu again and read the next command"""
        print(MENU)
        command = str(input(">>> "))


def load_file(file_name):
    projects = []
    with open(file_name, "r") as in_file:
        for line in in_file:
            line = line.split("\t")
            line[-1] = (line[-1]).strip()
            project = Project(line[0],line[1],line[2],line[3],line[4])
            projects.append(project)
    return projects


def get_file_name():
    wrong_file_name = True
    file_name = input("File Name: ")
    while wrong_file_name:
        if file_name != FILENAME:
            print("Provide a valid file")
        else:
            wrong_file_name = False
        file_name = input("File Name: ")
    return file_name


def display_projects(projects):
    print("Incomplete projects:")
    for project in projects:
        if not project.is_completed():
            print(project)

    print("Completed projects:")
    for project in projects:
        if project.is_completed():
            print(project)


main()
