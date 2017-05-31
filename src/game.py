"""Turbulent Tailing
A car chase game where you avoid obstacles and try not to get captured
Nicholas Carr and Victor Lin
2017-05-25
"""
# Import required modules
import pygame
import math
from pygame.locals import *
from BackgroundScroller import BackgroundScroller
from Car import Car
from UserCar import UserCar
from DummyCar import DummyCar
from PoliceCar import PoliceCar
from PauseMenu import Pause
from GameOver import Lose

pygame.init()
# Open a new 1010x695 window with the game's name and icon
SCREEN = pygame.display.set_mode((1010, 695))
pygame.display.set_caption("Turbulent Tailing")
pygame.display.set_icon(pygame.image.load("../design/icon.png"))
# Set up the timer to limit the game to 60 fps
CLOCK = pygame.time.Clock()
# Create all sprites and group them
scroller = BackgroundScroller()
scroller.addDummyCar((512, 200), 10, 0)
car = UserCar(scroller)
carGroup = pygame.sprite.GroupSingle(car)
policeCar = PoliceCar()
policeCarGroup = pygame.sprite.GroupSingle(policeCar)
# Main event loop
while True:
    # Limit the game to 60 fps
    CLOCK.tick(60)
    # Iterate through all events
    for event in pygame.event.get():
        # If the user presses the close button, end the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # Do nothing else if the event was not a keypress
        if not hasattr(event, 'key'): continue
        # If you pressed a key
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                car.startTurning(-5)
            elif event.key == K_LEFT:
                car.startTurning()
            elif event.key == K_UP:
                car.startAcceleration()
            elif event.key == K_DOWN:
                car.startAcceleration(-2)
            elif event.key == K_ESCAPE:
                Pause(CLOCK, SCREEN)
            elif event.key == K_l:
                Lose(CLOCK, SCREEN)

        # If you lifted your finger off the key
        else:
            if event.key == K_RIGHT or event.key == K_LEFT:
                car.stopTurning()
            elif event.key == K_UP or event.key == K_DOWN:
                car.stopAcceleration()

    # Render the frame
    SCREEN.fill((76,175,80))
    scroller.background.update()
    scroller.background.draw(SCREEN)
    scroller.cars.update()
    scroller.cars.draw(SCREEN)
    carGroup.update()
    carGroup.draw(SCREEN)
    policeCarGroup.update()
    policeCarGroup.draw(SCREEN)
    carCollide = pygame.sprite.spritecollide(car, scroller.cars, False)
    # Collision
    for sprite in carCollide:
        sprite.speed = 0
        car.speed = 0
        car.stopTurning()
        scroller.deltaY = 0

    pygame.display.flip()
