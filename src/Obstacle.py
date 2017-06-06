from random import choice, randint
import pygame
class Obstacle(object):
    # Positions of centers of lanes
    lanes = [298, 436, 574, 712]
    def __init__(self, game):
        self.game = game
        self.createObject()
    def drawObject(self):
        x = choice(self.__class__.lanes)
        self.newObstacle((x,-150))
    # Determine when the object should appear
    def createObject(self):
        self.objectDistance = self.game.maxDistance + randint(2000,4000)
    # Draw the object
    def update(self):
        if self.game.maxDistance >= self.objectDistance:
            self.drawObject()
            self.createObject()
class GenerateCar(Obstacle):
    def newObstacle(self, position):
        speed = 10
        x, y = position
        # Determine which lanes the cars are in
        if x > 505:
            direction = 0
        else:
            direction = 180
        # Draw the car
        self.game.scroller.addDummyCar(position, speed, direction)
class TrafficCone(pygame.sprite.Sprite):
    def __init__(self, scroller, centre):
        super().__init__()
        self.scroller = scroller
        self.image = pygame.image.load('trafficCone.png')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = centre
    def update(self):
        x, y = self.rect.center
        # If the cone is past the farthest distance we let the user reverse to, free its memory
        if y > 1440:
            return self.kill()
        y -= self.scroller.deltaY
        self.rect.center = (x, y)
class GenerateCone(Obstacle):
    def newObstacle(self, position):
        self.game.scroller.addTrafficCone(position)
