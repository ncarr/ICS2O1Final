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
        self.isAccelerating = 0
        self.turnDirection = 0

    def startTurning(self, degrees=5):
        self.turnDirection = degrees
    def stopTurning(self):
        self.turnDirection = 0
    def turn(self, degrees=5):
        self.direction += degrees
    def startAcceleration(self, pixels=2):
        self.isAccelerating = pixels
    def stopAcceleration(self):
        self.isAccelerating = 0
    def accelerate(self, pixels=2):
        self.speed += pixels
        if self.speed > self.MAX_SPEED:
            self.speed = self.MAX_SPEED
        elif self.speed < -self.MAX_SPEED:
            self.speed = -self.MAX_SPEED
    def deltaX(self, rad):
        return -self.speed * math.sin(rad)
    def deltaY(self, rad):
        return -self.speed * math.cos(rad)
    def update(self):
        self.turn(self.turnDirection)
        self.accelerate(self.isAccelerating)
        x, y = self.position
        rad = self.direction * math.pi / 180
        x += self.deltaX(rad)
        y += self.deltaY(rad)
        self.position = (x, y)
        self.image = pygame.transform.rotate(self.imageSource, self.direction) #pygame.image.load("../assets/png/playerCar.png")
        self.rect = self.image.get_rect()
        self.rect.center = self.position

class PoliceCar(Car):
    """The police car"""
    def __init__(self, position=(505, 700), speed=0, direction=0):
        Car.__init__(self, position, speed, direction)
        self.imageSource = pygame.image.load("../assets/png/policeCar.png")

class UserCar(Car):
    """The car the user controls"""
    def __init__(self, scroller, position=(505, 450), speed=0, direction=0):
        Car.__init__(self, position, speed, direction)
        self.scroller = scroller
        self.imageSource = pygame.image.load("../assets/png/playerCar.png")

    def accelerate(self, pixels=2):
        self.scroller.speed += pixels
        if self.scroller.speed > self.MAX_SPEED:
            self.scroller.speed = self.MAX_SPEED
        elif self.scroller.speed < -self.MAX_SPEED:
            self.scroller.speed = -self.MAX_SPEED

    def deltaX(self, rad):
        """Use the scroller's speed instead of its own"""
        return -self.scroller.speed * math.sin(rad)
    def deltaY(self, rad):
        """Keep the car in the same place on the screen"""
        return 0

class DummyCar(Car):
    """The cars that drive independently of the user"""
    def __init__(self, scroller, position, speed, direction):
        Car.__init__(self, position, speed, direction)
        self.scroller = scroller
        self.imageSource = pygame.image.load("../assets/png/playerCar.png")

    def deltaY(self, rad):
        """Move DummyCar instances relative to the background"""
        return -self.speed * math.cos(rad) + self.scroller.speed

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
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                car.startTurning(-5)
            elif event.key == K_LEFT:
                car.startTurning()
            elif event.key == K_UP:
                car.startAcceleration()
            elif event.key == K_DOWN:
                car.startAcceleration(-2)
            elif event.key == K_ESCAPE: sys.exit(0) # TODO: load the main menu
        else:
            if event.key == K_RIGHT or event.key == K_LEFT:
                car.stopTurning()
            elif event.key == K_UP or event.key == K_DOWN:
                car.stopAcceleration()

    # RENDERING
    SCREEN.fill((0,0,0))
    scroller.cars.update()
    scroller.cars.draw(SCREEN)
    carGroup.update()
    carGroup.draw(SCREEN)
    policeCarGroup.update()
    policeCarGroup.draw(SCREEN)
    pygame.display.flip()
