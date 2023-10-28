"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]:<12} and has {subject[2]:>3} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    complete_data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        complete_data.append(parts)
    return complete_data
    input_file.close()


main()