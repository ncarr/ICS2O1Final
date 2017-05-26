"""Turbulent Tailing
A car chase game where you avoid obstacles and try not to get captured
Nicholas Carr and Victor Lin
2017-05-25
"""

import pygame
import math
from pygame.locals import *
SCREEN = pygame.display.set_mode((1010, 695))
pygame.display.set_caption("Turbulent Tailing")
pygame.display.set_icon(pygame.image.load("../design/icon.png"))
CLOCK = pygame.time.Clock()

class Car(pygame.sprite.Sprite):
    """All cars inherit this class"""
    MAX_SPEED = 20
    def __init__(self, position, speed, direction):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.speed = speed
        self.direction = direction

    def turnLeft(self, degrees=5):
        self.direction += degrees
    def turnRight(self, degrees=5):
        self.direction -= degrees
    def accelerate(self, pixels=2):
        self.speed += pixels
        if self.speed > self.MAX_SPEED:
            self.speed = self.MAX_SPEED
    def decelerate(self, pixels=2):
        self.speed -= pixels
        if self.speed < -self.MAX_SPEED:
            self.speed = -self.MAX_SPEED
    def update(self):
        x, y = self.position
        rad = self.direction * math.pi / 180
        x += -self.speed * math.sin(rad)
        y += -self.speed * math.cos(rad)
        self.position = (x, y)
        self.image = pygame.transform.rotate(pygame.image.load("../assets/png/playerCar.png"), self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

class PoliceCar(Car):
    """The police car"""
    def __init__(self, position=(505, 660), speed=0, direction=0):
        Car.__init__(self, position, speed, direction)

class UserCar(Car):
    """The car the user controls"""
    def __init__(self, scroller, position=(505, 600), speed=0, direction=0):
        Car.__init__(self, position, speed, direction)
        self.scroller = scroller

    def accelerate(self, pixels=2):
        self.scroller.speed += pixels
        if self.scroller.speed > self.MAX_SPEED:
            self.scroller.speed = self.MAX_SPEED
    def decelerate(self, pixels=2):
        self.scroller.speed -= pixels
        if self.scroller.speed < -self.MAX_SPEED:
            self.scroller.speed = -self.MAX_SPEED

class DummyCar(Car):
    """The cars that drive independently of the user"""
    def __init__(self, scroller, position, speed, direction):
        Car.__init__(self, position, speed, direction)
        self.scroller = scroller

    def update(self):
        x, y = self.position
        rad = self.direction * math.pi / 180
        x += -self.speed * math.sin(rad)
        y += -self.speed * math.cos(rad) - self.scroller.speed
        self.position = (x, y)
        self.image = pygame.transform.rotate(pygame.image.load("../assets/png/playerCar.png"), self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

class BackgroundScroller(object):
    """Scrolls the background at the speed the car is going"""
    def __init__(self, speed=2):
        self.cars = pygame.sprite.Group()
        self.speed = 2

    def addDummyCar(self, coordinates, speed, direction):
        """Create a DummyCar and add it to the cars group"""
        dummyCar = DummyCar(self, coordinates, speed, direction)
        self.cars.add(dummyCar)
        return dummyCar

scroller = BackgroundScroller()
scroller.addDummyCar((512, 300), 1, 0)
car = UserCar(scroller)
carGroup = pygame.sprite.GroupSingle(car)
policeCar = PoliceCar()
policeCarGroup = pygame.sprite.GroupSingle(policeCar)
rightDown = leftDown = upDown = downDown = False
while True:
    deltat = CLOCK.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if not hasattr(event, 'key'): continue
        down = event.type == KEYDOWN
        if event.key == K_RIGHT:
            rightDown = down
        elif event.key == K_LEFT:
            leftDown = down
        elif event.key == K_UP:
            upDown = down
        elif event.key == K_DOWN:
            downDown = down
        elif event.key == K_ESCAPE: sys.exit(0) # TODO: load the main menu
    if rightDown:
        car.turnRight()
    elif leftDown:
        car.turnLeft()
    elif upDown:
        car.accelerate()
    elif downDown:
        car.decelerate()

    # RENDERING
    SCREEN.fill((0,0,0))
    scroller.cars.update()
    scroller.cars.draw(SCREEN)
    carGroup.update()
    carGroup.draw(SCREEN)
    policeCarGroup.update()
    policeCarGroup.draw(SCREEN)
    pygame.display.flip()
