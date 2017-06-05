from random import choice, randint
class Obstacle(object):
    # Positions of centers of lanes
    lanes = [298, 436, 574, 712]
    def __init__(self, game):
        self.game = game
        self.createObject()
    def drawObject(self):
        x = choice(self.__class__.lanes)
        speed = 10
        # Determine which lanes the cars are in
        if x > 505:
            direction = 0
        else:
            direction = 180
        # Draw the car
        self.game.scroller.addDummyCar((x,-150), speed, direction)
    # Determine when the object should appear
    def createObject(self):
        self.objectDistance = self.game.maxDistance + randint(2000,4000)
    # Draw the object
    def update(self):
        if self.game.maxDistance >= self.objectDistance:
            self.drawObject()
            self.createObject()
