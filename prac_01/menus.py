"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

name = input("What is your name?")
menu = "(H)ello\n(G)oodbye\n(Q)uit"
print(menu)
choice = input("Enter your choice:>>>").upper()
while choice != "Q":
   if choice == "H":
       print(f"Hello {name}")
   elif choice == "G":
       print(f"Goodbye {name}")
   else:
       print ("Invalid Choice!")
   print (menu)
   choice = input("Enter your choice:>>>").upper()
print("Finished.")