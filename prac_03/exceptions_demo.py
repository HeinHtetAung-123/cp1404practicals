valid_input = False
while not valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        while denominator == 0:
            print ("Not divisible by Zero")
            denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
        valid_input = True
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    print("Finished.")
"""

CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
(ValueError occurs if the user enters a non-integer input.)
2. When will a ZeroDivisionError occur?
(A ZeroDivisionError will occur if the denominator is  0 and is not handled before performing the division process)
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
(Remove the except ZeroDivisionError block since the while loop check the denominator to not be zero before division.)
If you could figure out the answer to question 3, then make this change now.
"""