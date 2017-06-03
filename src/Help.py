import pygame
from Button import Button
from EventLoop import EventLoop

class Help(object):
    def __init__(self, SCREEN):
        # Load the image and set the size and position
        image = pygame.image.load("help.png")
        rect = image.get_rect()
        rect.topleft = (0, 0)
        # Create the back button and draw it onto the image
        backButton = Button((400, 100), (505, 590), "Back")
        # Draw the image on top of the screen
        SCREEN.blit(image, rect)
        # Output the first frame
        pygame.display.flip()
        # Create a new event loop
        loop = EventLoop()
        # Go back
        backButton.onClick(loop.stop)
        # When a new frame needs to be rendered, update the button
        @loop.onUpdate
        def update():
            backButton.update()
            SCREEN.blit(backButton.image, backButton.rect)
        # Start animating
        loop.start()
