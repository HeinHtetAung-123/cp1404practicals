"""


   1. Write code that asks the user for their name, then opens a file called name.txt and writes that name to it.
   Use open and close for this question.

   2. In the same file, but as if it were a separate program, write code that opens "name.txt" and reads the name
   (as above) then prints (note the exact output), Hi Bob! (or whatever the name is in the file). Do not simply print
   the user's input variable! Use open and close for this question.

   3. Create a text file called numbers.txt and save it in your prac directory. Put the following three numbers on
   separate lines in the file and save it:
    17
    42
    400
    Write code that opens numbers.txt, reads only the first two numbers, adds them together then prints the result,
    which should be... 59. Use with instead of open and close for this question.

   4. Now write a fourth block of code that prints the total for all lines in numbers.txt. This should work for a file
   with any number of numbers. Use with instead of open and close for this question.

"""
from prac_03.string_formatting import number

#1
FILENAME = "name.txt"
name = input("What is your name?")
out_file = open(FILENAME, "w")
print(name, file=out_file)
out_file.close()

#2
FILENAME = "name.txt"
in_file = open(FILENAME)
name = in_file.read()
print("Hi,Nice to see you",name)
in_file.close()

#3
total_result = 0
FILENAME = "numbers.txt"
in_file= open(FILENAME,"r")
for i in range(0,2):
    number=int(in_file.readline())
    total_result= total_result+number
print(total_result)
in_file.close()

#4
total_result = 0
FILENAME = "numbers.txt"
in_file= open(FILENAME,"r")
numbers= in_file.readlines()
for number in numbers:
    number = int(number)
    total_result= total_result+ number
print(numbers)
print(total_result)
in_file.close()

