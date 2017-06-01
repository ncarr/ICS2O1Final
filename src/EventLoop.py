import pygame

class EventLoop(object):
    def __init__(self):
        self.processing = True
    def onEvent(self, event):
        self.eventProcessor = event
    def onUpdate(self, update):
        self.updator = update
    def eventProcessor(self, event):
        pass
    def updator(self):
        pass
    def start(self):
        """Start a basic event loop with the supplied hooks"""
        CLOCK = pygame.time.Clock()
        while self.processing:
            # Limit the game to 60 fps
            CLOCK.tick(60)
            # Iterate through all events
            for event in pygame.event.get():
                # If the user presses the close button, end the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                # Call the user-defined event processing hook
                self.eventProcessor(event)
            # Call the user-defined update hook
            self.updator()
            # Output the frame to the display
            pygame.display.flip()
    def stop(self):
        self.processing = False
