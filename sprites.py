# MADE BY: Lisette Spalding
# ART WORK CREDIT: "Kenney.nl" @ "www.kenney.nl"
# FILE NAME: sprites.py
# PROJECT NAME: pygame__shmup
# DATE CREATED: 02/25/2021
# DATE LAST MODIFIED: 04/03/2021
# PYTHON VER. USED: 3.8

################### IMPORTS ####################
import pygame as pg
import random as r
from os import path

# Custom Imports #
from settings import *
################### FINISHED ###################

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pg.Surface((50, 50))
        self.image.fill(PURPLE)

        # self.image = pg.transform.scale(playerImage, (50, 38))
        # self.image.set_colorkey(BLACK)

        ## Creating a bound box around the image:
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
        ## Bound box FIN

        if debugging: # Saying that if we are debugging, draw this big red circle
            pg.draw.circle(self.image, RED, self.rect.center, self.radius)

        ## Placement
        self.rect.center = (WIDTH/2, HEIGHT/2)
        ## Placement FIN

        self.speedx = 0
        self.speedy = 0

        self.shield = PLAYER_SHIELDS

        self.shootDelay = PLAYER_SHOOT_DELAY
        self.lastShot = pg.time.get_ticks()

        self.lives = player_lives

        self.hidden = False # If we are hidden this turns to "True"
        self.hideTimer = pg.time.get_ticks()

        self.keypressed = False

    def hide(self):
        self.hidden = True
        self.hideTimer = pg.time.get_ticks()

        self.rect.center = (WIDTH /2, (HEIGHT - (HEIGHT*.05))) # This way we spawn where we left off

    def shoot(self):
        """ To use: self.shoot()
                This function causes a bullet to be shot by the player. """
        now = pg.time.get_ticks()

        if now - self.lastShot > self.shootDelay:
            self.lastShot = now
            bullet = Bullet(self.rect.centerx, self.rect.top)
            bulletGroup.add(bullet)
            allSprites.add(bullet)

    def togglePressed(self):
        self.keypressed = False
        self.speedx = 0

    def update(self):
        """ To use: self.update()
        This is the function that will update the movement of the player character. """
        ##### !! Basic Movement !! #####
        self.speedx = 0

        # Cheking the Keystate
        keystate = pg.key.get_pressed()

        ########## !!!! .. FLOW MOVEMENT .. !!!! ##########
        if keystate[pg.K_LEFT] or keystate[pg.K_a]:
            self.speedx += -PLAYER_SPEED
            self.keypressed = True
        if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
            self.speedx = PLAYER_SPEED
            self.keypressed = True

        self.rect.x += self.speedx
        ########## !!!! .. FLOW FINISHED .. !!!! ##########

        ##### !!!! .. SCREEN BINDING .. !!!! #####
        # We are binding the player to the screen area
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        ##### !!!! .. BINDING FINISH .. !!!! #####