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
    def startAcceleration(self, pixels=2):
        if self.colliding:
            radians = self.direction * math.pi / 180
            # Find the current distance squared between the centres
            currentDistance = abs(self.rect.centerx + self.colliding[0].rect.centerx) ** 2 + abs(self.rect.centery + self.colliding[0].rect.centery) ** 2
            # Find the distance squared between the centres after moving in the direction of acceleration
            distanceAfterAccelerating = abs(self.rect.centerx - pixels * math.sin(radians) + self.colliding[0].rect.centerx) ** 2 + abs(self.rect.centery - pixels * math.cos(radians) + self.colliding[0].rect.centery) ** 2
            # If it would move you toward the object you are already crashing into
            if distanceAfterAccelerating < currentDistance:
                # Stop you from accelerating
                return False
        super().startAcceleration(pixels)

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
        """Slowly decelerate the car over time and slow it on the grass"""
        self.speed *= 0.999
        radians = self.direction * math.pi / 180
        self.scroller.deltaY = super().deltaY(radians)
        x, y = self.position
        if x < 229 or x > 781:
            self.MAX_SPEED = 5
        else:
            self.MAX_SPEED = super().MAX_SPEED
        # Also do normal car things
        super().update()
