import random
MIN_NUMBER =1
MAX_NUMBER =45
EACH_COUNT_NUMBER = 6
quick_picks = int(input("Numbers of quick-picks please:"))
for i in range(quick_picks):
    numbers =[]
    while len(numbers) < EACH_COUNT_NUMBER:
        random_number = random.randint(MIN_NUMBER,MAX_NUMBER)
        if random_number not in numbers:
            numbers.append(random_number)
    numbers.sort()
    output = " ".join(f"{random_number:2}" for random_number in numbers)
    print(output)



