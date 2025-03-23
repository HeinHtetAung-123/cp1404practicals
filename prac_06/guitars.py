from prac_06.guitar import Guitar
from operator import attrgetter
def main():
    """A Main function for a collection of guitars"""
    guitars =[]
    print("My Guitars!")

    name = input("Name:")
    while name != "":
        try:
            year= int(input("Year:"))
            cost = float(input("Cost $:"))
            guitar_add = Guitar(name,year,cost)
            guitars.append(guitar_add)
            print(f"{guitar_add} added.")
        except ValueError:
            print("Invalid Input")
        name = input("Guitar Name:")

    if not guitars:
        guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
        guitars.append(Guitar("Fender Stratocruisers", 2014, 765.4))
        guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    guitars.sort(key=attrgetter("year"),reverse=True)

    if guitars:
        print("\nThese are my guitars:")
        for i, guitar in enumerate(guitars,1):
            vintage_string="(vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No guitars :( Quick and buy one!")
main()