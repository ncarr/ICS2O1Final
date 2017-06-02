import pygame

class Button(pygame.sprite.Sprite):
    """Buttons on menus"""
    def __init__(self, size, centre, text):
        # Call the sprite constructor
        super().__init__()
        # Create a new white surface
        self.image = pygame.Surface(size)
        self.image.fill((255, 255, 255))
        # Create a new font and draw it to the surface
        font = pygame.font.SysFont('Segoe UI', 40, False, False)
        self.stamp = font.render(text, True, (149, 152, 154))
        self.image.blit(self.stamp, [25, 25])
        # Decide where it should go on screen
        self.rect = self.image.get_rect()
        self.rect.center = centre
        self.hovering = False
        self.clicking = False

    def update(self):
        # Get the x and y coordinates of the mouse
        x, y = pygame.mouse.get_pos()
        # If you are hovering inside the button
        if self.rect.left < x < self.rect.right and self.rect.top < y < self.rect.bottom:
            # If you just started hovering this frame
            if not self.hovering:
                # Change the colour of the button
                self.hovering = True
                self.image.fill((127, 127, 127))
                self.image.blit(self.stamp, [25, 25])
                self.hover()
            # If the user is clicking
            if pygame.mouse.get_pressed()[0] == 1:
                # If you just started clicking this frame
                if not self.clicking:
                    self.clicking = True
                    self.image.fill((100, 100, 100))
                    self.image.blit(self.stamp, [25, 25])
            # If you just stopped clicking
            elif self.clicking:
                self.clicking = False
                self.image.fill((127, 127, 127))
                self.image.blit(self.stamp, [25, 25])
                self.click()
        # If you just stopped hovering
        elif self.hovering:
            self.hovering = False
            self.image.fill((255, 255, 255))
            self.image.blit(self.stamp, [25, 25])
            self.endHover()

    def hover(self):
        """Default hover callback, gets replaced by self.onHover()"""
        pass
    def onHover(self, hover):
        """Set the hover callback"""
        self.hover = hover
    def endHover(self):
        """Default end hover callback, gets replaced by self.onEndHover()"""
        pass
    def onEndHover(self, endHover):
        """Set the end hover callback"""
        self.endHover = endHover
    def click(self):
        """Default click callback, gets replaced by self.onClick()"""
        pass
    def onClick(self, click):
        """Set the click callback"""
        self.click = click
