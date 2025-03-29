import datetime
from prac_07.project import Project
FILENAME= "projects.txt"

def load_file(filename):
    """Loading the details of the projects from the file and returning them in a list."""
    projects =[]
    with open(filename,"r")as file:
        file.readline()
        for line in file:
            name, start_date, priority,cost,completion=line.strip().split("\t")
            project  = Project(name, start_date, int(priority), float(cost), int(completion))
            projects.append(project)
        print(f"Loaded {len(projects)} projects from{filename}")
    return projects

def validate_file(projects):
    """Validating the user's input of a file while trying to load data from it."""
    filename = input("What is the filename? ")
    if filename != "":
        try:
            projects = load_file(filename)
            print(projects)
        except FileNotFoundError:
            print("File is not found!")
    return projects

def save_data(projects):
    """Saving the name of the file"""
    filename = input("What is the filename you would like to save? ")
    if filename:
        save_file(projects, filename)

def save_file(projects, filename):
    """Saving the details of the projects to a file. """
    with open(filename,"w")as out_file:
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost}\t{project.completion}")

def separate_project(projects):
    """Checking the projects and splitting them into completed and incomplete categories."""
    completed=[]
    uncompleted=[]
    for project in projects:
        if project.is_complete():
            completed.append(project)
        else:
            uncompleted.append(project)
    completed.sort()
    uncompleted.sort()
    return completed,uncompleted

def sort_projects(projects):
    date_list =[]
    for project in projects:
        if project.start_date not in date_list:
            date_list.append(project.start_date)
    date_list.sort()
    sorted_project =[]
    for date in date_list:
        for project in projects:
            if project.start_date == date:
                sorted_project.append(project)
    return sorted_project

def display_projects(projects):
    completed,uncompleted= separate_project(projects)
    print("Incomplete projects:")
    display_individual_details(uncompleted)
    print("\nCompleted projects:")
    display_individual_details(completed)

def display_individual_details(projects):
    """Print details of each project in the given list."""
    for number, project in enumerate(projects):
        print(f"{number+1} {project}")

def filter_projects(projects):
    """Filter and display projects that start after a user-provided date."""
    is_valid =False
    while not is_valid:
        try:
            date=input("Show projects that start after date (dd/mm/yyyy): ")
            datetime.datetime.strptime(date, "%d/%m/%Y")
            filtered_projects_date=[project for project in projects if project.compare_date(date)]
            filtered_projects_date = sort_projects(filtered_projects_date)
            display_individual_details(filtered_projects_date)
            is_valid=True
        except ValueError:
            print("Incorrect data format, it should be (dd/mm/yyyy)")
    return projects

def add_project(projects):
    """Adding a new project to the list."""
    print("let's add a  new project!")
    try:
        name = input("Name:")
        start_date = input("Start date in the format of (dd/mm/yyyy): ")
        priority = int(input("Priority: "))
        cost = input("Estimate: ").replace("$","")
        cost = int(cost)
        completion = input("Percent Complete: ")
        project = Project(str(name),str(start_date),int(priority),int(cost),float(completion))
        projects.append(project)
    except ValueError:
        print("Invalid Input")


def update_project(projects):
    """Updating an existing project's completion percentage or the priority."""
    projects = sort_projects(projects)
    display_individual_details(projects)
    projects_number ={}
    for number,project in enumerate(projects):
        projects_number[str(number +1)] = project
    try:
        choice = input("Your Project Choice: ")
        chosen_project = projects_number[choice]
        print(chosen_project)
        new_percentage = input("New Percentage:")
        new_priority = input("New Priority:")
        if new_percentage:
            chosen_project.update_percentage(int(new_percentage))
        if new_priority:
            chosen_project.update_priority(int(new_priority))
    except KeyError:
        print("Invalid Input")
    return projects

def main():
    """Main function to run the project management system."""
    MENU ="""
    -(L)oad projects
    -(S)ave projects
    -(D)isplay projects
    -(F)ilter projects by date
    -(A)dd new project
    -(U)pdate project
    -(Q)uit
    """
    print("Welcome to Pythonic Project Management")
    projects = load_file('projects.txt')
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "L":
            projects = validate_file(projects)
        elif choice =="S":
            save_data(projects)
        elif choice =="D":
            display_projects(projects)
        elif choice =="F":
            projects= filter_projects(projects)
        elif choice=="A":
            add_project(projects)
        elif choice=="U":
            projects=update_project(projects)
        else:
            print("Invalid Choice")
        print(MENU)
        choice = input(">>>").upper()
    print("Thank you for using the custom-built project management software.")
main()


            