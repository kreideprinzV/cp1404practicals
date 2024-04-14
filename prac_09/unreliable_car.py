import random
from prac_09.car import Car  # Update the import path based on your project structure

class UnreliableCar(Car):
    """A Car class that may not always drive when asked due to reliability issues."""

    def __init__(self, name, fuel, reliability):
        """
        Initialise an UnreliableCar instance, based on parent class Car.
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """
        Attempt to drive the car a given distance, depending on its reliability.
        """
        if random.random() * 100 < self.reliability:
            return super().drive(distance)
        return 0  # Car does not move due to unreliability
