import pygame
from DummyCar import DummyCar
from Background import Background
from Obstacle import TrafficCone

class BackgroundScroller(object):
    """Scrolls the background at the speed the car is going"""
    def __init__(self, speed=2):
        # Set default properties, create empty sprite groups
        self.cars = pygame.sprite.Group()
        self.trafficCones = pygame.sprite.Group()
        self.background = pygame.sprite.Group(Background(self, 0))
        # This is the property that tells other objects how quickly the background is moving
        self.deltaY = 0

    def addDummyCar(self, coordinates, speed, direction):
        """Create a DummyCar and add it to the cars group"""
        dummyCar = DummyCar(self, coordinates, speed, direction)
        self.cars.add(dummyCar)
        return dummyCar

    def addTrafficCone(self, centre):
        """Create a TrafficCone and add it to the trafficCones group"""
        trafficCone = TrafficCone(self, centre)
        self.trafficCones.add(trafficCone)
        return trafficCone
