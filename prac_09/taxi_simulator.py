from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi
def main():
    """Calling this main to run the taxi simulator."""
    print("Let's drive!")
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    bill = 0.0
    current_taxi = None
    while True:
        menu="q)uit, c)hoose taxi, d)rive"
        print(menu)
        choice = input(">>> ").lower()
        if choice == "q":
            print(f"Total trip cost: ${bill:.2f}")
            print("Taxis are now:")
            for taxi in taxis:
                print(taxi)
            break
        elif choice == "c":
            show_taxis(taxis)
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            cost = drive_taxi(current_taxi)
            bill += cost
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill:.2f}")

def show_taxis(taxis):
    """Displaying the list of the available taxis."""
    print("Taxis available: ")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def choose_taxi(taxis):
    """Letting the user choose a taxi."""
    while True:
        try:
            choice = int(input("Choose taxi: "))
            if 0 <= choice < len(taxis):
                return taxis[choice]
            else:
                print("Invalid taxi choice")
        except ValueError:
            print("Invalid input. Please choose a valid taxi number.")

def drive_taxi(current_taxi):
    """Letting user drive it and telling them about the cost."""
    if current_taxi is None:
        print("Choose a taxi before you start driving.")
        return 0.0

    while True:
        try:
            distance = float(input("Drive how far? "))
            if distance <= 0:
                print("Distance must be greater than zero.")
                continue
            cost = current_taxi.drive(distance)
            print(f"Your {current_taxi.name} trip cost you ${cost:.2f}")
            return cost
        except ValueError:
            print("Invalid input. Please enter a valid distance.")

main()
