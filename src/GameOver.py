import pygame
from EventLoop import EventLoop

def Lose(SCREEN):
    # Load the image and set the size and position to overlay the screen
    image = pygame.image.load("../assets/png/endScreen.png")
    rect = image.get_rect()
    rect.topleft = (0, 0)
    # Draw the image on top of the screen
    SCREEN.blit(image, rect)
    # Update the screen
    pygame.display.flip()
    # Start a basic event loop and don't bother saving it to a varible
    EventLoop().start()
