import pygame
from Button import Button
from EventLoop import EventLoop

class MainMenu(object):
    def __init__(self, SCREEN):
        # Load the image and set the size and position to overlay the screen
        image = pygame.image.load("../assets/png/mainMenu.png")
        # Create the play button and draw it onto the image
        playButton = Button((400, 100), (505, 400), "Play")
        image.blit(playButton.image, playButton.rect)
        # Find the image's position
        rect = image.get_rect()
        rect.topleft = (0, 0)
        # Draw the image on top of the screen
        SCREEN.blit(image, rect)
        # Output the first frame
        pygame.display.flip()
        # Create a new event loop
        loop = EventLoop()
        # Continue to the game if they click play
        playButton.onClick(loop.stop)
        # When a new frame needs to be rendered, update the button
        @loop.onUpdate
        def update():
            playButton.update()
            SCREEN.blit(playButton.image, playButton.rect)
        # Start animating
        loop.start()
