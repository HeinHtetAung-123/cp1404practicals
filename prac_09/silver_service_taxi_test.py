from silver_service_taxi import SilverServiceTaxi
def test_silver_service_text():
    """Creating an object to test which is SilverServiceTaxi object"""
    taxi = SilverServiceTaxi("Hummer",100,25)
    taxi.start_fare()
    taxi.drive(32)
    expected_fare = (2*1.23*18)+4.50
    print(f"Actual fare: ${taxi.get_fare()}")
    print(f"Expected fare: ${expected_fare}")
    print(str(taxi))
test_silver_service_text()