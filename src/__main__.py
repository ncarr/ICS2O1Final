"""Turbulent Tailing
A car chase game where you avoid obstacles and try not to get captured
Nicholas Carr and Victor Lin
2017-05-25
"""

import pygame
import math
from pygame.locals import *
SCREEN = pygame.display.set_mode((1010, 695))
CLOCK = pygame.time.Clock()

class Car(pygame.sprite.Sprite):
    """All cars inherit this class"""
    MAX_SPEED = 20
    def __init__(self, position, speed, direction):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.speed = speed
        self.direction = direction

class PoliceCar(Car):
    """The police car"""

class UserCar(Car):
    """The car the user controls"""

class DummyCar(Car):
    """The cars that drive independently of the user"""
    def __init__(self, scroller, position, speed, direction):
        Car.__init__(self, position, speed, direction)
        self.scroller = scroller

    def update(self, deltat):
        x, y = self.position
        rad = self.direction * math.pi / 180
        x += -self.speed * math.sin(rad)
        y += -self.speed * math.cos(rad)
        self.position = (x, y)
        self.image = pygame.transform.rotate(pygame.image.load("../assets/png/playerCar.png"), self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

class BackgroundScroller(object):
    """Scrolls the background at the speed the car is going"""
    def __init__(self):
        self.cars = pygame.sprite.Group()

    def addDummyCar(self, coordinates, speed, direction):
        """Create a DummyCar and add it to the cars group"""
        dummyCar = DummyCar(self, coordinates, speed, direction)
        self.cars.add(dummyCar)
        return dummyCar

scroller = BackgroundScroller()
car = scroller.addDummyCar((512, 300), 1, 0)
while True:
    deltat = CLOCK.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # RENDERING
    SCREEN.fill((0,0,0))
    scroller.cars.update(deltat)
    scroller.cars.draw(SCREEN)
    pygame.display.flip()
