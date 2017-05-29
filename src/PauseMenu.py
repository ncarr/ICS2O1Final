import pygame

#class Pause(object):
def Pause(CLOCK, SCREEN):
    image = pygame.image.load("../assets/png/pause.png")
    rect = image.get_rect()
    rect.topleft = (0, 0)
    SCREEN.blit(image, rect)
    pygame.display.flip()
    while True:
        CLOCK.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return True
