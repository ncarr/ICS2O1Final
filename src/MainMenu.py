import sys
import pygame
from Button import Button
from EventLoop import EventLoop
from Help import Help
from BackgroundScroller import BackgroundScroller
from DummyCar import DummyCar
from Obstacle import GenerateCar

class MainMenu(object):
    def __init__(self, SCREEN):
        self.SCREEN = SCREEN
        # Create animation-related objects
        self.maxDistance = 0
        self.obstacle = GenerateCar(self, 2, 600, 601)
        # Create all sprites and group them
        self.scroller = scroller = BackgroundScroller()
        scroller.deltaY = -3
        # Load the image and set the size and position to overlay the screen
        self.image = pygame.image.load("mainMenu.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        # Create the play button and draw it onto the image
        self.playButton = Button((400, 100), (505, 355), "Play")
        self.helpButton = Button((400, 100), (505, 475), "Help")
        self.quitButton = Button((400, 100), (505, 590), "Quit")

        # Load the high score
        with open("highScore.txt") as f:
            self.highScore = f.read()
        font = pygame.font.SysFont('Segoe UI', 24, True, False)
        self.text = font.render("High score: " + self.highScore, True, (255, 255, 255))
        self.textRect = self.text.get_rect()
        self.textRect.center = (505, 275)

        self.drawFirstFrame()
        # Create a new event loop
        loop = EventLoop()
        # Continue to the game if they click play
        self.playButton.onClick(loop.stop)
        # Exit the game
        @self.quitButton.onClick
        def quit():
            pygame.quit()
            sys.exit()
        # Help screen
        @self.helpButton.onClick
        def help():
            Help(SCREEN)
            self.drawFirstFrame()

        # When a new frame needs to be rendered, update the button
        @loop.onUpdate
        def update():
            self.maxDistance += 3
            # Render the frame
            SCREEN.fill((76,175,80))
            scroller.background.update()
            scroller.background.draw(SCREEN)
            scroller.cars.update()
            scroller.cars.draw(SCREEN)
            self.obstacle.update()
            SCREEN.blit(self.image, self.rect)
            # Update buttons
            self.playButton.update()
            SCREEN.blit(self.playButton.image, self.playButton.rect)
            self.helpButton.update()
            SCREEN.blit(self.helpButton.image, self.helpButton.rect)
            self.quitButton.update()
            SCREEN.blit(self.quitButton.image, self.quitButton.rect)
        # Start animating
        loop.start()

    def drawFirstFrame(self):
        self.SCREEN.fill((76,175,80))
        self.scroller.background.update()
        self.scroller.background.draw(self.SCREEN)
        self.scroller.cars.update()
        self.scroller.cars.draw(self.SCREEN)
        self.obstacle.update()
        self.image.blit(self.playButton.image, self.playButton.rect)
        self.image.blit(self.helpButton.image, self.helpButton.rect)
        self.image.blit(self.quitButton.image, self.quitButton.rect)
        # Write the high score to the screen
        self.image.blit(self.text, self.textRect)
        # Draw the image on top of the screen
        self.SCREEN.blit(self.image, self.rect)
        # Output the first frame
        pygame.display.flip()
