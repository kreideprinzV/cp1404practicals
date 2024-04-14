from silver_service_taxi import SilverServiceTaxi

def test_silver_service_taxi():
    # Create a SilverServiceTaxi with a fanciness of 2
    luxury_taxi = SilverServiceTaxi("Hummer", 200, 1.23, 2)

    # Start a new fare
    luxury_taxi.start_fare()

    # Drive for 18 km
    luxury_taxi.drive(18)

    # Calculate the fare
    fare = luxury_taxi.get_fare()

    # Output for inspection
    print(luxury_taxi)
    print(f"Calculated Fare: ${fare:.2f}")

    expected_fare = 18 * 1.23 * 2 + SilverServiceTaxi.flagfall
    assert fare == expected_fare, f"Test failed: Fare should be ${expected_fare:.2f} but was ${fare:.2f}"

if __name__ == "__main__":
    test_silver_service_taxi()
