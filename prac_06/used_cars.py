"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car
def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180, "Lexus Hybrid")
    print(f"Car's fuel amount: {my_car.fuel}")
    my_car.drive(30)
    print(f"Car has {my_car.fuel} fuel left")
    print(my_car)

    print()

    limo = Car(100,"Aston Martin")
    limo.add_fuel(20)
    print(f"Limo's fuel amount: {limo.fuel}")
    limo.drive(115)
    print(f"Limo has {limo.fuel} fuel left")
    print(limo)
main()