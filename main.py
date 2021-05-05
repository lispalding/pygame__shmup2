# MADE BY: Lisette Spalding
# ART WORK CREDIT: "Kenney.nl" @ "www.kenney.nl"
# FILE NAME: main.py
# PROJECT NAME: pygame__shmup
# DATE CREATED: 02/25/2021
# DATE LAST MODIFIED: 05/03/2021
# PYTHON VER. USED: 3.8

################### IMPORTS ####################
import pygame as pg
import random as r
from os import path

# Custom Imports
from settings import *
from sprites import *
################### FINISHED ###################

################ MAIN GAME LOOP ################
####### Game class #######
class Game(object):
    """ To use: Game()
    This class runs the main game. """
    def __init__(self):
        self.running = True

        pg.init()  # Initializing Pygame Library
        pg.mixer.init()  # Sounds

        # Initializing display
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)

        # Initializing clock
        self.clock = pg.time.Clock()

        self.fontName = pg.font.match_font("arial")

    def loadData(self):
        """ To use: self.loadData()
        This method loads the game's data. """
        ##### Loading Sounds:
        self.shootSound = pg.mixer.Sound(path.join(fxSoundsDir, "LaserLoop1.wav"))

        self.explosionSounds = []
        for snd in ["Explosion 5.wav", "Explosion 2.wav"]:
            self.explosionSounds.append(pg.mixer.Sound(path.join(fxSoundsDir, snd)))

        pg.mixer.music.load(path.join(musicSoundDir, "MattOglseby - 6.ogg"))
        pg.mixer.music.set_volume(0.5)
        ##### Loading Sounds FIN

        ##### Loading Images:
        ## Background ##
        self.background = pg.image.load(path.join(backgroundImgDir, "starfield.png")).convert()
        self.background_rect = self.background.get_rect()

        ## Player Image ##
        self.playerImage = pg.image.load(path.join(playerImgDir, "playerShip1_orange.png")).convert()

        ## Lives Image ##
        self.playerLivesImage = pg.image.load(path.join(playerImgDir, "playerShip1_orange.png")).convert()
        self.playerLivesImageMini = pg.transform.scale(self.playerLivesImage, (25, 19))
        self.playerLivesImageMini.set_colorkey(BLACK)

        ## NPC Image ##
        self.meteorImages = []
        self.npcImages = ["meteorBrown_big1.png", "meteorBrown_big2.png", "meteorBrown_big3.png",
                     "meteorBrown_big4.png", "meteorBrown_med1.png", "meteorBrown_med3.png",
                     "meteorBrown_small1.png", "meteorBrown_small2.png", "meteorBrown_tiny1.png",
                     "meteorBrown_tiny2.png", "meteorGrey_big1.png", "meteorGrey_big2.png",
                     "meteorGrey_big3.png", "meteorGrey_big4.png", "meteorGrey_med1.png",
                     "meteorGrey_med2.png", "meteorGrey_small1.png", "meteorGrey_small2.png",
                     "meteorGrey_tiny1.png", "meteorGrey_tiny2.png"]

        for image in self.npcImages:
            self.meteorImages.append(pg.image.load(path.join(meteorImgDir, image)).convert())

        ## Bullet Image ##
        self.bulletImage = pg.image.load(path.join(bulletImgDir, "laserRed16.png")).convert()

        ## Explosion Image ##
        self.explosionAnimation = {}
        self.explosionAnimation["lg"] = []
        self.explosionAnimation["sm"] = []
        self.explosionAnimation["player"] = []

        for i in range(9):
            filename = "regularExplosion0{}.png".format(i)
            image = pg.image.load(path.join(explosionImgDir, filename)).convert()
            image.set_colorkey(BLACK)

            imageLg = pg.transform.scale(image, (75, 75))
            self.explosionAnimation["lg"].append(imageLg)

            imageSm = pg.transform.scale(image, (32, 32))
            self.explosionAnimation["sm"].append(imageSm)

            filename = "sonicExplosion0{0}.png".format(i)
            image = pg.image.load(path.join(explosionImgDir, filename)).convert()
            image.set_colorkey(BLACK)

            self.explosionAnimation["player"].append(image)

        ## Powerups Images ##
        self.powerupImages = {}

        self.powerupImages["shield"] = pg.image.load(path.join(powerupsImgDir, "shield_gold.png")).convert()

        self.powerupImages["gun"] = pg.image.load(path.join(powerupsImgDir, "bolt_silver.png")).convert()

        self.livesPowerupImage = pg.image.load(path.join(powerupsImgDir, "star_gold.png")).convert()

        self.fuelPowerupImage = pg.image.load(path.join(powerupsImgDir, "pill_red.png")).convert()

        self.alienImage = pg.image.load(path.join(powerupsImgDir, "alien_extra_points.jpg")).convert()
        ##### Loading Images FIN

    def new(self):
        """ To use: self.new()
        This method creates a new game. """
        # Creating the sprite groups
        self.allSprites = pg.sprite.Group() # All sprites group
        self.playerGroup = pg.sprite.Group() # Player group

        ## Creating the game objects
        player = Player()

        # Adding player to sprite groups
        self.allSprites.add(player)
        self.playerGroup.add(player)

        # Start running game loop...
        self.run()

    def run(self):
        """ To use: self.run()
        This method runs the game. """
        ## Game loop
        self.playing = True

        while self.playing:
            self.clock.tick(FPS)

            # Processing input events
            self.events()

            # Processing updated variables
            self.update()

            # Creating the images on the screen
            self.draw()

    def events(self):
        """ To use: self.events()
        This method keeps track of the events that happen throughout running the game. """
        for event in pg.event.get():
            # Check for closing windows:
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def update(self):
        """ To use: self.update()
        This method updates what is shown on the HUD. """
        self.allSprites.update()

    def draw(self):
        """ To use: self.draw()
        This method draws the content on the screen. """
        self.screen.fill(BLACK)

        self.allSprites.draw(self.screen)

        ## This is the very last thing to happen during the draw:
        pg.display.flip()

    def showStartingScreen(self):
        """ To use: self.showStartingScreen()
        This method shows the starting screen. """
        pass

    def showGameOverScreen(self):
        """ To use: self.showGameOverScreen()
        This method shows the game over screen. """
        pass

####### Finished #######

g = Game() # Defining the game start

g.showStartingScreen() # Showing the starting screen for the new game

while g.running:
    g.new() # This kicks off the actual game loop
    g.showGameOverScreen()

# If the loop ever breaks this happens:
pg.quit()
################### FINISHED ###################