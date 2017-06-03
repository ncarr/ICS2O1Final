import math
import pygame
from Car import Car

class DummyCar(Car):
    """The cars that drive independently of the user"""
    def __init__(self, scroller, position, speed, direction):
        super().__init__(position, speed, direction)
        self.scroller = scroller
        self.imageSource = pygame.image.load("playerCar.png")

    def deltaY(self, rad):
        """Move DummyCar instances relative to the background"""
        return -self.speed * math.cos(rad) - self.scroller.deltaY
