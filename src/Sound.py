import pygame
class Sound(object):
    def __init__(self):
        #self.backgroundMusic = pygame.mixer.Music('music.mp3')
        self.hornSound = pygame.mixer.Sound('horn.wav')
        #self.obstacleSound = pygame.mixer.Sound('collide.wav')
    def music(self):
        self.backgroundMusic.play(loops=-1)
    def carHorn(self):
        self.hornSound.play(loops=0)
        print ('hron')
    def obstacleSound(self):
        self.obstacleSound.play(loops=0)
