"""Turbulent Tailing
A car chase game where you avoid obstacles and try not to get captured
Nicholas Carr and Victor Lin
2017-05-25
"""
# Import required modules
import pygame
from pygame.locals import *
from BackgroundScroller import BackgroundScroller
from EventLoop import EventLoop
from Car import Car
from UserCar import UserCar
from DummyCar import DummyCar
from PoliceCar import PoliceCar
from PauseMenu import Pause
from GameOver import Lose

class Game(object):
    def __init__(self, SCREEN):
        self.__class__.countDown(SCREEN)
        self.distance = 0
        self.maxDistance = 0
        # Create all sprites and group them
        scroller = BackgroundScroller()
        scroller.addDummyCar((512, 200), 10, 0)
        car = UserCar(scroller, self)
        carGroup = pygame.sprite.GroupSingle(car)
        policeCar = PoliceCar()
        policeCarGroup = pygame.sprite.GroupSingle(policeCar)

        self.loop = loop = EventLoop()
        @loop.onEvent
        def event(event, frames):
            # Do nothing else if the event was not a keypress
            if not hasattr(event, 'key'): return True
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
                    Pause(SCREEN, self)
                elif event.key == K_l:
                    Lose(SCREEN, self)

            # If you lifted your finger off the key
            else:
                if event.key == K_RIGHT or event.key == K_LEFT:
                    car.stopTurning()
                elif event.key == K_UP or event.key == K_DOWN:
                    car.stopAcceleration()
        @loop.onUpdate
        def update(frames):
            # Stop the user if they have gone too far in reverse
            if self.maxDistance - 695 > self.distance and scroller.deltaY > 0:
                car.stopAcceleration()
                car.speed = 0
                scroller.deltaY = 0
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
        loop.startFrames()

    @staticmethod
    def countDown(SCREEN):
        # Create an event loop
        loop = EventLoop()
        # Define the font
        font = pygame.font.SysFont('Segoe UI', 72, False, False)
        # On every frame
        @loop.onUpdate
        def frame(frames):
            # Check to see if 1 second has passed
            if frames % 60 == 0:
                # Black out the screen and render the number of seconds left
                SCREEN.fill((0, 0, 0))
                stamp = font.render(str(3 - frames // 60), True, (149, 152, 154))
                SCREEN.blit(stamp, [505, 347])
            # Stop the countdown just before 0
            if frames >= 179:
                loop.stop()
        # Start the loop, but give the number of frames passed to the update function
        loop.startFrames()
