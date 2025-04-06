from taxi import Taxi
def main():
    """Creating an object to start with which is Prius 1 and fuel of 100"""
    my_taxi = Taxi("Prius 1",100)
    my_taxi.drive(40)
    print(my_taxi)
    print(f"Current Fare; ${my_taxi.get_fare()}")
    my_taxi.start_fare()#Starting a new fare to calculate
    my_taxi.drive(100)
    print(my_taxi)
    print(f"Current Fare: ${my_taxi.get_fare()}")
main()