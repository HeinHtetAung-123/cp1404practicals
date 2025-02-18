"""
CP1404/CP5632 - Practical
Temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""




def main():
    """ Printing the menu for the conversion to two temperatures"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")
def convert_celsius_to_fahrenheit(celsius):
    """Converting Celsius to Fahrenheit degree"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

def convert_fahrenheit_to_celsius(fahrenheit):
    """Converting Fahrenheit to Celsius degree"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()