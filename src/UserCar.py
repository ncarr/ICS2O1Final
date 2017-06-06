import math
import pygame
from Car import Car

class UserCar(Car):
    """The car the user controls"""
    def __init__(self, scroller, game, position=(505, 450), speed=0, direction=0):
        super().__init__(position, speed, direction)
        self.scroller = scroller
        self.game = game
        self.imageSource = pygame.image.load("playerCar.png")
        self.image = self.imageSource
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.colliding = None

    def accelerate(self, pixels=2):
        """Perform normal acceleration but also update the speed the background is moving"""
        super().accelerate(pixels)
        radians = self.direction * math.pi / 180
        self.scroller.deltaY = super().deltaY(radians)
        self.game.distance -= self.scroller.deltaY
        if self.game.distance > self.game.maxDistance:
            self.game.maxDistance = self.game.distance

    def deltaX(self, rad):
        """Keep the car from falling off the screen"""
        # ((rad > 0) != (self.speed < 0)) makes sure that rad > 0 or self.speed < 0 is true, but not none or both
        if self.position[0] < 25 and ((rad > 0) != (self.speed < 0)) or self.position[0] > 995 and ((rad < 0) != (self.speed < 0)):
            return 0
        return super().deltaX(rad)
    def deltaY(self, rad):
        """Keep the car in the same place on the screen"""
        return 0

    def update(self):
        """Slowly decelerate the car over time"""
        self.speed *= 0.999
        radians = self.direction * math.pi / 180
        self.scroller.deltaY = super().deltaY(radians)
        # Also do normal car things
        super().update()
