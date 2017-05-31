import pygame
from Button import Button

class MainMenu(object):
    play = False
    def __init__(self, SCREEN):
        # Load the image and set the size and position to overlay the screen
        CLOCK = pygame.time.Clock()
        image = pygame.image.load("../assets/png/mainMenu.png")
        rect = image.get_rect()
        rect.topleft = (0, 0)
        # Draw the image on top of the screen
        SCREEN.blit(image, rect)
        playButton = Button((400, 100), (505, 400), "Play")

        # Update the screen
        pygame.display.flip()
        while True:
            CLOCK.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            playButton.update()
            SCREEN.blit(playButton.image,playButton.rect)
            pygame.display.flip()
            if self.__class__.play:
                return True
        @playButton.onClick
        def play():
            self.__class__.play = True
