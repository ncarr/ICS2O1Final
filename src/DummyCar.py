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

    def update(self):
        # If the car is past the farthest distance we let the user reverse to, free its memory
        if self.position[1] > 1440:
            return self.kill()
        # Do the other things Cars do every frame
        super().update()
