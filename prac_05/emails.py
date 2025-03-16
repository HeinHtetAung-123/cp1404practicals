def main():
    """ Stores users' emails and names in a dictionary."""
    SPECIAL_CHAR = "@"
    email_to_name = {}
    email = input("Email:")
    while email != "":
        if SPECIAL_CHAR not in email:
            print("The email must contain (@)!")
            email = input("Email:")
        name = extract_name(email)
        question = input(f"Is your name {name}? (Y/N)").strip().upper()
        if question != "Y" and question != "":
            name = input("Name:")
        email_to_name[name] = name
        email = input("Email:")
    print_email(email_to_name)

def extract_name(email):
    """Extracting the name from the email by splitting at '@'."""
    name_part = email.split("@")[0]
    name_parts = name_part.split('.')
    name = " ".join(name_parts).title()
    return name

def print_email(email_to_name):
    """Printing email and the name"""
    for email,name in email_to_name.items():
        print (f"{name} ({email})")
main()

