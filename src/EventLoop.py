import sys
import pygame

class EventLoop(object):
    def __init__(self):
        self.processing = True
        self.frames = 0
    def beforeEvents(self, beforeUpdator):
        """First function to be called every frame, even before event handling"""
        self.beforeUpdator = beforeUpdator
    def onEvent(self, event):
        """Function to be called for every event received"""
        self.eventProcessor = event
    def onUpdate(self, update):
        """Function to call every frame after events were handled"""
        self.updator = update
    def onStart(self, start):
        """Function to call when the loop is started"""
        self.startHook = start
    def onStop(self, stop):
        """Function to call when the loop is stopped"""
        self.stopHook = stop
    def beforeUpdator(self, frames=None):
        pass
    def eventProcessor(self, event, frames=None):
        pass
    def updator(self, frames=None):
        pass
    def startHook(self):
        pass
    def stopHook(self):
        pass
    def start(self):
        """Start a basic event loop with the supplied hooks"""
        self.startHook()
        CLOCK = pygame.time.Clock()
        self.processing = True
        while self.processing:
            # Limit the game to 60 fps
            CLOCK.tick(60)
            # Call the user-defined pre-event-processing hook
            self.beforeUpdator()
            # Iterate through all events
            for event in pygame.event.get():
                # If the user presses the close button, end the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Call the user-defined event processing hook
                self.eventProcessor(event)
            # Call the user-defined update hook
            self.updator()
            # Output the frame to the display
            pygame.display.flip()
    def startFrames(self):
        """Start an event loop which counts frames with the supplied hooks"""
        self.startHook()
        CLOCK = pygame.time.Clock()
        self.processing = True
        while self.processing:
            # Limit the game to 60 fps
            CLOCK.tick(60)
            # Call the user-defined pre-event-processing hook
            self.beforeUpdator(self.frames)
            # Iterate through all events
            for event in pygame.event.get():
                # If the user presses the close button, end the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Call the user-defined event processing hook
                self.eventProcessor(event, self.frames)
            # Call the user-defined update hook
            self.updator(self.frames)
            # Output the frame to the display
            pygame.display.flip()
            self.frames += 1
    def stop(self):
        self.stopHook()
        self.processing = False
