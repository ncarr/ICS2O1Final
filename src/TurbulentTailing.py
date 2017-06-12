"""Turbulent Tailing
A car chase game where you avoid obstacles and try not to get captured
Nicholas Carr and Victor Lin
2017-05-25
"""
# Import required modules
import pygame
from pygame.locals import *
pygame.init()
from MainMenu import MainMenu
from game import Game

# Open a new 1010x695 window with the game's name and icon
SCREEN = pygame.display.set_mode((1010, 695))
pygame.display.set_caption("Turbulent Tailing")
pygame.display.set_icon(pygame.image.load("icon.png"))
MainMenu(SCREEN)
while True:
    Game(SCREEN)
