from random import choice, randint
class Obstacle(object):
    lanes = [298, 436, 574, 712]
    def __init__(self, game):
        self.game = game
        self.createObject()
    def drawObject(self):
        x = choice(self.__class__.lanes)
        speed = 10
        if x > 505:
            direction = 0
        else:
            direction = 180
        self.game.scroller.addDummyCar((x,-150), speed, direction)
    def createObject(self):
        self.objectDistance = self.game.maxDistance + randint(2000,4000)
    def update(self):
        if self.game.maxDistance >= self.objectDistance:
            self.drawObject()
            self.createObject()
