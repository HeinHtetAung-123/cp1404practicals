
MINIMUM_LENGTH = 18
def main():
    """Printing the  asterisks as long as the word"""
    password = get_valid_password()
    print(len(password)*"*")

def get_valid_password():
    password = input("What is your password")
    while len(password) < MINIMUM_LENGTH:
        print("Invalid, Try Again!")
        password = input("What is your password")
    return password
main()