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
        # Create all sprites and group them
        scroller = BackgroundScroller()
        scroller.addDummyCar((512, 200), 10, 0)
        car = UserCar(scroller)
        carGroup = pygame.sprite.GroupSingle(car)
        policeCar = PoliceCar()
        policeCarGroup = pygame.sprite.GroupSingle(policeCar)

        self.loop = loop = EventLoop()
        @loop.onEvent
        def event(event):
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
        def update():
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
        loop.start()
