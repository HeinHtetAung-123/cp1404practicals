from prac_07.guitar import Guitar
FILENAME="guitars.csv"

def write_to_file(name, price, year):
    """Writing the details of the guitars to the CSV file."""
    with open("guitars.csv","a")as out_file:
        print(f"{name}, {year}, {price:,.2f}", file=out_file)

def main():
    """Main function to run this program"""
    guitars = read_file(FILENAME)
    for guitar in guitars:
        guitars.sort()
        print(guitar)
    name = input("Name:")
    year = int(input("Year:"))
    price = float(input("Price::"))
    write_to_file(name,price,year)

def read_file(filename):
    """Reading the details of the guitars from a file and returning them in a list"""
    guitars =[]
    with open(filename,"r") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]),  float(parts[2]))
            guitars.append(guitar)
    return guitars

main()


