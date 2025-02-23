
def main():
    """Asking the user for 5 times, stores them then show the user where the prompts belong """
    numbers =[]
    for i in range(1,6):
        each_number = int(input(f"What is the No.{i}:"))
        numbers.append(each_number)
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the all the numbers is {sum(numbers)/len(numbers)}")

main()

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn','Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("What is your name?")
if username in usernames:
    print("Access Granted")
else:
    print ("Access Denied")