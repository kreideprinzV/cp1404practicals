from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes higher quality service and additional charges."""

    flagfall = 4.50

    def __init__(self, name, fuel, price_per_km, fanciness):
        """
        Initialise a SilverServiceTaxi instance, based on parent class Taxi.
        """
        super().__init__(name, fuel, price_per_km * fanciness)
        self.fanciness = fanciness

    def get_fare(self):
        """Calculate and return the total fare including flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation of the SilverServiceTaxi including the flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
