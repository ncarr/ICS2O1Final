import pygame

class Background(pygame.sprite.Sprite):
    """The tiled, scrolling background"""
    def __init__(self, scroller, top):
        super().__init__()
        self.scroller = scroller
        self.image = pygame.image.load("../assets/png/road.png")
        self.rect = self.image.get_rect()
        self.rect.center = (550, top)
        self.top = top
    def update(self):
        """Push each background down at the speed of the car every frame"""
        # Calculate the new position of the background
        self.top -= self.scroller.deltaY
        if not -695 <= self.top <= 695:
            if self.scroller.deltaY > 0:
                self.top = 695
            else:
                self.top = -695
        # Pygame uses self.rect to determine where to draw the sprite
        self.rect.top = self.top
