"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
FIRST_THRESHOLD = 90
SECOND_THRESHOLD = 50


def main():
    """Display the grade based on the score input"""
    score = get_score()
    grade = get_grade(score)
    print(grade)
    random_score = random.randint(MINIMUM_SCORE,MAXIMUM_SCORE)
    random_result = get_grade(random_score)
    print(random_result,random_score)

def get_score():
    "Making sure the input is valid"
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score

def get_grade(score):
    """Using the score and determining the result """
    if score >= FIRST_THRESHOLD:
        grade = "Excellent"
    elif score >= SECOND_THRESHOLD:
        grade = "Passable"
    else:
         grade ="Bad"
    return grade
main()

