"""Turbulent Tailing
A car chase game where you avoid obstacles and try not to get captured
Nicholas Carr and Victor Lin
2017-05-25
"""
# Import required modules
import pygame
import math
from pygame.locals import *
from MainMenu import MainMenu
#import game

pygame.init()
# Open a new 1010x695 window with the game's name and icon
SCREEN = pygame.display.set_mode((1010, 695))
pygame.display.set_caption("Turbulent Tailing")
pygame.display.set_icon(pygame.image.load("../design/icon.png"))
MainMenu(SCREEN)
# Set up the timer to limit the game to 60 fps
CLOCK = pygame.time.Clock()

# Main event loop
while True:
    # Limit the game to 60 fps
    CLOCK.tick(60)
    # Iterate through all events
    for event in pygame.event.get():
        # If the user presses the close button, end the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.flip()
