import math
import random
import pygame
from Car import Car

class DummyCar(Car):
    """The cars that drive independently of the user"""
    def __init__(self, scroller, position, speed, direction):
        # Call the Car constructor
        super().__init__(position, speed, direction)
        # Set default attributes
        self.scroller = scroller
        # Randomly choose a colour
        self.imageSource = pygame.image.load(random.choice(["blueCar.png", "greenCar.png", "yellowCar.png", "purpleCar.png", "orangeCar.png"]))
        self.image = self.imageSource
        # Set up a bitmask so we know which pixels cause collisions
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

    def deltaY(self, rad):
        """Move DummyCar instances relative to the background"""
        return -self.speed * math.cos(rad) - self.scroller.deltaY

    def update(self):
        # If the car is past the farthest distance we let the user reverse to, free its memory
        if self.position[1] > 1440:
            return self.kill()
        # Do the other things Cars do every frame
        super().update()
