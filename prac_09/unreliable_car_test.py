from unreliable_car import UnreliableCar

def test_unreliable_car():
    """Create an instance of UnreliableCar"""
    my_car = UnreliableCar("Old Clunker", 100, 50)
    print("Attempting to drive 40km:")
    driven_distance = my_car.drive(40)
    print(f"Driven Distance: {driven_distance}km, Remaining Fuel: {my_car.fuel} units")

    print("Attempting to drive another 60km:")
    driven_distance = my_car.drive(60)
    print(f"Driven Distance: {driven_distance}km, Remaining Fuel: {my_car.fuel} units")

    print(my_car)

if __name__ == "__main__":
    test_unreliable_car()
