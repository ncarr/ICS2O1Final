from random import choice, randint
import pygame
class Obstacle(object):
    """Generate obstacles randomly"""
    # Positions of centers of lanes
    lanes = [298, 436, 574, 712]
    def __init__(self, game, lowerLimit=2000, upperLimit=4000):
        # Set default properites
        self.game = game
        self.lowerLimit = lowerLimit
        self.upperLimit = upperLimit
        # Start randomly generating objects
        self.createObject()
    def drawObject(self):
        """Randomly choose a lane and call the function to draw an obstacle"""
        x = choice(self.__class__.lanes)
        self.newObstacle((x,-150))
    def createObject(self):
        """Determine when the object should appear"""
        self.objectDistance = self.game.maxDistance + randint(self.lowerLimit, self.upperLimit)
    def update(self):
        """Draw the object"""
        if self.game.maxDistance >= self.objectDistance:
            self.drawObject()
            self.createObject()
class GenerateCar(Obstacle):
    def __init__(self, game, speed=10, lowerLimit=2000, upperLimit=4000):
        self.speed = speed
        super().__init__(game, lowerLimit, upperLimit)
    def newObstacle(self, position):
        x, y = position
        # Determine which lanes the cars are in
        if x > 505:
            direction = 0
        else:
            direction = 180
        # Draw the car
        self.game.scroller.addDummyCar(position, self.speed, direction)
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
# This inherits most properties from the Obstacle class defined above
class GenerateCone(Obstacle):
    def newObstacle(self, position):
        self.game.scroller.addTrafficCone(position)
