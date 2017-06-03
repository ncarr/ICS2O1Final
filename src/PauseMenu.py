import sys
import pygame
from Button import Button
from EventLoop import EventLoop


def Pause(SCREEN, game):
    # Load the image and set the size and position to overlay the screen
    image = pygame.image.load("pause.png")
    rect = image.get_rect()
    rect.topleft = (0, 0)
    # Load and display the buttons
    playButton = Button((400, 100), (505, 305), "Resume")
    newGameButton = Button((400, 100), (505, 425), "New Game")
    quitButton = Button((400, 100), (505, 545), "Quit")
    image.blit(playButton.image, playButton.rect)
    image.blit(newGameButton.image, newGameButton.rect)
    image.blit(quitButton.image, quitButton.rect)
    # Draw the image on top of the screen
    SCREEN.blit(image, rect)
    # Create an event loop
    loop = EventLoop()

    # Make the buttons do their functions
    # Stop the loop and continue the game if resume is clicked
    playButton.onClick(loop.stop)
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
    @loop.onEvent
    def event(event):
        # Check to see if the player has unpaused the game
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            loop.stop()
    @loop.onUpdate
    # Check to see when the user has pressed a button
    def update():
        playButton.update()
        SCREEN.blit(playButton.image, playButton.rect)
        newGameButton.update()
        SCREEN.blit(newGameButton.image, newGameButton.rect)
        quitButton.update()
        SCREEN.blit(quitButton.image, quitButton.rect)
    loop.start()
