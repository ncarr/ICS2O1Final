import pygame
from Car import Car

class PoliceCar(Car):
    """The police car"""
    def __init__(self, position=(505, 700), speed=0, direction=0):
        super().__init__(position, speed, direction)
        self.imageSource = pygame.image.load("policeCar.png")
        self.image = self.imageSource
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
