import math
import pygame

class Car(pygame.sprite.Sprite):
    """All cars inherit this class"""
    MAX_SPEED = 15
    def __init__(self, position, speed, direction):
        """Constructor to be called when a new Car object is created"""
        # Call pygame's sprite constructor
        super().__init__()
        # Set all default properties
        self.position = position
        self.speed = speed
        self.direction = direction
        self.speedIncrease = 0
        self.turnDirection = 0

    def startTurning(self, degrees=0.18):
        """Start turning 'degrees' degrees counterclockwise every frame until stopTurning is called"""
        self.turnDirection = degrees
    def stopTurning(self):
        self.turnDirection = 0
    def turn(self, degrees=5):
        self.direction += degrees
        # If you are facing left, make sure you are rotated between 0 and 180 degrees
        if self.direction // 180 % 2 == 0:
            self.direction %= 360
        # If you are facing right, make sure you are rotated between 0 and -180 degrees
        else:
            self.direction = self.direction % 360 - 360
    def startAcceleration(self, pixels=2):
        """Start accelerating 'pixels' pixels every frame until stopAcceleration is called"""
        self.speedIncrease = pixels
    def stopAcceleration(self):
        self.speedIncrease = 0
    def accelerate(self, pixels=2):
        self.speed += pixels
        if self.speed > self.MAX_SPEED:
            self.speed = self.MAX_SPEED
        elif self.speed < -self.MAX_SPEED:
            self.speed = -self.MAX_SPEED
    def deltaX(self, rad):
        """Use magic to determine the horizontal distance travelled per frame using speed and direction"""
        return -self.speed * math.sin(rad)
    def deltaY(self, rad):
        """Mathematically determine the vertical distance travelled per frame using speed and direction"""
        return -self.speed * math.cos(rad)
    def update(self):
        """Determine how to transform the image every frame"""
        # If the start* functions were called, it would accelerate or rotate by that amount every frame, otherwise it would use 0
        self.turn(self.turnDirection * self.speed)
        self.accelerate(self.speedIncrease)
        # Calculate the new position of the car
        x, y = self.position
        rad = self.direction * math.pi / 180
        x += self.deltaX(rad)
        y += self.deltaY(rad)
        self.position = (x, y)
        # Rotate it to its new angle
        self.image = pygame.transform.rotate(self.imageSource, self.direction)
        # Set its mask to its newly rotated image, we use it for collision detection
        self.mask = pygame.mask.from_surface(self.image)
        # Pygame uses self.rect to determine where to draw the sprite
        self.rect = self.image.get_rect()
        self.rect.center = self.position
