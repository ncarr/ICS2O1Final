import pygame
class Sound(object):
    def __init__(self):
        self.backgroundMusic = pygame.mixer.Sound('music.mp3')
        self.hornSound = pygame.mixer.Sound('horn.mp3')
        self.obstacleSound = pygame.mixer.Sound('collide.mp3')
    def Music(self):
        self.backgroundMusic.play(loops=-1)
    def Collide(self, type):
        if collideType == 'car':
            self.hornSound.play(loops=0)
        elif collideType == 'object':
            self.obstacleSound.play(loops=0)
