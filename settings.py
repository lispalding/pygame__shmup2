# MADE BY: Lisette Spalding
# ART WORK CREDIT: "Kenney.nl" @ "www.kenney.nl"
# FILE NAME: settings.py
# PROJECT NAME: pygame__shmup
# DATE CREATED: 02/25/2021
# DATE LAST MODIFIED: 04/03/2021
# PYTHON VER. USED: 3.8

################### IMPORTS #####################
import pygame as pg
import random as r
from os import path
################### FINISHED ###################

################## VARIABLES ###################
########## GAME VAR ##########
WIDTH = 360
HEIGHT = 480
FPS = 30

# Title
TITLE = "Space Shooter [Shmup] - Python"

# Other variables
debugging = False

######## GAME VAR FIN #########

######### PLAYER VAR #########
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 38

PLAYER_SPEED = 8

PLAYER_SHIELDS = 100
player_lives = 3

PLAYER_SHOOT_DELAY = 250
###### PLAYER VAR FIN ########
################### FINISHED ###################

################# FOLDER SETUP #################
## Basic Directories
gameFolder = path.dirname(__file__)
imageDirectory = path.join(gameFolder, "images")
soundDirectory = path.join(gameFolder, "sounds")

## Image Directories
backgroundImgDir = path.join(imageDirectory, "background")
bulletImgDir = path.join(imageDirectory, "bullet")
meteorImgDir = path.join(imageDirectory, "meteor")
playerImgDir = path.join(imageDirectory, "player")
explosionImgDir = path.join(imageDirectory, "explosions")
powerupsImgDir = path.join(imageDirectory, "power_ups")

## Sound Directories
fillerSoundDir = path.join(soundDirectory, "filler_sound")
ambientSoundDir = path.join(soundDirectory, "ambient_fx")
musicSoundDir = path.join(soundDirectory, "music")
fxSoundsDir = path.join(soundDirectory, "sound_fx")
################### FINISHED ###################

############### COLORS (R, G, B) ###############
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Custom Colors
ORANGE = (242, 162, 41)
YELLOW_GREEN = (182, 219, 18)
MINT = (63, 232, 159)
PURPLE = (182, 103, 224)
PINK = (224, 103, 139)
LIGHT_BLUE = (100, 162, 209)
YELLOW = (245, 233, 154)
################### FINISHED ###################