"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

"""
get sales
while sales >= 0
    calculate bonus (this line is intentionally incomplete pseudocode)
    print bonus
    get sales
do next thing
"""
MINIMUM_SALE = 0
MAXIMUM_SALE = 1000
MINIMUM_DISCOUNT = 0.10
MAXIMUM_DISCOUNT =0.15
sales = float(input("Enter sales: $"))
while sales >= MINIMUM_SALE:
    if sales <MAXIMUM_SALE:
        bonus = sales*MINIMUM_DISCOUNT
    else:
        bonus = sales*MAXIMUM_DISCOUNT
    print (f"Your bonus is ${bonus:.2f}")
    sales = float(input("Enter sales: $"))
print("Your input is invalid, it must not be a negative number!")