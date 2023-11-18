from prac_09.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, reliability, **kwargs):
        """Initialise an unreliable car instance, based on parent class Car."""
        super().__init__(**kwargs)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car if drive_chance is less than reliability"""
        drive_chance = random.randint(0, 100)
        if drive_chance >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
