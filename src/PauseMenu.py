import pygame
from Button import Button

def Pause(CLOCK, SCREEN):
    # Load the image and set the size and position to overlay the screen
    image = pygame.image.load("../assets/png/pause.png")
    rect = image.get_rect()
    rect.topleft = (0, 0)
    # Draw the image on top of the screen
    SCREEN.blit(image, rect)
    play = pygame.sprite.Group(Button((300, 50), (505, 400)))
    # Update the screen
    pygame.display.flip()
    while True:
        CLOCK.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # Check to see if the player has unpaused the game
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return True
            play.update()
            play.draw(SCREEN)
            pygame.display.flip()
