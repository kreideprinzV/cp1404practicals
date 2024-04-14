# This assumes you have a file named taxi.py where the Taxi class is defined as shown
from taxi import Taxi

def test_taxi():
    """Create a new taxi object
    Restart the meter
     Print the taxi's details and the current fare"""
    my_taxi = Taxi("Prius 1", 100, 1.23)


    my_taxi.drive(40)
    print("After driving 40km:")
    print(my_taxi)
    print(f"Current Fare: ${my_taxi.get_fare():.2f}")

    my_taxi.start_fare()
    my_taxi.drive(100)


    print("After driving another 100km:")
    print(my_taxi)
    print(f"Current Fare: ${my_taxi.get_fare():.2f}")

if __name__ == "__main__":
    test_taxi()
