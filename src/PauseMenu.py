import pygame
from Button import Button
from EventLoop import EventLoop

def Pause(SCREEN):
    # Load the image and set the size and position to overlay the screen
    image = pygame.image.load("../assets/png/pause.png")
    playButton = Button((400, 100), (505, 400), "Resume")
    image.blit(playButton.image, playButton.rect)
    rect = image.get_rect()
    rect.topleft = (0, 0)
    # Draw the image on top of the screen
    SCREEN.blit(image, rect)
    # Create an event loop
    loop = EventLoop()
    # Stop the loop and continue the game if resume is clicked
    playButton.onClick(loop.stop)
    # Update the screen
    pygame.display.flip()
    @loop.onEvent
    def event(event):
        # Check to see if the player has unpaused the game
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            loop.stop()
    @loop.onUpdate
    def update():
        playButton.update()
        SCREEN.blit(playButton.image, playButton.rect)
    loop.start()
