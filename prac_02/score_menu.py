MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
FIRST_THRESHOLD = 90
SECOND_THRESHOLD = 50
MENU = """G - Get a valid score(must be 0-100 inclusive)
P - Print the result
S- Show the stars
Q - Quit"""

def main():
    """Displaying the main menu"""
    print(MENU)
    choice = input("Enter your choice:").upper()
    while choice != "Q":
        if choice =="G":
            score = get_the_score()
        elif choice == "P":
            score = validate_the_score(score)
            grade = get_the_grade(score)
            print (grade)
        elif choice == "S":
            score = validate_the_score(score)
            show_stars(score)
        else:
            print("Invalid Choice of yours, try again!")
            print(MENU)
            choice = input("Enter your choice:").upper()
    print("Quit,Farewell")



def get_the_score():
    """Inputting the score """
    score = float(input("What is your score?"))
    while score < MINIMUM_SCORE or score>MAXIMUM_SCORE:
        print("Invalid score, try again!")
        score = float(input("What is your score?"))
    return score

def validate_the_score(score):
    """Validating the score"""
    if score =="":
        score = get_the_score()
    return score

def get_the_grade(score):
    """Using the score and determining the result """
    if score >= FIRST_THRESHOLD:
        grade = "Excellent"
    elif score >= SECOND_THRESHOLD:
        grade = "Passable"
    else:
        grade = "Bad"
    return grade

def show_stars(score):
    """Showing the stars"""
    int(score)
    print(score*"*")


