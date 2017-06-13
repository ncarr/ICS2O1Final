import math
import pygame
from Car import Car
from Sound import Sound

class PoliceCar(Car):
    """The police car"""
    MAX_SPEED = 12
    def __init__(self, scroller, position=(505, 1700), speed=12, direction=0):
        super().__init__(position, speed, direction)
        self.scroller = scroller
        self.imageSource = pygame.image.load("policeCar.png")
        self.image = self.imageSource
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
    def deltaY(self, rad):
        """Move PoliceCar instances relative to the background"""
        return -self.speed * math.cos(rad) - self.scroller.deltaY
    def update(self):
        """Update the volume every frame"""
        Sound.setSirenVolume(100 / (self.position[1] - 650))
        print(100 / (self.position[1] - 650))
        # Call the parent class' constructor
        super().update()
