"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject.data.txt"

def main():
    data = load_data()
    display_subject_details(data)

def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:

        print(line)
        print(repr(line))

        line = line.strip()
        parts = line.split(',')
        print(parts)

        parts[2] = int(parts[2])
        data.append(parts)
        print(data)

        print("----------")
    input_file.close()
    return data

def display_subject_details(data):
    """Displaying the details of the subject"""
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students.")

main()