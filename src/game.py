"""Turbulent Tailing
A car chase game where you avoid obstacles and try not to get captured
Nicholas Carr and Victor Lin
2017-05-25
"""
# Import pygame
import pygame
from pygame.locals import *
# Import the other files in the folder
from BackgroundScroller import BackgroundScroller
from EventLoop import EventLoop
from Car import Car
from UserCar import UserCar
from DummyCar import DummyCar
from PoliceCar import PoliceCar
from PauseMenu import Pause
from GameOver import Lose
from Obstacle import GenerateCar, GenerateCone
from Sound import Sound

class Game(object):
    def __init__(self, SCREEN):
        # Count down
        self.__class__.countDown(SCREEN)
        # Set default attributes
        self.distance = 0
        self.maxDistance = 0
        self.bonusPoints = 0
        # Set up obstacle generators
        self.obstacle = GenerateCar(self)
        self.trafficCone = GenerateCone(self)
        # Create all initial sprites and group them
        self.scroller = scroller = BackgroundScroller()
        policeCar = PoliceCar(scroller)
        car = UserCar(scroller, policeCar, self)
        carGroup = pygame.sprite.GroupSingle(car)
        policeCarGroup = pygame.sprite.GroupSingle(policeCar)

        # Create the event loop
        self.loop = loop = EventLoop()
        @loop.onEvent
        def event(event, frames):
            # Do nothing else if the event was not a keypress
            if not hasattr(event, 'key'): return True
            # If you pressed a key
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    car.startTurning(-0.18)
                elif event.key == K_LEFT:
                    car.startTurning()
                elif event.key == K_UP:
                    car.startAcceleration()
                elif event.key == K_DOWN:
                    car.startAcceleration(-2)
                elif event.key == K_ESCAPE:
                    Pause(SCREEN, self)

            # If you lifted your finger off the key
            else:
                if event.key == K_RIGHT or event.key == K_LEFT:
                    car.stopTurning()
                elif event.key == K_UP or event.key == K_DOWN:
                    car.stopAcceleration()
        @loop.beforeEvents
        def checkCollision(frames):
            # Detect collision with other cars
            carCollide = pygame.sprite.spritecollide(car, scroller.cars, False, pygame.sprite.collide_mask)
            # Stop other cars when they hit us
            for sprite in carCollide:
                sprite.speed = 0
            # Detect collision with traffic cones
            coneCollide = pygame.sprite.spritecollide(car, scroller.trafficCones, False, pygame.sprite.collide_mask)
            # Stopping the car when it hits another car
            if carCollide:
                if not car.colliding:
                    car.colliding = carCollide
                    Sound.carHorn()
                    car.speed = 0
                    car.stopTurning()
                    car.stopAcceleration()
                    scroller.deltaY = 0
            # Slowing the car when it hits traffic cones
            elif coneCollide:
                if not car.colliding:
                    car.colliding = coneCollide
                    Sound.obstacleSound()
                    car.speed = car.speed * 0.3
                    #car.stopTurning()
                    #car.stopAcceleration()
                    scroller.deltaY = 0
            else:
                car.colliding = None
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
            scroller.trafficCones.update()
            scroller.trafficCones.draw(SCREEN)
            scroller.cars.update()
            scroller.cars.draw(SCREEN)
            carGroup.update()
            carGroup.draw(SCREEN)
            policeCarGroup.update()
            policeCarGroup.draw(SCREEN)
            # Make the user lose if they hit the police car
            if pygame.sprite.spritecollide(car, policeCarGroup, False, pygame.sprite.collide_mask):
                Lose(SCREEN, self)
            # Inform the generators of a new frame
            self.obstacle.update()
            self.trafficCone.update()
            # Draw the score
            font = pygame.font.SysFont('Segoe UI', 48, True, False)
            stamp = font.render(str(int(self.score())), True, (255, 255, 255))
            rect = stamp.get_rect()
            rect.right = 960
            rect.top = 50
            SCREEN.blit(stamp, rect)
        # Start music when the game is playing, stop it when they are not playing
        loop.onStart(Sound.music)
        loop.onStop(Sound.stopMusic)
        # Start the event loop
        loop.startFrames()

    @staticmethod
    def countDown(SCREEN):
        """Countdown at the beginning of the game"""
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
                countdownBg = pygame.image.load('countdownbg.png')
                stamp = font.render(str(3 - frames // 60), True, (149, 152, 154))
                stampRect = stamp.get_rect()
                stampRect.center = (505, 347)
                SCREEN.blit(countdownBg, (0, 0))
                SCREEN.blit(stamp, stampRect)
            # Stop the countdown just before 0
            if frames >= 179:
                loop.stop()
        # Start the loop, but give the number of frames passed to the update function
        loop.startFrames()

    def score(self):
        """Calculate the score"""
        return self.maxDistance * 0.1 + self.bonusPoints
