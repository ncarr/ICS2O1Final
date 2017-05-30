import pygame

def Lose(CLOCK, SCREEN):
    # Load the image and set the size and position to overlay the screen
    image = pygame.image.load("../assets/png/endScreen.png")
    rect = image.get_rect()
    rect.topleft = (0, 0)
    # Draw the image on top of the screen
    SCREEN.blit(image, rect)
    # Update the screen
    pygame.display.flip()
    while True:
        CLOCK.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
