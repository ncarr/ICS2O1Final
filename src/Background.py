import pygame

class Background(pygame.sprite.Sprite):
    """The tiled, scrolling background"""
    ROAD_SURFACE = pygame.image.load("../assets/png/road.png")
    def __init__(self, scroller, top, above=None, below=None):
        super().__init__()
        self.scroller = scroller
        self.image = self.__class__.ROAD_SURFACE
        self.rect = self.image.get_rect()
        self.rect.midtop = (505, top)
        self.above = above
        self.below = below
    def update(self):
        """Push each background down at the speed of the car every frame"""
        self.rect.top -= self.scroller.deltaY
        # If the tile is off screen
        if not -self.rect.height <= self.rect.top <= 695:
            # Announce to its neighbours that it doesn't exist
            if self.above:
                self.above.below = None
            if self.below:
                self.below.above = None
            # Remove itself from all groups
            self.kill()
        # If there is empty space below, fill it
        elif self.rect.top < 0 and not self.below:
            self.below = self.__class__(self.scroller, self.rect.top + self.rect.height, self)
            self.scroller.background.add(self.below)
        # If there is empty space above, fill it
        elif self.rect.top > 0 and not self.above:
            self.above = self.__class__(self.scroller, self.rect.top - self.rect.height, None, self)
            self.scroller.background.add(self.above)
