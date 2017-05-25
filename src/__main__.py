"""Turbulent Tailing
A car chase game where you avoid obstacles and try not to get captured
Nicholas Carr and Victor Lin
2017-05-25
"""

from pygame import *

class Car(sprite.Sprite):
    """All cars inherit this class"""
    MAX_SPEED = 20
    def __init__(self, coordinates, speed, direction):
        self.coordinates = coordinates
        self.speed = speed
        self.direction = direction

class PoliceCar(Car):
    """The police car"""

class UserCar(Car):
    """The car the user controls"""

class DummyCar(Car):
    """The cars that drive independently of the user"""

class BackgroundScroller(object):
    """Scrolls the background at the speed the car is going"""
    def __init__(self):
        self.cars = sprite.Group()

    def addDummyCar(self, coordinates, speed, direction):
        """Create a DummyCar and add it to the cars group"""
        dummyCar = DummyCar(self, coordinates, speed, direction)
        cars.add(dummyCar)
        return dummyCar
