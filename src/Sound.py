import pygame
class Sound(object):
    #Set sound effects/music
    #backgroundMusic = pygame.mixer.Music('music.mp3')
    hornSound = pygame.mixer.Sound('horn.ogg')
    collideSound = pygame.mixer.Sound('collide.ogg')
    #Play the sound
    @classmethod
    def music(cls):
        cls.backgroundMusic.play(loops=-1)
    @classmethod
    def carHorn(cls):
        cls.hornSound.play(loops=0)
    @classmethod
    def obstacleSound(cls):
        cls.collideSound.play(loops=0)
