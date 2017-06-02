import pygame
from Button import Button
from EventLoop import EventLoop
from Help import Help

class MainMenu(object):
    def __init__(self, SCREEN):
        # Load the image and set the size and position to overlay the screen
        image = pygame.image.load("../assets/png/mainMenu.png")
        rect = image.get_rect()
        rect.topleft = (0, 0)
        # Create the play button and draw it onto the image
        playButton = Button((400, 100), (505, 355), "Play")
        helpButton = Button((400, 100), (505, 475), "Help")
        quitButton = Button((400, 100), (505, 590), "Quit")
        image.blit(playButton.image, playButton.rect)
        image.blit(helpButton.image, helpButton.rect)
        image.blit(quitButton.image, quitButton.rect)
        # Draw the image on top of the screen
        SCREEN.blit(image, rect)
        # Output the first frame
        pygame.display.flip()
        # Create a new event loop
        loop = EventLoop()
        # Continue to the game if they click play
        playButton.onClick(loop.stop)
        # Exit the game
        @quitButton.onClick
        def quit():
            pygame.quit()
            exit()
        # Help screen
        @helpButton.onClick
        def help():
            Help(SCREEN)
            print ('literally anything')
        # When a new frame needs to be rendered, update the button
        @loop.onUpdate
        def update():
            playButton.update()
            SCREEN.blit(playButton.image, playButton.rect)
            helpButton.update()
            SCREEN.blit(helpButton.image, helpButton.rect)
            quitButton.update()
            SCREEN.blit(quitButton.image, quitButton.rect)
        # Start animating
        loop.start()
