import sys
import pygame
from EventLoop import EventLoop
from Button import Button

def Lose(SCREEN, game):
    # Load the image and set the size and position to overlay the screen
    image = pygame.image.load("endScreen.png")
    rect = image.get_rect()
    rect.topleft = (0, 0)
    # Load and display the buttons
    newGameButton = Button((400, 100), (505, 425), "New Game")
    quitButton = Button((400, 100), (505, 545), "Quit")
    image.blit(newGameButton.image, newGameButton.rect)
    image.blit(quitButton.image, quitButton.rect)
    # Draw the image on top of the screen
    SCREEN.blit(image, rect)
    # Create an event loop
    loop = EventLoop()
    # Start a new game
    @newGameButton.onClick
    def newGame():
        game.loop.stop()
        loop.stop()
    # Exit the game
    @quitButton.onClick
    def quit():
        pygame.quit()
        sys.exit()
    # Update the screen
    pygame.display.flip()
    @loop.onUpdate
    # Check to see when the user has pressed a button
    def update():
        newGameButton.update()
        SCREEN.blit(newGameButton.image, newGameButton.rect)
        quitButton.update()
        SCREEN.blit(quitButton.image, quitButton.rect)
    loop.start()
