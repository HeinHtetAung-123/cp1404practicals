from unreliable_car import UnreliableCar

def main():
    """Calling this main function to run all the tests """
    drive_reliable()
    drive_unreliable()
    drive_partially_reliable()
    print("All the tests are now completed.")

def drive_reliable():
    """Test case with 100% reliability"""
    car = UnreliableCar("Reliable Car",100,100)
    result = car.drive(50)
    print(f"Test with 100% reliability: Expected 50, Got back {result}")

def drive_unreliable():
    """Test case with 0% reliability"""
    car = UnreliableCar("Unreliable Car",100,0)
    result = car.drive(50)
    print(f"Test with )% reliability: Expected 0, Got back {result}")

def drive_partially_reliable():
    """Test case with 30% reliability"""
    car = UnreliableCar("Partially Reliable Car", 100, 30)
    count = 0
    for _ in range(100):
        result = car.drive(50)
        if result > 0:
            count += 1
    print(f"Test 30% reliability: Expected between 15 and 45, Got {count}")
main()