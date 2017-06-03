import sys
import pygame
from Button import Button
from EventLoop import EventLoop
from Help import Help

class MainMenu(object):
    def __init__(self, SCREEN):
        self.SCREEN = SCREEN
        # Load the image and set the size and position to overlay the screen
        self.image = pygame.image.load("mainMenu.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        # Create the play button and draw it onto the image
        self.playButton = Button((400, 100), (505, 355), "Play")
        self.helpButton = Button((400, 100), (505, 475), "Help")
        self.quitButton = Button((400, 100), (505, 590), "Quit")

        self.drawFirstFrame()
        # Create a new event loop
        loop = EventLoop()
        # Continue to the game if they click play
        self.playButton.onClick(loop.stop)
        # Exit the game
        @self.quitButton.onClick
        def quit():
            pygame.quit()
            sys.exit()
        # Help screen
        @self.helpButton.onClick
        def help():
            Help(SCREEN)
            self.drawFirstFrame()

        # When a new frame needs to be rendered, update the button
        @loop.onUpdate
        def update():
            self.playButton.update()
            SCREEN.blit(self.playButton.image, self.playButton.rect)
            self.helpButton.update()
            SCREEN.blit(self.helpButton.image, self.helpButton.rect)
            self.quitButton.update()
            SCREEN.blit(self.quitButton.image, self.quitButton.rect)
        # Start animating
        loop.start()

    def drawFirstFrame(self):
        self.image.blit(self.playButton.image, self.playButton.rect)
        self.image.blit(self.helpButton.image, self.helpButton.rect)
        self.image.blit(self.quitButton.image, self.quitButton.rect)
        # Draw the image on top of the screen
        self.SCREEN.blit(self.image, self.rect)
        # Output the first frame
        pygame.display.flip()
