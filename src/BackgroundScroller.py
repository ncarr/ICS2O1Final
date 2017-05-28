import pygame
from DummyCar import DummyCar
from Background import Background

class BackgroundScroller(object):
    """Scrolls the background at the speed the car is going"""
    def __init__(self, speed=2):
        self.cars = pygame.sprite.Group()
        self.background = pygame.sprite.Group(Background(self, 0))
        self.deltaY = 0

    def addDummyCar(self, coordinates, speed, direction):
        """Create a DummyCar and add it to the cars group"""
        dummyCar = DummyCar(self, coordinates, speed, direction)
        self.cars.add(dummyCar)
        return dummyCar
