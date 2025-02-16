total_price_before_discount = 0
DISCOUNT_RATE = 0.9
DISCOUNT_THRESHOLD =100
number_of_items = int(input("Enter the number of items:"))
while number_of_items <= 0:
    print("Invalid number of items!")
    number_of_items = int(input("Enter the number of items:"))

for i in range(1,number_of_items+1):
    price_of_items = float(input(f"Price of Item No.{i}: "))
    total_price = total_price_before_discount + price_of_items

if total_price_before_discount >DISCOUNT_THRESHOLD:
    total_price_after_discount = total_price_before_discount * DISCOUNT_RATE
    print (f"Total price for {number_of_items} items is ${total_price_after_discount:.2f}")