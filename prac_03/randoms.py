import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
What did you see on line 1? (5)
What was the smallest number you could have seen, what was the largest? 5 and 20

What did you see on line 2? (9)
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?
Smallest: 3
Largest: 9
No, because 4 is not part of the range which starts from 3 and step is 2,(3, 10, 2).

What did you see on line 3? (4.51618738503126)
What was the smallest number you could have seen, what was the largest?
Smallest: 2.5
Largest: 5.5 

Write code, not a comment, to produce a random number between 1 and 100 inclusive.
"""
print(random.randint(1, 100))
