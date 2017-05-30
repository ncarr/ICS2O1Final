import pygame

class Button(pygame.sprite.Sprite):
    """Buttons on menus"""
    def __init__(self, size, centre):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = centre
        self.hover = False

    def update(self):
        x, y = pygame.mouse.get_pos()
        if self.rect.left < x < self.rect.right and self.rect.top < y < self.rect.bottom:
            self.hover = True
            self.image.fill((127, 127, 127))
        elif self.hover:
            self.hover = False
            self.image.fill((255, 255, 255))
