#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Victor Seifert'


import sys, time, os, shlex
import pygame
from subprocess import Popen, CREATE_NEW_CONSOLE, PIPE
from Tkinter import *
from pygame.locals import *
import random
# Initialize pygame as a modul
pygame.init()

clock = pygame.time.Clock

######################
# Setting variables
######################

###########################
# Important Variables. Not necessary for the save/load -process.
# They stay the same at all times.
###########################

# Display settings
FPS = 30 # Set maximum of 30 Frames per Second. Game pauses in between game-loops so it doesnt run too fast on fast computers.
WINDOWWIDTH = 900
WINDOWHEIGHT = 650
FLAGS = HWSURFACE|DOUBLEBUF
PLAYERSIZE = 50  # Width of character. Height = 2* width.

screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), FLAGS)
pygame.display.set_caption('Pythonia - Learning Python') # Caption fo the window0
clock = pygame.time.Clock() # We need this for FPS reduction.
font = pygame.font.SysFont("Calibri", 30) # Font for ingame text (buttons etc)
smallfont = pygame.font.SysFont("Calibri", 20)
bigfont = pygame.font.SysFont("monospace", 60)  # Font for "you died!"

# Set key bindings
LEFT = K_LEFT
RIGHT = K_RIGHT
JUMP = K_SPACE
MUSIC = K_m
ATTACK = K_a

MinLevel = 1
MaxLevel = 8

# X movement variable bindings
PLAYERACCEL = 3
PLAYERDEACCEL = 5
MAXSPEED = 20

enemySpeedX = 5
enemysize = 50
enemyBlink = False
IndexOfBlink = 0
blinkCounter = 0

# Y movement
AIRACCEL = 2 # Acceleration while jumping/ in the air
FALLACCEL = 5 # Acceleration while falling
JUMPMOD = 3.5  # Controls possible jumping height

JUMPACCEL = 31 # Acceleration while jumping (accel upwards)
MAXFALLSPEED = 50 # Maximum Fall speed

BLOCKWIDTH = 100 # Blocks are quadratic
BLOCKHEIGHT = 100

# Initialize counting coins/deaths/flags
coins_collected = 0
death_counter = 0
flag_counter = 0

buttonreload = 0

# Player HP starting (and max == 3)
playerHP = 3

inventar = ["Apfel", "Zauberstab"]

invMessage = ""
displayInvCounter = 0
displayInventarButton = False

levelcounter = 1 # current Level
level = [] # Will contain current level 2D array
starterbool = True # True if game begins, if player presses Start => False


levelThree = 0


# Empty List - flag gets added if player runs into a flag.
# A function later on checks each loop of the gameloop if a flag was added.
currentflags = []

x = 0
y = 0
spawnpoint = (x,y)
# player = pygame.Rect(10*BLOCKWIDTH, 9*BLOCKHEIGHT, PLAYERSIZE, PLAYERSIZE*2)


########### GRAPHICS ############

def loadImage(filename):
    # Description: Loads image into pygame
    # Parameters:
    #   - image file (e.g. ".png")
    # Returns: Converted image for use with pygame
    image = pygame.image.load(filename)

    # convert to alpha if image has transparent background (player, coins etc)
    if image.get_alpha() is None:
        image = image.convert()
    else:
        image = image.convert_alpha()

    # Colour Magenta (r,g,b,) will be left out while rendering
    # (allows round figures - 2nd possibility next to alpha-channel transparency)
    colorkey = (255, 0, 255)
    image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image


# All graphics initialized which are needed for the game
myimage_left = loadImage("graphics/left.png")
myimage_right = loadImage("graphics/right.png")
myimage_jump = loadImage("graphics/jump.png")
myimage_stand = loadImage("graphics/stand.png")
myimage_left_w = loadImage("graphics/left_w.png")
myimage_right_w = loadImage("graphics/right_w.png")
myimage_jump_w = loadImage("graphics/jump_w.png")
myimage_stand_w = loadImage("graphics/stand_w.png")
myimage_fireR = loadImage("graphics/fireR.png")
myimage_fireL = loadImage("graphics/fireL.png")
myimage_coin = loadImage("graphics/coin.png")
myimage_coinCounter = loadImage("graphics/coins.png")
myimage_flagdown = loadImage("graphics/flag_down.png")
myimage_flagup = loadImage("graphics/flag_up.png")
myimage_kill= loadImage("graphics/barbs.png")
myimage_enemy= loadImage("graphics/enemy1.png")
myimage_enemyL= loadImage("graphics/enemy1.png")
myimage_hp = loadImage("graphics/hp.png")
myimage_heart = loadImage ("graphics/heart.png")
myimage_apple = loadImage ("graphics/apple.png")
myimage_endscreen = loadImage ("graphics/endscreen.png")
myimage_score = loadImage("graphics/score.png")
myimage_start = loadImage("graphics/Willkommen.png")
myimage_block = loadImage("graphics/block.png")
# Colours for later use
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 150,   0)
LIGHTGREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

# Shot: (if shot = True
# [Blockwidth, Blockheight, direction(boolean - left for true), enemy position from spawn (0 at the beginning), Maximum range in which enemy moves (pixels)
        # , speed, enemy_number in the level]


############# LEVEL DESIGN #########

BLANK = '.' #
BLOCK = '0' # HitBox (Wall)
KILL = '1' # Barbs
COIN = '3' # Coins for collecting
FLAGDOWN = '4' # Flags will be down if not yet encountered.
FLAGUP = '5' # Flags will be updated to '5' if player ran into them.
HEART = '6' # HP Hearts to collect
APPLE = '7' # Apples to collect
BLINK = '8' # Blinking Blocks


level1 = ['00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
          '06.............3...3...3..............0..................00..................................................0',
          '0000.........00000000000...33......3...0.................0.........................3........................60',
          '0..................0..000000000000000..0.................00.......................000....................3.000',
          '0......3..3........0...................033...............00........................00.0.................000000',
          '0....0000000.......0..3..........3.....033...............00....................3...00.0.3............3..000000',
          '0.....000000.......000000......0000..000000000...........00...................000..00.0000......3..0000......0',
          '003..............110.3............3.1110000000003........00.......3...3.....000....00..........00............0',
          '000..............000000000..000000000000......0000.......0.......00..00...3........00......00000.............0',
          '00003..............0.3.............3...0........0000.............00..00..000.......00.....000................0',
          '000000.........40..0000000000000000000.0............4...........3..................0000011...................0',
          '00000000000000000..0...................0..........3.00..........000......00........0000000...................0',
          '0......3...........00003.......3.....3.0..........00000000.....0000...........3....0......................00.0',
          '0..............000000000......0000000000...3...0000000000011111000000011....0000.............3.....3.........0',
          '011.3.............3.00000003...............000000000000000000000000000000111111111111111111110000000000....4.0',
          '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000']


level2 = ['00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
          '0.............................00......000..................................................00................0',
          '0.............................00......0006.................................................00................0',
          '0.........................3...00......00000....3...........................................00................0',
          '0.................3.00000000..00..............0000....................................3....00................0',
          '0................000000.......00.....................3...........................3.110000..00................0',
          '0.........3....0000...........00...................0000.....................3.4000000.3....00................0',
          '0.....300000....00............00.........................3...........3......00000..3..0000000................0',
          '0..000000000....00..3......0000..........................00...............0000.....00000000..................0',
          '01..............0000011....00............................00..................00.3....3...3......3.......000000',
          '000................000011...3........................3..........3..00000......00000000000000000009...........0',
          '0000...00000..........0000000000..................9.000.........0000..........000000000000000000000.3........0',
          '0.....000000.39.3........3....00....3.....3.....3.00000.......00..........00000000000000000000000000000......0',
          '0....0000000000000...........300...000...000....000000......00......3.....0000000000000000000000000000000....0',
          '0.3......3......60....3.....3.001110001110001111000000......00111111....0000000000000000000000000000000000.4.0',
          '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',]


level3 = ['00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
          '0000000000000000000000000000000000000000000000...300000.........................00000000000000000....3...00000',
          '000000000000000000000000000000000000000000....3...00000000.....0000000000000000.0000000000000.......000..00000',
          '00000000000000000000000000............3......000..00000........0000000000000000.00..........3.0000000000.3...0',
          '0000000000000000000000000........3......00000000..00000......000000000000000000..3..........000000000000000..0',
          '0000000000000000000000000..........000000000000...00000........0000000000000........00000000000000000000000..0',
          '000............000000000...3.0000000000000...3....0000000......00000000000000....0000000000000000000000..3...0',
          '000.3...........0000.....000000000000000....00000.00000........00000......3000000000000000000000000000..000000',
          '000................3.0000000000000000.....0000001100000.....00000.........0000000000000000000000000000..000000',
          '00011.........30000000000000000......3.0000000000000000..................00000000000000000000000000000.......0',
          '000000000000000000000000000..3...000000000000000000000000000000......11.300000000000000000000000000000.3...4.0',
          '000000000000000000000000000..000000000000000000000000000000......3.0000000000000000000000000000000000000000000',
          '00000000000000000.....0...3..0000000..........00000.3.000...00000000000000000000000000000000000000000000000000',
          '0000000000000000.........0000000000.....3......0.........3..00000000000000000000000000000000000000000000000000',
          '0000000000000000..........3.......4....11...6.....00...0000000000000000000000000000000000000000000000000000000',
          '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',]


level4 = ['00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
          '0.............................00000...6........................000000000000..............00000000............0',
          '0.............................00000000000.........................0000000..................000000..........4.0',
          '0.......................3.00..00000003..00...3......................0000..............3........00.....3..00000',
          '0.......................0000...0000003...000.00.7....................00..............................000000000',
          '0...................3.000000........00....00.00.00.3.................00................7........3.000000000000',
          '0...............73.000000000..3.....000.........00.00................00..........3.000000000..0000000000000000',
          '0.............3.0000000000000.......000000000......00.................0.........000000000000770000000000000000',
          '0............000000000000000001.....000000000.........3...3..................000000000000000..00.............0',
          '0111111....00000000000........0003................0000000000.............3.0000000000....000..00.............0',
          '00000000000000000000...3....3....00..........00..........000..........70000000000000.....0001100.............0',
          '00000000000000000.....000..000......3......3..............0003....34000000000000000........0000..............0',
          '0000000000000000......000110000000000...00000000....00....000011.0000000000000000000.........................0',
          '0.......0000000......000000000.....03...00000000....00....0000000000.........................................0',
          '0.......0000.3...........3.........6.111............00...........00000.......................................0',
          '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',]


level5 = ['00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
          '0............000..........................00......................................................000........0',
          '0............000..........................00.....................................................3000........0',
          '0............000.........................600.....................................................0000........0',
          '0.3..........000.....................3..0000......................................3.....3.....000000.........0',
          '0000.........000..................3.00.......................................3..000000000000..00.............0',
          '000000.......000...............7.00.00...................................7.000000000..........00.............0',
          '0........3.................3...0000......................................00000000...........3.00.............0',
          '0.......0000.........3...0000............3.......3.........3......3..000000000......3..000000000.............0',
          '0111....0000........000................4000..00..00.......000...00000000000000.....000000....................0',
          '00000.3.........3.0000...............000000..00..0000............000000000000......00............3...........0',
          '00000000........0000.............................000000....3.......00000000..................3..00...3.......0',
          '0000.......3......00............3.000...................7..00......00000000.........3.......00..00..00.......0',
          '00.......00000..............3...0000000..3............0000000000...............000000000.......3............40',
          '00.3..0000000000.....3......0000000000000011111111110000000000000003........0000000000000001111000011110000000',
          '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',]


level6 = ['00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
          '0.......................................333333333.................................................000........0',
          '0.......................................8888888..................................................3000........0',
          '0....................................7.........3.3..88...........................................0000........0',
          '0.3...............................88...8.....88888.....88..888..3....7...........3.....3.....000000..........0',
          '0000.............................88..8.............8....7...........88......73..000088888888..00.............0',
          '000000.......................88..88.......888.......8888.........888.......008888000..........00.............0',
          '0........3.7.......333388......88...........................88...........00333333...........3400.............0',
          '0.......0000.........8888......8......8883.......3.........3......3..000000000......3..000000000.............0',
          '0111....0000........8....................................000.8800000000000000.....000000.....................0',
          '00000.3.........3...888...8.......888........88..0000............000000000000......00............3...........0',
          '00000000........0000..................8..........000000....3.......00000000..................3..00...3.......0',
          '0000.......3......00............3.808......................00......00000000......7..3.......00..00..00.......0',
          '00.......00000..............3...888888.83............8888880000................00888088880888..3.....888888840',
          '00.3..0000000000.....3......00001111111111111111111100000000000000031111111..111111111111111111000011111111100',
          '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',]


level7 = ['00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
          '06.............3...3...3.....0........0......................................................................0',
          '0000.........00000000000...330.....3...0.....................................................................0',
          '0...............8.........88.0......0..0.................................................................3.000',
          '0......3..3.....8..8888......0.........033.............4...........................00.0.................000000',
          '0...............8.....3.888880...3.....033.........00000000..8..0..8..0..8..0..8..000.0.3............3.4000000',
          '0...............8...........0.0000..000000000...........00...................000..00.0000......3..000000.....0',
          '003.............8110.3.......0....3.....000000003........00.......3...3.....000....00..........00............0',
          '000.............88888888....1088....88........0000.......0.......00..00...3................00000.............0',
          '00003................3....8800333...............0000.....80...............................000................0',
          '000000..............8888.......88......0.................08.....3..................0000011...................0',
          '00000000000000000..000..............0000..........3.00...80.....000......00......880000000...................0',
          '0......3...................88..3.....3.0000000000000000000.....0000....00.....3.8880.........................0',
          '0..............00000...88888800000000000...3...0000000000011111000000011....00000000.........3.....3.........0',
          '011.3.............3.0011111110.............0000000000000000000000000000001111111111111111111111111111111111110',
          '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000']


level8 = ['00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
          '06.............3...3...3..............0..................00..................................................0',
          '0000.........00000000000...33......3...0.................0.........................3........................60',
          '0..................0..000000000000000..0.................00.......................000....................3.000',
          '0......3..3........0...................033...............00........................00.0.................000000',
          '0....0000000.......0..3..........3.....033...............00....................3...00.0.3............3..000000',
          '0.....000000.......000000......0000..000000000...........00...................000..00.0000......3..0000......0',
          '003..............110.3............3.1110000000003........00.......3...3.....000....00..........00............0',
          '000..............000000000..000000000000......0000.......0.......00..00...3........00......00000.............0',
          '00003..............0.3.............3...0........0000.............00..00..000.......00.....000................0',
          '000000..........0..0000000000000000000.0............4...........3..................0000011...................0',
          '00000000000000000..0...................0..........3.00..........000......00........0000000...................0',
          '0......3...........00003.......3.....3.0..........00000000.....0000...........3....0......................00.0',
          '0..............000000000......0000000000...3...0000000000011111000000011....0000.............3.....3.........0',
          '011.3.............3.00000003...............000000000000000000000000000000111111111111111111110000000000....4.0',
          '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000']


BLANK = '.' #
BLOCK = '0' # HitBox (Wall)
KILL = '1' # Barbs
COIN = '3' # Coins for collecting
FLAGDOWN = '4' # Flags will be down if not yet encountered.
FLAGUP = '5' # Flags will be updated to '5' if player ran into them.
HEART = '6' # HP Hearts to collect
APPLE = '7' # Apples to collect
BLINK = '8' # Blinking Blocks




########## IN-GAME FUNCTIONS##########

    # Description:
    # Parameters:
    # Returns:
global listblocks
# sets all variables needed for the gamewindow


blinkingObjects = []



def prepBlinks(levelx):
    # Description:
    #   Preparation of "blinking" Objects. Objects appear and disappear randomly.
    #   This feature is used in higher levels to make clouds appear and disappear on which the player can potentially walk.
    # Parameters:
    #   - Takes the 2D Array Map of the level
    # Returns: nothing
    # Use: Once at the beginning of the level.
    global blinkingObjects

    blinkingObjects = []
    obj =  find_elem_in_2d_coordinates('8', levelx)
    for x in obj:
        blinkingObjects.append([x[0],x[1],random.randint(50,250), 0]) #[c1,c2, randomCounter, cooldown]

    for x in blinkingObjects:
        c1 = x[0]
        c2 = x[1]
        st1 = levelx[c1]
        st2 = st1[:c2]
        st3 = st2 + "0" +st1[c2+1:]
        levelx[c1] = st3

def changeBlinks(list1, level):
    # Description: Makes an object appear/disappear.
    # Parameters:
    #   - gives a list describing the "blinking" object
    #   - The 2D Array Map of the level
    # Returns: nothing

    # Initialize
    c1 = list1[0]
    c2 = list1[1]
    if (level[c1][c2] == '.'):
        st1 = level[c1]
        st2 = st1[:c2]
        st3 = st2 + "0" +st1[c2+1:]
        level[c1] = st3
    else:
        st1 = level[c1]
        st2 = st1[:c2]
        st3 = st2 + "." +st1[c2+1:]
        level[c1] = st3

def handleRandomCounters(level):
    global blinkingObjects
    for x in blinkingObjects:
        if x[3] > 0: # cooldown
            x[3] -= 1
            if x[3] == 0:
                changeBlinks(x,level)
                x[2] = random.randint (50,250)

        else:
            if x[2] > 0:
                x[2] -= 1
                if x[2] == 0:
                    changeBlinks(x,level)
                    x[3] = random.randint(50,100)

            else:
                changeBlinks(x, level)
                x[3] = random.randint(50,100)







def prepare_level(level_counter):
    # Description: prepares level
    # Parameters:
    #   - current level (1-5)
    # Returns: nothing (deals with global variables to set level)

    # All global variables this function accesses
    global levelcounter
    global LEVELHEIGHT
    global LEVELWIDTH
    global listenemy0
    global listenemy1
    global listenemy2
    global listenemies

    global map_coin_Preparation
    global listdyinglists
    global map_hearts_Preparation
    global map_apples_Preparation
    global map_flags_Preparation
    global listcoinlists
    global remaining_coins
    global listhearts
    global listapples
    global remaining_hearts
    global remaining_apples
    global listflags
    global remaining_flags

    global player
    global myimage_wall
    global myimage_wall2
    global myimage_enemy
    global myimage_enemyL
    global background_image
    global soundbg
    global listblocks
    global spawnpoint
    global blinkingObjects

    # load current level into global variable
    levelcounter = level_counter


    #Prepare if level == 1
    if levelcounter == 1:
        # set level size for rendering & camera according to new level
        LEVELWIDTH = len(level1[0])
        LEVELHEIGHT = len(level1)


        blinkingObjects = []
        prepBlinks(level1)
        # Set player spawn point

        spawnpoint = (10,9)
        player = pygame.Rect(10*BLOCKWIDTH, 9*BLOCKHEIGHT, PLAYERSIZE, PLAYERSIZE*2)
        # Load level specific graphics
        myimage_wall = loadImage("graphics/brick_gras.png")
        myimage_wall2 = loadImage("graphics/brick_gras2.png")
        myimage_enemy= loadImage("graphics/enemy1.png")
        myimage_enemyL= loadImage("graphics/enemy1L.png")
        background_image = loadImage("graphics/background1.png")
        blockdmg1 = [11,10,True,0,250,2,0]
        blockdmg2 = [46,11,False,250,250,2,1]
        blockdmg3 = [68,8,False,250,250,2,2]
        blockdmg4 = [72,8,False,250,250,2,3]
        blockdmg5 = [94,6,False,250,250,2,4]
        blockdmg6 = [105,13,False,250,250,2,5]
        listblocks = [blockdmg1, blockdmg2, blockdmg3, blockdmg4, blockdmg5, blockdmg6]

        # Load level specific music & set volumne
        pygame.mixer.music.load('sounds/bgSound1.ogg')
        pygame.mixer.music.set_volume(0.04)
        pygame.mixer.music.play(-1,0) # endless loop
        # Enemies are dealt with as list objects (cant change value in tuples in Python)
        # [Blockwidth, Blockheight, direction(boolean - left for true), enemy position from spawn (0 at the beginning), Maximum range in which enemy moves (pixels)
        # , speed, enemy_number in the level]
        listenemy0 = [9,10,False,0,250,2,0,2]
        listenemy1 = [10,4,False,0,300,2,1,2]
        listenemy2 = [34, 5, True,0,300,2,2,2]
        listenemy3 = [97, 13, False,0,250,2,3,2]
        listenemy4 = [70, 12, False,0,300,2,4,2]
        listenemy5 = [101, 13, False,0,300,2,5,2]
        # List of enemies for later use of rendering and enemy movement
        # Makes amount of enemies flexible for each level, listenemy0-4 will not be accessed on themselves.
        # Only the complete list of them.
        listenemies = [listenemy0, listenemy1, listenemy2,listenemy3,listenemy4, listenemy5]

    # Prepare if level == 2
    # For variable understanding see above (==1)
    elif levelcounter == 2:
        LEVELWIDTH = len(level2[0])
        LEVELHEIGHT = len(level2)

        blockdmg1 = [70,8,True,0,250,2,0]
        blockdmg2 = [34,11,True,0,250,2,1]
        blockdmg3 = [40,11,True,0,250,2,2]
        blockdmg4 = [47,11,True,0,250,2,3]
        listblocks = [blockdmg1, blockdmg2, blockdmg3, blockdmg4]

        spawnpoint = (7,10)
        player = pygame.Rect(8*BLOCKWIDTH, 10*BLOCKHEIGHT, PLAYERSIZE, PLAYERSIZE*2)
        myimage_wall = loadImage("graphics/brick_beach.png")
        myimage_wall2 = loadImage("graphics/brick_beach2.png")
        myimage_enemy= loadImage("graphics/enemy2.png")
        myimage_enemyL= loadImage("graphics/enemy2L.png")
        background_image = loadImage("graphics/background2.png")
        pygame.mixer.music.load('sounds/bgSound2.ogg')
        pygame.mixer.music.set_volume(0.04)
        pygame.mixer.music.play(-1,0)
        listenemy0 = [96, 9, False,0,300,2,0,2]
        listenemy1 = [51, 11, False,0,150,2,1,2]
        listenemy2 = [14, 12, False,0,200,2,2,2]
        listenemy3 = [102, 11, False,0,200,2,3,2]
        listenemies = [listenemy0, listenemy1, listenemy2, listenemy3]

    # Prepare if level == 3
    # For variable understanding see above (==1)
    elif levelcounter == 3:
        LEVELWIDTH = len(level3[0])
        LEVELHEIGHT = len(level3)

        blockdmg1 = [14,7,True,0,250,2,0]
        listblocks = [blockdmg1]
        listenemies = []
        spawnpoint = (10,9)
        player = pygame.Rect(10*BLOCKWIDTH, 9*BLOCKHEIGHT, PLAYERSIZE, PLAYERSIZE*2)
        myimage_wall = loadImage("graphics/brick_hoehle.png")
        myimage_wall2 = loadImage("graphics/brick_hoehle2.png")
        myimage_enemy= loadImage("graphics/enemy3.png")
        myimage_enemyL= loadImage("graphics/enemy3L.png")
        background_image = loadImage("graphics/background3.png")
        pygame.mixer.music.load('sounds/bgSound3.ogg')
        pygame.mixer.music.set_volume(0.04)
        pygame.mixer.music.play(-1,0)
        listenemy0 = [33, 5, False,0,300,2,0,2]
        listenemy1 = [21, 14, True,0,300,2,1,2]
        listenemies = [listenemy0, listenemy1]

    # Prepare if level == 4
    # For variable understanding see above (==1)
    elif levelcounter == 4:
        LEVELWIDTH = len(level4[0])
        LEVELHEIGHT = len(level4)

        blockdmg1 = [14,8,True,0,250,2,0]
        blockdmg2 = [21,4,True,0,250,2,1]
        blockdmg3 = [49,5,True,0,250,2,2]
        blockdmg4 = [87,6,True,0,250,2,3]
        blockdmg5 = [100,5,True,0,250,2,4]
        listblocks = [blockdmg1, blockdmg2, blockdmg3, blockdmg4, blockdmg5]

        spawnpoint = (8,9)
        player = pygame.Rect(8*BLOCKWIDTH, 9*BLOCKHEIGHT, PLAYERSIZE, PLAYERSIZE*2)
        myimage_wall = loadImage("graphics/brick_snow.png")
        myimage_wall2 = loadImage("graphics/brick_snow2.png")
        myimage_enemy= loadImage("graphics/enemy4.png")
        myimage_enemyL= loadImage("graphics/enemy4L.png")
        background_image = loadImage("graphics/background4.png")
        pygame.mixer.music.load('sounds/bgSound4.ogg')
        pygame.mixer.music.set_volume(0.04)
        pygame.mixer.music.play(-1,0)
        listenemy0 = [79, 7, False,0,200,2,0,2]
        listenemy1 = [54, 8, True,0,400,2,1,2]
        listenemy2 = [18, 14, True,0,300,2,2,2]
        listenemy3 = [70, 10, True,0,200,2,3,2]
        listenemies = [listenemy0, listenemy1, listenemy2, listenemy3]

    # Prepare if level == 5
    # For variable understanding see above (==1)
    elif levelcounter == 5:
        LEVELWIDTH = len(level5[0])
        LEVELHEIGHT = len(level5)
        listblocks = []
        listenemies = []

        spawnpoint = (10,9)
        player = pygame.Rect(10*BLOCKWIDTH, 9*BLOCKHEIGHT, PLAYERSIZE, PLAYERSIZE*2)
        myimage_wall = loadImage("graphics/brick_desert.png")
        myimage_wall2 = loadImage("graphics/brick_desert2.png")
        myimage_enemy= loadImage("graphics/enemy5.png")
        myimage_enemyL= loadImage("graphics/enemy5L.png")
        background_image = loadImage("graphics/background5.png")
        pygame.mixer.music.load('sounds/bgSound5.ogg')
        pygame.mixer.music.set_volume(0.04)
        pygame.mixer.music.play(-1,0)
        listenemy0 = [28, 7, False,0,300,2,0,2]
        listenemy1 = [72, 7, True,0,300,2,1,2]
        listenemy2 = [7, 10, True,0,200,2,2,2]
        listenemy3 = [58, 12, True,0,350,2,3,2]
        listenemy4 = [90, 13, True,0,200,2,4,2]
        listenemies = [listenemy0, listenemy1, listenemy2, listenemy3, listenemy4]

    elif levelcounter == 6:
        LEVELWIDTH = len(level6[0])
        LEVELHEIGHT = len(level6)


        blockdmg0 = [36, 6,True,0,250,2,0]
        blockdmg1 = [24, 6,True,0,250,2,0]
        blockdmg2 = [83, 6,True,0,250,2,0]
        blockdmg3 = [96, 9,True,0,250,2,0]
        listblocks = [blockdmg0,blockdmg1,blockdmg2,blockdmg3]


        listenemy0 = [11, 7, True,0,200,2,4,2]
        listenemy1 = [24, 14, True,0,200,2,4,2]
        listenemy2 = [31, 13, True,0,200,2,4,2]
        listenemy3 = [4, 83, True,0,200,2,4,2]
        listenemy4 = [91, 7, True,0,200,2,4,2]
        listenemies = [listenemy0,listenemy1,listenemy2,listenemy3,listenemy4]

        blinkingObjects = []
        prepBlinks(level6)

        spawnpoint = (10,9)
        player = pygame.Rect(10*BLOCKWIDTH, 9*BLOCKHEIGHT, PLAYERSIZE, PLAYERSIZE*2)
        myimage_wall = loadImage("graphics/brick_heaven.png")
        myimage_wall2 = loadImage("graphics/brick_heaven2.png")
        myimage_enemy= loadImage("graphics/enemy6.png")
        myimage_enemyL= loadImage("graphics/enemy6L.png")
        background_image = loadImage("graphics/background6.png")
        pygame.mixer.music.load('sounds/bgSound5.ogg')
        pygame.mixer.music.set_volume(0.04)
        pygame.mixer.music.play(-1,0)



    elif levelcounter == 7:
        LEVELWIDTH = len(level7[0])
        LEVELHEIGHT = len(level7)

        blockdmg0 = [53, 5,True,0,250,2,0]
        blockdmg1 = [69, 4,True,0,250,2,0]
        blockdmg2 = [63, 4,True,0,250,2,0]
        blockdmg3 = [35, 8,True,0,250,2,0]
        listblocks = [blockdmg0,blockdmg1,blockdmg2, blockdmg3]


        listenemy0 = [19, 12, False,0,300,2,0,2]
        listenemy2 = [46, 11, False,0,300,2,0,2]
        listenemy3 = [54, 4, False,0,300,2,0,2]
        listenemy4 = [10, 10, False,0,300,2,0,2]
        listenemy5 = [46, 11, False,0,300,2,0,2]
        listenemies = [listenemy0, listenemy2,listenemy3,listenemy4,listenemy5]

        blinkingObjects = []
        prepBlinks(level7)
        spawnpoint = (6,13)
        player = pygame.Rect(6*BLOCKWIDTH, 13*BLOCKHEIGHT, PLAYERSIZE, PLAYERSIZE*2)
        myimage_wall = loadImage("graphics/brick_mountain.png")
        myimage_wall2 = loadImage("graphics/brick_mountain2.png")
        myimage_enemy= loadImage("graphics/enemy7.png")
        myimage_enemyL= loadImage("graphics/enemy7L.png")
        background_image = loadImage("graphics/background7.png")
        pygame.mixer.music.load('sounds/bgSound5.ogg')
        pygame.mixer.music.set_volume(0.04)
        pygame.mixer.music.play(-1,0)


    elif levelcounter == 8:
        levelcounter = 8
        LEVELWIDTH = len(level8[0])
        LEVELHEIGHT = len(level8)

        blockdmg1 = [29,7,True,0,250,2,0]
        blockdmg2 = [27,14,True,0,250,2,0]
        blockdmg3 = [52,5,True,0,250,2,0]
        blockdmg4 = [68,7,True,0,250,2,0]
        blockdmg5 = [72,7,True,0,250,2,0]
        blockdmg6 = [103, 10,True,0,250,2,0]
        listblocks = [blockdmg1,blockdmg2,blockdmg3, blockdmg4, blockdmg5,blockdmg6]
        listenemy0 = [15, 14, False,0,300,2,0,2]
        listenemy1 = [10, 4, False,0,300,2,0,2]
        listenemy2 = [20, 1, False,0,300,2,0,2]
        listenemy3 = [35, 9, False,0,300,2,0,2]
        listenemy4 = [46, 13, False,0,300,2,0,2]
        listenemy5 = [85, 2, False,0,200,2,0,2]
        listenemies = [listenemy0, listenemy1, listenemy2, listenemy3, listenemy4, listenemy5,]

        blinkingObjects = []
        prepBlinks(level8)
        spawnpoint = (13,6)
        player = pygame.Rect(6*BLOCKWIDTH, 13*BLOCKHEIGHT, PLAYERSIZE, PLAYERSIZE*2)
        myimage_wall = loadImage("graphics/brick_lava.png")
        myimage_wall2 = loadImage("graphics/brick_lava2.png")
        myimage_enemy= loadImage("graphics/enemy8.png")
        myimage_enemyL= loadImage("graphics/enemy8L.png")
        background_image = loadImage("graphics/background8.png")
        pygame.mixer.music.load('sounds/bgSound5.ogg')
        pygame.mixer.music.set_volume(0.04)
        pygame.mixer.music.play(-1,0)

#### The following part loads all coins/barbs/hearts/flags from the specific level (2D Array)
#### into the global variables which are accessed in the gameloop.
#### Seperated from part above to keep the overview easy.

# if level == X
    # Prepare Coin for collecting....
    # Prepare barbs for dying....
    # Prepare hearts for collecting....
    # Prepare apples for collecting...
    # Prepare flags for running into....

    if levelcounter == 1:
        map_coin_Preparation = setcoins(level1)
        listdyinglists = setbarbs(level1)
        map_hearts_Preparation = sethearts(level1)
        map_apples_Preparation = setapples(level1)
        map_flags_Preparation = setflags(level1)
    elif levelcounter == 2:
        map_coin_Preparation = setcoins(level2)
        listdyinglists = setbarbs(level2)
        map_hearts_Preparation = sethearts(level2)
        map_apples_Preparation = setapples(level2)
        map_flags_Preparation = setflags(level2)
    elif levelcounter == 3:
        map_coin_Preparation = setcoins(level3)
        listdyinglists = setbarbs(level3)
        map_hearts_Preparation = sethearts(level3)
        map_apples_Preparation = setapples(level3)
        map_flags_Preparation = setflags(level3)
    elif levelcounter == 4:
        map_coin_Preparation = setcoins(level4)
        listdyinglists = setbarbs(level4)
        map_hearts_Preparation = sethearts(level4)
        map_apples_Preparation = setapples(level4)
        map_flags_Preparation = setflags(level4)
    elif levelcounter == 5:
        map_coin_Preparation = setcoins(level5)
        listdyinglists = setbarbs(level5)
        map_hearts_Preparation = sethearts(level5)
        map_apples_Preparation = setapples(level5)
        map_flags_Preparation = setflags(level5)
    elif levelcounter == 6:
        map_coin_Preparation = setcoins(level6)
        listdyinglists = setbarbs(level6)
        map_hearts_Preparation = sethearts(level6)
        map_apples_Preparation = setapples(level6)
        map_flags_Preparation = setflags(level6)
    elif levelcounter == 7:
        map_coin_Preparation = setcoins(level7)
        listdyinglists = setbarbs(level7)
        map_hearts_Preparation = sethearts(level7)
        map_apples_Preparation = setapples(level7)
        map_flags_Preparation = setflags(level7)
    elif levelcounter == 8:
        map_coin_Preparation = setcoins(level8)
        listdyinglists = setbarbs(level8)
        map_hearts_Preparation = sethearts(level8)
        map_apples_Preparation = setapples(level8)
        map_flags_Preparation = setflags(level8)
    else:
        # Safety net
        map_coin_Preparation = setcoins(level8)
        listdyinglists = setbarbs(level8)
        map_hearts_Preparation = sethearts(level8)
        map_apples_Preparation = setapples(level8)
        map_flags_Preparation = setflags(level8)

    # Set coins
    listcoinlists = map_coin_Preparation[0]
    remaining_coins = map_coin_Preparation[1] # So it cannot be collected more than once

    # Set hearts
    listhearts = map_hearts_Preparation[0]
    remaining_hearts = map_hearts_Preparation[1] # So it cannot be collected more than once

    # Set apples
    listapples = map_apples_Preparation[0]
    remaining_apples = map_apples_Preparation[1]

    # Set flags
    listflags = map_flags_Preparation[0]
    remaining_flags = map_flags_Preparation[1] # So it cannot be collected more than once





##### The following functions saves you work when creating new levels:
##### You dont have to create a new variable for every coin/heart/apple/barb/flag yourself.
##### The prepare_level in combination with these functions does it for you once you marked the spot (e.g. of a coin) in the 2D Array.


def setcoins(map_array):
    # Description: Creates for every single '3' (aka coin) in the 2D Array a coin variable to control collecting coins
    # Parameters:
    #   - Takes the 2D Array Map of the level
    # Returns: A tuple
    #   - listofcoins: contains complex coin variables (Y-hitbox, X-hitbox, tuple of coordinate)
    #   - remaining: contains a tuple of the coordinates of a coin (if a coin is collected, its tuple will be deleted from this list)

    # Initialize
    listofcoins = []
    remaining = []
    # This function gets all '3's in a 2D array map and returns their coordinates as a list of tuples
    coin_coordinates = find_elem_in_2d_coordinates('3', map_array )
    for c in coin_coordinates: # Create variables
        x = c[1]
        y = c[0]
        # The following two lines create the hitbox of coins
        y = range (y*100, y*100+101)
        x = range (x*100-25, x*100+35)
        # Create tuple variable (coordinates) for remaining
        ges = str(c[0]) + "," + str(c[1])
        remaining.append(ges)
        # Append the coins with their hitbox to listofcoins
        listofcoins.append( (x, y, (c[0],c[1]))  ) # X Hitbox, Y Hitbox, Tuple of coordinates
    return (listofcoins, remaining)


def setbarbs(map_array):
    # Description: Creates for every single '1' (aka barb) in the 2D Array a barb variable to control running into barbs
    # Parameters:
    #   - Takes the 2D Array Map of the level
    # Returns:
    #   - listbarbs: contains complex barb variable

    # Initialize
    listbarbs = []
    # This function gets all '1's in a 2D array map and returns their coordinates as a list of tuples
    barb_coordinates = find_elem_in_2d_coordinates('1', map_array )
    for c in barb_coordinates:# Create variables
        x = c[1] # x coordinate from tuple
        y = c[0] # y coordinate from tuple
        # Hitboxes of barbs
        y = range (y*100+50 , y*100+101)
        x = range (x*100-40, x*100+100)
        # Append the barbs with their hitboxes and coordinates to listbarbs
        # No remaining(barbs) needed, as barbs dont disappear when run into
        listbarbs.append( (x, y, (c[0],c[1]))) # X Hitbox, Y Hitbox, Tuple of coordinatess
    return listbarbs


def sethearts(map_array):
    # Description: Creates for every single '6' (aka heart) in the 2D Array a heart variable to control collecting hearts
    # Parameters:
    #   - Takes the 2D Array Map of the level
    # Returns: A tuple
    #   - listofhearts: contains complex heart variables (Y-hitbox, X-hitbox, tuple of coordinate)
    #   - remaining_hearts (hearts cannot be collected twice, heart is deleted from this list if collected)

    # Initialize
    listofhearts = []
    remaining_hearts = []
    # This function gets all '6's in a 2D array map and returns their coordinates as a list of tuples
    heart_coordinates = find_elem_in_2d_coordinates('6', map_array )
    for c in heart_coordinates: # Create variables
        x = c[1]
        y = c[0]
        # Hitboxes
        y = range (y*100, y*100+101)
        x = range (x*100-25, x*100+35)
        # Create tuple variable for remaining
        ges = str(c[0])+ "," +str (c[1])
        remaining_hearts.append(ges)
        # Append the hearts with their hitboxes and coordinates to listhearts
        listofhearts.append( (x, y, (c[0],c[1]))  ) # X Hitbox, Y Hitbox, Tuple of coordinates
    return (listofhearts, remaining_hearts)

def setapples(map_array):
    # Description: Creates for every single '7' (aka apple) in the 2D Array a apple variable to control collecting aples
    # Parameters:
    #   - Takes the 2D Array Map of the level
    # Returns: A tuple
    #   - listofapples: contains complex apple variables (Y-hitbox, X-hitbox, tuple of coordinate)
    #   - remaining_apples (apples cannot be collected twice, apple is deleted from this list if collected)

    # Initialize
    listofapples = []
    remaining_apples = []
    # This function gets all '6's in a 2D array map and returns their coordinates as a list of tuples
    apple_coordinates = find_elem_in_2d_coordinates('7', map_array )
    for c in apple_coordinates: # Create variables
        x = c[1]
        y = c[0]
        # Hitboxes
        y = range (y*100, y*100+101)
        x = range (x*100-25, x*100+35)
        # Create tuple variable for remaining
        ges = str(c[0])+ "," +str (c[1])
        remaining_apples.append(ges)
        # Append the apples with their hitboxes and coordinates to listapples
        listofapples.append( (x, y, (c[0],c[1]))  ) # X Hitbox, Y Hitbox, Tuple of coordinates
    return (listofapples, remaining_apples)




def setflags(map_array):
    # Description: Creates for every single '4' (aka flag) in the 2D Array a flag variable to control collecting flags
    # Parameters:
    #   - Takes the 2D Array Map of the level
    # Returns: A tuple
    #   - listofflags: contains complex flags variables (Y-hitbox, X-hitbox, tuple of coordinate)
    #   - remaining_flags (flags cannot be collected twice, flags is deleted from this list if collected)

    # initialize
    listofflags = []
    remaining_flags = []
    # This function gets all '4's in a 2D array map and returns their coordinates as a list of tuples
    flag_coordinates = find_elem_in_2d_coordinates('4', map_array )
    # Sorts flags in a specific order:
    # Probably redundant as we dont want players to skip flags and programmed it that even if you skip (jump over) the first flag,
    # the second one will lead to the lesson-part of the game and to continue the game you have to run back to the first,
    # as only the second COLLECTED flag leads to the new level.
    flag_coordinates.sort(key=lambda tup: tup[1])
    # i is to append a number to each flag. Probably redundant as well (reason see lines above)
    i = 0
    for c in flag_coordinates:
        # Create Hitboxes of flags
        y = range (c[0]*100, c[0]*100+101)
        x = range (c[1]*100, c[1]*100+100)
        # Create variable for remaining flags (to collect)
        remaining_flags.append( (c[0], c[1]) )
        listofflags.append((x, y, (c[0],c[1]), i)) # X Hitbox, Y Hitbox, tuple of coordinates, number of flag
        i += 1 # count up to give each flag a different number

    return (listofflags, remaining_flags)




def find_elem_in_2d_coordinates(elem, list2D):
    # Description: Gives all "elements" (e.g. '3') in a list back
    # Parameters:
    #  - the element we look for
    #  - the 2D map we look in
    # Returns: a list of tuples with coordinates of all elements

    # Initialize
    lss = list(enumerate(list2D)) # Creates a list of tuples containing: (Number of horizontal line (Y-Coordinate), Line itself)
    ls = []
    result = []
    # Next part checks if an element is in a line, so later we only go through lines actually containing an element
    for a in lss:
        if elem in a[1]:
            ls.append((a[0], list(enumerate(a[1])))) # appending a line in which the element occurs

    # For all lines in which we found an element we look for that element and append a tuple of an element's coordinates to the return value
    for c in ls: # For every Line
        for d in c[1]: # For every Element in the 2nd Index of the tuple (aka map-horizontal-line)
            if d[1] == elem: # if current element is element we look for
                result.append((c[0],d[0])) # Create variable with line-Number (Y-Coordinate) and Index in line (X-Coordinate) and append.
    return result



def textobject (text, font):
    # Description: Creates a textobject
    # Parameters:
    # - Text we want to display
    # - Font we want to use
    # Returns: a surface to write on and the fitting rectangle
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()




######## Render a button with variable parameters ######
def button(msg, x, y ,w, h, ic, ac, action=None, smallF=False):
    # Description: Creates a button for rendering/blitting and offer action
    # Buttons just assign True/False to booleans (if boolean: in gameloop).
    # If true something is displayed (scoreboard/endscreen/startscreen) or music pauses/plays.

    # Parameters:
    # - Displayed Message written on the button
    # - X Coordinate (top left Corner)
    # - Y Coordinate (top left Corner)
    # - width of button
    # - height of button
    # - inactive coulour (when button is not hoovering over the utton)
    # - active colour
    # - action type (what happens if you click the button)

    # Returns: nothing


    # Access to global variables needed for button action
    global Music_paused
    global endgamebool
    global scorebool
    global starterbool
    global playerHP
    global buttonreload
    global displayInventarButton

    # Bind in mouse clicks
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x +  w > mouse[0]  > x and y + h > mouse[1] > y: # Mouse coordinates checking.
         pygame.draw.rect(screen , ac, (x, y, w, h) ) # Draws a rectangle if mouse is hoovering over button (active color)
         if click[0] == 1 and action != None and buttonreload == 0: # Left click & button has a purpose (action)
             buttonreload = 25
             if action == "music":  # Music button - if music if off, turn it on & vice versa
                 if Music_paused == False:
                     pygame.mixer.music.pause()
                     Music_paused = True
                 elif Music_paused == True:
                     pygame.mixer.music.unpause()
                     Music_paused = False
             if action == "endgame_continue":   # Button allows player to continue playing after reaching the endscreen
                                                # Can be deleted probably. If the game is over it's over. (but in case you want to collect all coins of the last level...)
                 if endgamebool == True:
                     endgamebool = False
                 else:
                     endgamebool = True
             if action == "score": # Display Scoreboard during the game
                 if scorebool == True:
                    scorebool = False
                 else:
                     scorebool = True
             if action == "start": # Display starting screen
                 starterbool = False
             if action == "Apfel":
                 displayInvMessage("Du hast einen Apfel gegessen! +1HP")
                 inventar.remove("Apfel")
                 if playerHP < 3:
                     playerHP +=1
             if action == "Inventar":
                 displayInventarButton = not displayInventarButton
    else:
         pygame.draw.rect(screen , ic, (x,y,w,h) )# Mouse is not over button, button should still be visible. (in-active color)
    if smallF:
         Text = pygame.font.SysFont("Calibri", 15)
    else:
        Text = pygame.font.Font("FreeSans.ttf",20)

    textSurf, textRect = textobject(msg, Text)
    textRect.center = ( (x+(w/2)), (y+(h/2)) ) # appoint center of the rectangle
    screen.blit(textSurf, textRect) # blitting button to display


def displayInvMessages():
    global invMessage
    drawText(invMessage, font, BLACK, screen, 100,100)

def displayInvMessage(stringtsh):
    global invMessage
    global displayInvCounter
    displayInvCounter = 30
    drawText(stringtsh, font, BLACK, screen, 100,100)
    invMessage = stringtsh

# Changes flag-image (down => up) (if part == "4")
# Deletes coin-images (else Part)
def change_graphic(x,y):
    # Description: changes graphic
    # Parameters: x & y Coordinates of graphic which is supposed to be changed
    # Returns: Nothing

    # global variables to access
    global Music_paused
    global playerHP
    global remaining_hearts
    global remaining_apples
    global remaining_coins
    global levelcounter
    global level1
    global level2
    global level3
    global level4
    global level5
    global level6
    global level7
    global level8
    global coins_collected
    global flag_counter

    # to get current level for checking to change graphics
    if levelcounter == 1:
        level = level1
    elif levelcounter == 2:
        level = level2
    elif levelcounter == 3:
        level = level3
    elif levelcounter == 4:
        level = level4
    elif levelcounter == 5:
        level = level5
    elif levelcounter == 6:
        level = level6
    elif levelcounter == 7:
        level = level7
    elif levelcounter == 8:
        level = level8
    else:
        level = level8



    test = ("%r,%r" % (x,y)) # create string "tuple"
    if test in remaining_coins: # variable in list of string tuples
        remaining_coins.remove(test) # remove coin/hearts/apples/flag from remaining_list
        st1 =  level[x] # Gets horizontal level line
        st2 = st1[0:y] # Gets all characters up to the character which is supposed to be changed.
        if level[x][y] == '3': # if character to change is a coin, change to BLANK
            st3 = st2 + "."
            level[x] = st3 + st1[y+1:len(level[0])] # add rest of the line to make line complete again
            coins_collected +=1 # One coin collected
            if Music_paused == False: # play sound if music is on
                sound_coin.play()

    intX = int(x)
    intY = int(y)
    flagtest = (intX,intY) # Create variable for flag changing
    if flagtest in remaining_flags:
        remaining_flags.remove(flagtest) # delete variable from remaining_list
        # same process as above: get all characters up to the character we want to change, append character
        # we want to change it into, append all characters after the character we want to change
        st1 =  level[x]
        st2 = st1[0:y]
        if level[x][y] == '4': # Flag DOWN
            st3 = st2 + '5' # Flag UP now
            level[x] = st3 + st1[y+1:len(level[0])]
            flag_counter += 1 # in the score collecting a flag == +10 Scorepoints

    # use test variable from before
    if test in remaining_hearts:
        remaining_hearts.remove(test) # delete variable from remaining_list
        # same process as above: get all characters up to the character we want to change, append character
        # we want to change it into, append all characters after the character we want to change
        st1 = level[x]
        st2 = st1[0:y]
        if level[x][y] == '6': # delete heart from the map
            st3 = st2 + '.' # insert blank
            level[x] = st3 + st1[y+1:len(level[0])]
            if playerHP ==3: # if player HP is at max add no additional HP, if its below 3 (1 or 2) add one
                playerHP += 0
            else:
                playerHP += 1

    if test in remaining_apples:
        remaining_apples.remove(test) # delete variable from remaining_list
        # same process as above: get all characters up to the character we want to change, append character
        # we want to change it into, append all characters after the character we want to change
        st1 = level[x]
        st2 = st1[0:y]
        if level[x][y] == '7': # delete heart from the map
            st3 = st2 + '.' # insert blank
            level[x] = st3 + st1[y+1:len(level[0])]
            if len(inventar) < 8: # if player inventar is not full
                inventar.append("Apfel")
                displayInvMessage("Du hast einen Apfel aufgesammelt!")
                displayInvCounter = 25


def checkhitboxes(playerleft, playerbottom):
    # Description: Checks hitbox of player vs coins/flags/hearts/enemies
    # This function very un-efficient as it runs (max) 30 times a second and checks always all lists and tuple ranges...
    # Always works the same way:
    #   Check for every variable in a list if:
        # Player is at the same X & Y Coordinate: if so => Hitbox collision.
        # Return variable (tuple) for change_graphic which decides which kind of element the player collided with and deals with it.

    # Parameters: Playercoordinates as pixels (X/Y)
    # Returns: A tuple
    #   - (0,0) if no hitbox collides
    #   - (x,y) if player ran into another hitbox

    global listcoinlists
    global listhearts
    global listapples
    global listdyinglists
    global listflags
    global remaining_flags
    global currentflags
    global spawnpoint

    # Detection of coins
    for x in listcoinlists:
        if playerleft in x[0]:
            if playerbottom in x[1]:
                return x[2]

    # Detection of flags
    for x in listflags:
        if playerleft in x[0]:
            if playerbottom in x[1]:
                if x[2] in remaining_flags:
                        # Append flag to currentflags so next round (30 per second) of the gameloop the game deals with it.
                        currentflags.append(x[3])
                        #reset spawnpoint to new flag, so player doesnt have to run the same way again and again
                        # listofflags.append((x, y, (c[0],c[1]), i)) # X Hitbox, Y Hitbox, tuple of coordinates, number of flag
                        tuple = x[2]
                        spawnpoint = (tuple[0], tuple[1])

                        return x[2]

    # Detection of hearts
    for x in listhearts:
        if playerleft in x[0]:
            if playerbottom in x[1]:
                return x[2]

    # Detection of apples
    for x in listapples:
        if playerleft in x[0]:
            if playerbottom in x[1]:
                return x[2]

    # Detection of enemies
    for y in listdyinglists:
        if playerleft in y[0]:
            if playerbottom in y[1]:
                dying()
    else:
        return (0,0) # if no hitbox was collided with



def drawText(text, font, color, surface, x, y):
    # We had another function as well which returned a textobject, but this way its easier and saves time (though old function is still used. Could be swapped in the code)

    # Description: Draw a text onto a surface with specific font & colour & with coordinates
    # Parameters: Text, Font, Colour, Surface, X-, Y-Coordinate
    # Returns: Nothing. Blits on screen itself.

    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)



def convertPixelToLevel(x, y):
    # Inefficient funtion. Best solution I got. But a better function than the collision detection function of coins/hearts/enemies,
    # but different from that as walls dont move and are not collectible. Also walls always have the same hitbox. Coins/hearts/enemies differ.

    # Description: Converts Pixel to 2D Array Coordinates
    # Parameters: pixel-coordinates X&Y
    # Returns: 2D-Array-coordinates of the block the pixels are in.
    for levelX in range(LEVELWIDTH): # for entire levelwidth
        for levelY in range(LEVELHEIGHT): # for entire levellength
            tempRect = pygame.Rect(levelX * BLOCKWIDTH, levelY * BLOCKHEIGHT, BLOCKWIDTH, BLOCKHEIGHT) # create rectangle for every block in level
            if tempRect.collidepoint(x, y): # test in which rectangle (aka block) the pixel-coordinates are (e.g. pixel-coordinates are in a wall => return 2D Array coordinates of said wall)
                return (levelX, levelY) # return Coordinates

# Collision detection
# Calculating the distance between player and the nearest wall on X / Y
# If player is faster than the distance, move by distance instead.
def calculateDistance(coord, lines, dir):
    # Description: calculates distance between player and the nearest wall. Is the actual collision algorythm.
    # Parameters:
    #   - coord is the coordinate behind player.left or player.right (depends in which direction we run, so we know in which way to look for walls)
    #   - lines in which we look for walls/collision points
    #   - dir (direction) player is moving (left/right/up/down)
    # Returns: Distance we can travel without hitting a block
    distances = []
    global levelcounter
    global level1
    global level2
    global level3
    global level4
    global level5
    global level6
    global level7
    global level8
    global level

    if levelcounter == 1:
        level = level1
    elif levelcounter == 2:
        level = level2
    elif levelcounter == 3:
        level = level3
    elif levelcounter == 4:
        level = level4
    elif levelcounter == 5:
        level = level5
    elif levelcounter == 6:
        level = level6
    elif levelcounter == 7:
        level = level7
    elif levelcounter == 8:
        level = level8
    else:
        level = level8

    #print "1- PlayerX " +str(player.top / 100)
    #print "2- PlayerY " +str(player.left / 100 +1)

    for line in lines:
        # Which blocks are scanned are dependent on which direction the player is moving in.
        if dir == 'left':
            playerX = convertPixelToLevel(coord, 0)[0] # Convert the player pixel coordinate of his "border" to 2D level coordinates
            for levelX in range(playerX, -1, -1): # Check for every point/block from playerborder to minus one( left border of the screen) to find nearest wall.
                if level[line][levelX] == BLOCK: # HitBox, Player can't move through there.
                    distances.append(levelX * BLOCKWIDTH + BLOCKWIDTH - coord) # append distance to that hitbox (wall) to list
        elif dir == 'right':
            playerX = convertPixelToLevel(coord, 0)[0]# Convert the player pixel coordinate of his "border" to 2D level coordinates
            for levelX in range(playerX, LEVELWIDTH, 1):# Check for every point from playerborder to levelwidth ( right border of the screen) to find nearest wall.
                if level[line][levelX] == BLOCK: # HitBox, Player can't move through there.
                    distances.append(levelX * BLOCKWIDTH - coord) # append distance to that hitbox (wall) to list

        if dir == 'up':
            playerY = convertPixelToLevel(0, coord)[1]# Convert the player pixel coordinate of his "border" to 2D level coordinates
            for levelY in range(playerY, -1, -1):# Check for every point from playerborder to -1 ( top border of the screen) to find nearest wall.
                if level[levelY][line] == BLOCK: # HitBox, Player can't move through there.
                    distances.append(levelY * BLOCKHEIGHT + BLOCKHEIGHT - coord) # append distance to that hitbox (wall) to list
        elif dir == 'down':
            playerY = convertPixelToLevel(0, coord)[1]# Convert the player pixel coordinate of his "border" to 2D level coordinates
            for levelY in range(playerY, LEVELHEIGHT, 1):# Check for every point from playerborder to levelheight ( bottom border of the screen) to find nearest wall.
                if level[levelY][line] == BLOCK:  # HitBox, Player can't move through there.
                    distances.append(levelY * BLOCKHEIGHT - coord) # append distance to that hitbox (wall) to list


    # Depending on the direction the player moves in we check all lines for the distance we actually CAN move.
    if dir == 'left' or dir == 'up':
        desiredValue = -100000 # set very low so we can check for a wall even if it is far away ( going left/up in the array is minus)
    if dir == 'right' or dir == 'down':
        desiredValue = 100000 # set very high so we can check for a wall even if it is far away ( going right/down is plus)
    for value in distances: # We go through all distances to find the shortest distance until we collide if we keep moving left/up/right/down
        if dir == 'left' or dir == 'up':
            if value > desiredValue: # if the distance to the next hitbox is higher (e.g. shorter as we want to move left/up) than the set value to desiredvalue (e.g. as we cant move -100000 and only -10 until we hit a wall)
                desiredValue = value
        elif dir == 'right' or dir == 'down':
            if value < desiredValue: # same goes here as above, but this time we move right/down. Meaning we look for a smaller value to the next wall. (e.g. we cant move +10000 but only +10)
                desiredValue = value
    return desiredValue


def gameprint(text,xx,yy,color,textsize=40, font=pygame.font.get_default_font()):
    # Description: Draws a message onto the screen
    # Parameters:
    #   - Text to be drawn
    #   - X Coordinate
    #   - Y Coordinate
    #   - Colour
    #   - Textsize
    #   - use default font if none is given
    # Returns: Nothing. Blits on the screen itself
   font = pygame.font.SysFont(font,textsize)
   ren = font.render(text,1,color)
   screen.blit(ren, (xx,yy))

def dying():
    # Description: Handles if the player dies. Sets player back to the Startposition.
    # BUG: Doesnt take in account that different levels have different starting positions!
    # (Worked so far though - if different (new) levels are designed where the spawn point is blocked) we would probably need to fix this)

    # Parameters: None
    # Returns: Nothing
    global player
    global playerHP
    global death_counter
    global spawnpoint

    drawText('YOU DIED!', bigfont, RED, screen, 300, 300) # Display Text
    pygame.display.flip()   # blits to screen
    pygame.display.update() # updates screen
    pygame.time.delay(1200) # Stops game for 1,2seconds after the player died.

    #spawnpoint = (x,y)
    spx = spawnpoint[1]
    spy = spawnpoint[0]
    player = pygame.Rect(spx*BLOCKWIDTH, spy*BLOCKHEIGHT-50, PLAYERSIZE, PLAYERSIZE*2) # (Faulty) Startposition of the player

    #Reset Player HP and update death_counter
    playerHP = 3
    death_counter += 1


def blockmove(xblock, yblock, en_dir_U, block_mov, block_movementMAX, speed, coord):
    if block_mov >= block_movementMAX:
        listblocks[coord][2] = False
    if block_mov <= 0:
        listblocks[coord][2] = True
    if listblocks[coord][2] == True:
        listblocks[coord][3] += speed
    else:
        listblocks[coord][3] -= speed

    screen.blit(myimage_block, ((xblock*BLOCKWIDTH)-camerax, (yblock*BLOCKHEIGHT)-cameray-listblocks[coord][3], BLOCKWIDTH, BLOCKHEIGHT))


def enemymove(xblock, yblock, en_dir_L, enemy_mov, enemy_movementMAX, speed, coord):
    global enemyOfBlink
    global enemyBlink
    global blinkCounter

    # Description: Makes the enemy move
    # Parameters:
    #   - X Coordinate of the block the enemy moves from
    #   - Y Coordinate of the block the enemy moves from
    #   - Direction in which he moves (boolean)
    #   - Position (pixel) in which the enemy is now, calculated from the starting position
    #   - Maximum movement range the enemy has
    #   - Speed of the enemy
    #   - Number of enemy (Index in listenemy)
    # Returns: Nothing. Blits on screen itself.
    if enemy_mov == enemy_movementMAX: # Enemy is at turning point.
        listenemies[coord][2]= False # save changed direction in enemy
        en_dir_L = False # change direction for this method (easier to access)
    if enemy_mov == 0: # Turning point at the other end
        listenemies[coord][2] = True # save changed direction in enemy
        en_dir_L = True # change direction for this method (easier to access)
    if en_dir_L == True:
        listenemies[coord][3] += speed # save speed direction of enemy in its list
    if en_dir_L == False:
        listenemies[coord][3] -= speed # save speed direction of enemy in its list

    # Here we could implement another enemy graphic so the graphic turns around as well (as is done with the player)


    if enemyBlink:
        if coord == IndexOfBlink:
            if blinkCounter > 0:
                blinkCounter -=1
                if blinkCounter %6 == 0:
                    if en_dir_L == True: # blit left walking enemy with calculated movement
                        screen.blit(myimage_enemyL, ((xblock*BLOCKWIDTH)-camerax-enemy_mov, (yblock*BLOCKHEIGHT)-cameray, BLOCKWIDTH, BLOCKHEIGHT))
                    else: # blit right walking enemy with calculated movement
                        screen.blit(myimage_enemy, ((xblock*BLOCKWIDTH)-camerax-enemy_mov, (yblock*BLOCKHEIGHT)-cameray, BLOCKWIDTH, BLOCKHEIGHT))
            if blinkCounter == 0:
                enemyOfBlink = 0
                enemyBlink = False

        else: # Enemy is not the one hit - blitted as usual
            if en_dir_L == True: # blit left walking enemy with calculated movement
                screen.blit(myimage_enemyL, ((xblock*BLOCKWIDTH)-camerax-enemy_mov, (yblock*BLOCKHEIGHT)-cameray, BLOCKWIDTH, BLOCKHEIGHT))
            else: # blit right walking enemy with calculated movement
                screen.blit(myimage_enemy, ((xblock*BLOCKWIDTH)-camerax-enemy_mov, (yblock*BLOCKHEIGHT)-cameray, BLOCKWIDTH, BLOCKHEIGHT))
    # No hit enemy
    else:
        if en_dir_L == True: # blit left walking enemy with calculated movement
            screen.blit(myimage_enemyL, ((xblock*BLOCKWIDTH)-camerax-enemy_mov, (yblock*BLOCKHEIGHT)-cameray, BLOCKWIDTH, BLOCKHEIGHT))
        else: # blit right walking enemy with calculated movement
            screen.blit(myimage_enemy, ((xblock*BLOCKWIDTH)-camerax-enemy_mov, (yblock*BLOCKHEIGHT)-cameray, BLOCKWIDTH, BLOCKHEIGHT))




def start_communication(levelcount):
    # Description: This function is key for interaction start between the two windows.
    #       Creates a .txt file for interaction
    #       This is a very ugly way of communicating but piping didnt work somehow. (+time issue of the project - took me 4 hours trying to get it done by piping between the subprocess and the main process... didnt work out)
    # Parameters: levelcount (current level)
    # Returns: Nothing. Writes in a textfile.

    comm_file = open("communication_file.txt","w") # create new file or overwrite old one


    if levelcount == 1:
        if len(remaining_flags) == 2:
            number = -1
            comm_file.write(str(number)+"\nrunning") # write into file
        if len(remaining_flags) == 1:
            number = 1 # Lesson Number which is supposed to be loaded in the coding window.
            comm_file.write(str(number)+"\nrunning") # write into file

    elif levelcount == 2:
        number = 5# Lesson Number which is supposed to be loaded in the coding window.
        comm_file.write(str(number)+"\nrunning") # write into file

    elif levelcount == 3:
        number = 8# Lesson Number which is supposed to be loaded in the coding window.
        comm_file.write(str(number)+"\nrunning") # write into

    elif levelcount == 4:
        number = 12
        comm_file.write(str(number)+"\nrunning")

    elif levelcount == 5:
        number = 14# Lesson Number which is supposed to be loaded in the coding window.
        comm_file.write(str(number)+"\nrunning") # write into file

    elif levelcount == 6:
        number = 18# Lesson Number which is supposed to be loaded in the coding window.
        comm_file.write(str(number)+"\nrunning") # write into file

    elif levelcount == 7:
        number = 21
        comm_file.write(str(number)+"\nrunning") # write into file

    elif levelcount == 8:
        number = 23
        comm_file.write(str(number)+"\nrunning") # write into file

    comm_file.close() # close file channel



def check_communication():
    # Description: This functon checks the .txt file each gameloop run if it was emptied by the 2nd window (which happens when the 2nd window closes).
    #   It also delays the game by 1 second down to 1 run of the gameloop per second. Stopping the game Window completely while the user coded lead
    #   to a crash of Python as Python assumed it crashed because the programm didnt answer anymore.
    # Parameters: None
    # Returns: Nothing.

    comm_file = open("communication_file.txt","r")
    communication = [x.strip('\n') for x in comm_file.readlines()]
    comm_file.close()
    if communication != []:
        if communication[1] == "running":
        # Stop time for a second each round (30 FPS usually), does not stop Game completely (lead to a crash usually)
            time.sleep(1)
    if communication == "":
        pass



def addToInventar(object):
    global inventar
    if len(inventar) != 8:
        inventar.append(object)
        return True
    else:
        displayInvMessages("Inventar voll!")
        return False

def displayInventar():
    global inventar
    if levelcounter >= 4:
        drawText("Inventar", smallfont, BLACK, screen, 10, 70)
        yax = 70
        for elementstr in inventar:
            yax += 30
            button(elementstr, 25, yax ,50, 20, WHITE, RED,action=elementstr, smallF=True)
    else:
        drawText("Wir haben noch kein Inventar implementiert!", font, BLACK, screen, 10, 70)






def attack():
    global shotFromPlayer
    global shotXCoord
    global shotYCoord
    global player
    global shot
    global shotdir
    global shotdirF

    if shotdir == "R":
        shotXCoord = player.left
        shotYCoord = player.top
    else:
        shotXCoord = player.left-50
        shotYCoord = player.top

    shot = True
    shotdirF = shotdir

    # create graphic from play in walking direction moving

def displayAttack():
    global shotMove
    global shotXCoord
    global shotYCoord
    global shotdir
    global shot
    global shotdirF

    shotMove += 5

    if shotMove >= 300:
        shotMove = 0
        shot = False
        shotXCoord = 0
        shotYCoord = 0
        #shotdir = "R"
        #shotdirF = "R"

    if shotdirF == "L":
        screen.blit(myimage_fireL, (shotXCoord-camerax-shotMove, shotYCoord-cameray, 100, 100))
    elif shotdirF == "R":
        screen.blit(myimage_fireR, (shotXCoord-camerax+shotMove, shotYCoord-cameray, 100, 100))


######### SETTING PLAYER VARIABLES #########
global player
player = pygame.Rect(10*BLOCKWIDTH, 12*BLOCKHEIGHT - 300, PLAYERSIZE, PLAYERSIZE*2) # Initialize Startposition of the player (deprecated probably.. we set this in prepare_level() again

# Acceleration, Speed along the X/Y axis and Jumping. Set to zero/false at the beginning => No movement.
accelX = 0
playerSpeedX = 0
playerSpeedY = 0
jumping = False


######### SETTING GAME VARIABLES #########
camerax = player.centerx-(WINDOWWIDTH/2)
cameray = player.centery-(WINDOWHEIGHT/2)
# Music Mixer Variable. False if music in On.
Music_paused = False
# Load Sounds
sound_coin = pygame.mixer.Sound("sounds/coin.wav") # collecting coin
sound_coin.set_volume(0.2) # set low volume
sound_flag = pygame.mixer.Sound("sounds/flag.wav") # reaching flag
sound_flag.set_volume(0.2) # set low volume
# Fixes the bug that game starts with 1FPS if game crashes without resetting the communication file as it empties the file when the game is started
comm_file = open("communication_file.txt","w") # create new file
comm_file.write("")
comm_file.close()

endRect = pygame.Rect(0, 0, 900, 650) # Rectangle for the end-Screen
endgamebool = False # whether the game ended and end-screen should be displayed
scorebool = False # whether the score-board is shown (changes by pressing a button)



#-------------------------------------------------------------
# Initializing
#-------------------------------------------------------------


save_file = open("saveLevel.txt","r")
saverr = [x.strip('\n') for x in save_file.readlines()]
levelcounter = int(saverr[0])
save_file.close()
if (levelcounter < 1) or  (levelcounter >= 9):
    levelcounter = 1
    save_file = open("saveLevel.txt","w")
    save_file.write(str(levelcounter)+"\nsavedAt")
    save_file.close()


shotMove = 0
shot = False
shotXCoord = 0
shotYCoord = 0
shotdir = "R"
shotdirF = "R"

hitenemy = False
rowsToCheck2 = []
cooldown = 40
enemyWasHit = False
deadEnemy = 0

prepare_level(levelcounter)
#-------------------------------------------------------------
# THE GAME LOOP
#-------------------------------------------------------------





#screen.blit(myimage_enemy, ((xblock*BLOCKWIDTH)-camerax-enemy_mov, (yblock*BLOCKHEIGHT)-cameray, BLOCKWIDTH, BLOCKHEIGHT))
    # detect collection with wall/enemy => dissapear, enemy HP -1

    # enemy blinking.

#def recognizeAttack:
#    if


while True:
    if levelcounter == 1:
        handleRandomCounters(level1)
    elif levelcounter == 2:
        handleRandomCounters(level2)
    elif levelcounter == 3:
        handleRandomCounters(level3)
    elif levelcounter == 4:
        handleRandomCounters(level4)
    elif levelcounter == 5:
        handleRandomCounters(level5)
    elif levelcounter == 6:
        handleRandomCounters(level6)
    elif levelcounter == 7:
        handleRandomCounters(level7)
    elif levelcounter == 8:
        handleRandomCounters(level8)


    if buttonreload > 0:
        buttonreload -= 1

    if levelcounter == 1:
        if len(remaining_flags) > 2:
            JUMPMOD = 0.5
        else:
            JUMPMOD = 3.5
    else:
        JUMPMOD = 3.5

############ COMMUNICATION #############

#_____________ Coding Window Check _____________#
    check_communication() # Checks if Lesson-Window is running
#_____________ Key Input Handling  _______________#
    # These lines check if an event happened (event = quitting the game or pressing a button)
    for event in pygame.event.get():
        if event.type == QUIT or\
        (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit() # Fixes the bug that pygame takes up space in the RAM when game is just closed by sys.exit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == JUMP and not jumping:
                jumping = True
        if event.type == KEYUP:
            if event.key == ATTACK:
                if levelcounter >= 3:
                    if shot != True:
                        attack()
            if event.key == JUMP:
                jumping = False # jumps until either spacebar is not pressed anymore or calculated jump height maximum is reached
            if event.key == MUSIC:
                if eventMusic != 0:
                    if Music_paused == False:
                        pygame.mixer.music.pause()
                        Music_paused = True
                        eventMusic = 20
                    else:
                        pygame.mixer.music.unpause()
                        Music_paused = False
                        eventMusic = 20

    Xkeys = pygame.key.get_pressed()

    if Xkeys[RIGHT] < Xkeys[LEFT]:
        shotdir = "L"
    if Xkeys[RIGHT] > Xkeys[LEFT]:
        shotdir = "R"

############# CHARACTER MOVEMENT #################
#_____________ Jump Acceleration Calculation _____________#
    if not jumping:
        accelX = (Xkeys[RIGHT] - Xkeys[LEFT]) * PLAYERACCEL # acceleration left/right, depending on which is pressed longer
    elif jumping:
        accelX = (Xkeys[RIGHT] - Xkeys[LEFT]) * AIRACCEL # acceleration upwards added

#_____________ Movement Calculation X-Axis _____________#
    # Accelerate the player towards the maximum speed
    if accelX != 0:
        if playerSpeedX <= MAXSPEED and playerSpeedX >= -MAXSPEED: # Maxspeed is the same for moving right and left
            playerSpeedX += accelX # speed+acceleation if speed is not maxxed
            # if speed is above maximum, set speed to maximum
            if playerSpeedX > MAXSPEED:
                playerSpeedX = MAXSPEED
            if playerSpeedX < -MAXSPEED:
                playerSpeedX = -MAXSPEED
    # Deaccelerate the player when no keys are pressed
    if accelX == 0:
        if playerSpeedX > 0:
            playerSpeedX -= PLAYERDEACCEL
            if playerSpeedX < 0:
                playerSpeedX = 0
        if playerSpeedX < 0:
            playerSpeedX += PLAYERDEACCEL
            if playerSpeedX > 0:
                playerSpeedX = 0

#__________________Collision Detection X-Axis______________#

    # The player moves over several rows when he runs.
    # We want to find out which ones we have to check for HitBoxes. (== BLOCK)
    rowsToCheck = []
    # The for loop appends all rows in which the player is moving (e.g. can be moving in two if he is between two)
    for y in range(LEVELHEIGHT):
        if player.colliderect(pygame.Rect(0, y*BLOCKHEIGHT, LEVELWIDTH*BLOCKWIDTH, BLOCKHEIGHT)):
            rowsToCheck.append(y)

    # The calculateDistance() function needs to know which way the player is moving
    if playerSpeedX < 0: # moves left (array counting!)
        minXDistance = calculateDistance(player.left, rowsToCheck, 'left')
    elif playerSpeedX > 0: # moves right (array counting!)
        minXDistance = calculateDistance(player.right, rowsToCheck, 'right')
    else:
        minXDistance = 0


#____________ Character Movement X-axis ____________#

    # If the player's speed is bigger than the distance to the next Hitbox(wall in this case) he can only move up to the wall.
    # If the player's speed is smaller than the distance to the next Hitbox (wall in this case) he can move by that speed/distance
    if playerSpeedX < 0: # moving left
        if minXDistance > playerSpeedX:
            player.left += minXDistance
            playerSpeedX = 0 # Player is standing in front of a Hitbox(wall) now
        else:
            player.left += playerSpeedX # player can move freely
    elif playerSpeedX > 0: # moving right
        if minXDistance < playerSpeedX:
            player.left += minXDistance
            playerSpeedX = 0 # Player is standing in front of a Hitbox(wall) now
        else:
            player.left += playerSpeedX # player can move freely

#_____________ Movement Calculation Y-axis _____________#

    if jumping and playerSpeedY == 0: # Player is at the "top" of the jump
        playerSpeedY -= JUMPACCEL

    # Gravity is decreased while jumping so the player can control
    # the height of his jump.
    if jumping:
        playerSpeedY += FALLACCEL - JUMPMOD
    else:
        playerSpeedY += FALLACCEL

    # Player cannot fall faster than maxfallspeed. (physics: 9.81 m/s while calculating friction, added speed & drag of the body)
    if playerSpeedY > MAXFALLSPEED:
        playerSpeedY = MAXFALLSPEED

#_______________ Collision Detection Y-Axis _____________#

    # Collision detection for the Y-Axis, see above in X-axis movement to understand the process
    columnsToCheck = []
    for x in range(LEVELWIDTH):
        if player.colliderect(pygame.Rect(x*BLOCKWIDTH, 0, BLOCKWIDTH, LEVELHEIGHT*BLOCKHEIGHT)):
            columnsToCheck.append(x)

    if playerSpeedY < 0:
        minYDistance = calculateDistance(player.top, columnsToCheck, 'up')
    elif playerSpeedY > 0:
        minYDistance = calculateDistance(player.bottom, columnsToCheck, 'down')
    else:
        minYDistance = 0

#____________ Character Movement Y-Axis ____________#
    if playerSpeedY < 0:
        if minYDistance > playerSpeedY:
            player.bottom += minYDistance
            playerSpeedY = -1
        else:
            player.bottom += playerSpeedY
    elif playerSpeedY > 0:
        if minYDistance < playerSpeedY:
            player.bottom += minYDistance
            playerSpeedY = 0
        else:
            player.bottom += playerSpeedY


########### CAMERA MOVEMENT ###########

    camerax = player.centerx  - WINDOWWIDTH/2
    cameray = player.centery  - WINDOWHEIGHT/2

    # This keeps the camera within the boundaries of the level.
    # If the camera would usually show space behind the wall of a level we set the camera movement back to show only inside the level boundaries
    cameraRect = pygame.Rect(camerax, cameray, WINDOWWIDTH, WINDOWHEIGHT) # Make a rectangle for the camera
    # This part is for the X-Axis
    if cameraRect.right > LEVELWIDTH*BLOCKWIDTH: # check if camera would show something outside the level in the next gameloop
        camerax = (LEVELWIDTH*BLOCKWIDTH)-WINDOWWIDTH # Set camera to normal (not outside level)
    elif cameraRect.left < 0:# check if camera would show something outside the level in the next gameloop
        camerax = 0 # Set camera normally (not outside level)
    # This Part is for the Y-Axis
    if cameraRect.top < 0: # check if camera would show something outside the level in the next gameloop
        cameray = 0 # Set camera to normal (not outside level)
    elif cameraRect.bottom > LEVELHEIGHT*BLOCKHEIGHT: # check if camera would show something outside the level in the next gameloop
        cameray = (LEVELHEIGHT*BLOCKHEIGHT)-WINDOWHEIGHT# Set camera normally (not outside level)


################# RENDERING ###################

#____________ Level Environment Rendering ____________#

    # The active area makes sure only blocks far away from the screen (camera) are not rendered
    activeArea = pygame.Rect(camerax-BLOCKWIDTH, cameray-BLOCKHEIGHT, WINDOWWIDTH+(200), WINDOWHEIGHT+(200))

    screen.blit(background_image, [0, 0]) # blit background - global variable which has been set in prepare_level()


    for y in range(LEVELHEIGHT):
        for x in range(LEVELWIDTH):
            if activeArea.collidepoint((x*BLOCKWIDTH), (y*BLOCKHEIGHT)): # If in activeArea (supposed to be rendered) do this:
                if level[y][x] == BLANK:
                    continue
                if level[y][x] == HEART:
                    screen.blit(myimage_heart, ((x*BLOCKWIDTH)-camerax, (y*BLOCKHEIGHT)- cameray, BLOCKWIDTH, BLOCKHEIGHT))
                if level[y][x] == APPLE:
                    screen.blit(myimage_apple, ((x*BLOCKWIDTH)-camerax, (y*BLOCKHEIGHT)- cameray, BLOCKWIDTH, BLOCKHEIGHT))
                if level[y][x] == KILL:
                    screen.blit(myimage_kill, ((x*BLOCKWIDTH)-camerax, (y*BLOCKHEIGHT)- cameray, BLOCKWIDTH, BLOCKHEIGHT))
                if level [y][x] == COIN:
                    screen.blit(myimage_coin, ((x*BLOCKWIDTH)-camerax, (y*BLOCKHEIGHT)- cameray, BLOCKWIDTH, BLOCKHEIGHT))
                if level [y][x] == FLAGDOWN:
                    screen.blit(myimage_flagdown, ((x*BLOCKWIDTH)-camerax, (y*BLOCKHEIGHT)- cameray, BLOCKWIDTH, BLOCKHEIGHT))
                if level [y][x] == FLAGUP:
                    screen.blit(myimage_flagup, ((x*BLOCKWIDTH)-camerax, (y*BLOCKHEIGHT)- cameray, BLOCKWIDTH, BLOCKHEIGHT))
                if level[y][x] == BLOCK:
                    if level[y-1][x] == BLOCK:
                        screen.blit (myimage_wall2, ((x*BLOCKWIDTH) - camerax, (y*BLOCKHEIGHT) - cameray, BLOCKWIDTH, BLOCKHEIGHT))
                    else:
                        screen.blit (myimage_wall, ((x*BLOCKWIDTH) - camerax, (y*BLOCKHEIGHT) - cameray, BLOCKWIDTH, BLOCKHEIGHT))


#____________ Enemy Rendering ____________#

    # Move all enemies in the list of the level
    for x in listenemies:
        enemymove(x[0],x[1],x[2],x[3],x[4],x[5],listenemies.index(x))

    for x in listblocks:
        blockmove(x[0],x[1],x[2],x[3],x[4],x[5],listblocks.index(x))
#____________ Character Rendering ____________#

    # Character movement -  images being drawn
    # The " - camerax/y" part makes sure that even if the camera cant move anymore (player is near boundary of the level) the player can move up to the outer wall
    # If the player has been hit and the cooldown is on, player should "blink"
    if levelcounter >= 3:
        if hitenemy and cooldown != 0:
            if cooldown %6 == 0:
                if Xkeys[RIGHT] < Xkeys[LEFT]:
                    screen.blit(myimage_left_w, (player.left - camerax, player.top - cameray, PLAYERSIZE, PLAYERSIZE*2))
                elif Xkeys[LEFT] < Xkeys[RIGHT]:
                    screen.blit(myimage_right_w, (player.left - camerax, player.top - cameray, PLAYERSIZE, PLAYERSIZE*2))
                elif jumping == True:
                    screen.blit(myimage_jump_w, (player.left - camerax, player.top - cameray, PLAYERSIZE, PLAYERSIZE*2))
                else:
                    screen.blit(myimage_stand_w, (player.left - camerax, player.top - cameray, PLAYERSIZE, PLAYERSIZE*2))
        else:
            if Xkeys[RIGHT] < Xkeys[LEFT]:
                screen.blit(myimage_left_w, (player.left - camerax, player.top - cameray, PLAYERSIZE, PLAYERSIZE*2))
            elif Xkeys[LEFT] < Xkeys[RIGHT]:
                screen.blit(myimage_right_w, (player.left - camerax, player.top - cameray, PLAYERSIZE, PLAYERSIZE*2))
            elif jumping == True:
                screen.blit(myimage_jump_w, (player.left - camerax, player.top - cameray, PLAYERSIZE, PLAYERSIZE*2))
            else:
                screen.blit(myimage_stand_w, (player.left - camerax, player.top - cameray, PLAYERSIZE, PLAYERSIZE*2))
    else:
        if hitenemy and cooldown != 0:
            if cooldown %6 == 0:
                if Xkeys[RIGHT] < Xkeys[LEFT]:
                    screen.blit(myimage_left, (player.left - camerax, player.top - cameray, PLAYERSIZE, PLAYERSIZE*2))
                elif Xkeys[LEFT] < Xkeys[RIGHT]:
                    screen.blit(myimage_right, (player.left - camerax, player.top - cameray, PLAYERSIZE, PLAYERSIZE*2))
                elif jumping == True:
                    screen.blit(myimage_jump, (player.left - camerax, player.top - cameray, PLAYERSIZE, PLAYERSIZE*2))
                else:
                    screen.blit(myimage_stand, (player.left - camerax, player.top - cameray, PLAYERSIZE, PLAYERSIZE*2))
        else:
            if Xkeys[RIGHT] < Xkeys[LEFT]:
                screen.blit(myimage_left, (player.left - camerax, player.top - cameray, PLAYERSIZE, PLAYERSIZE*2))
            elif Xkeys[LEFT] < Xkeys[RIGHT]:
                screen.blit(myimage_right, (player.left - camerax, player.top - cameray, PLAYERSIZE, PLAYERSIZE*2))
            elif jumping == True:
                screen.blit(myimage_jump, (player.left - camerax, player.top - cameray, PLAYERSIZE, PLAYERSIZE*2))
            else:
                screen.blit(myimage_stand, (player.left - camerax, player.top - cameray, PLAYERSIZE, PLAYERSIZE*2))



#____________ Button Rendering ____________#

    # Display music button with different Text, depending on whether the music is playing or not. )
    if Music_paused == True:
        button("Music off", 810,0,90,30 ,GREEN, LIGHTGREEN , "music")
    else:
        button("Music on", 810,0,90,30 ,GREEN, LIGHTGREEN , "music")
    # InGame Score Board Button
    button("Score", 810,620,90,30 ,GREEN, LIGHTGREEN , "score")


#____________ HP & Coin Counter Rendering ____________#

    # Display the coin counter (image + actualy number)
    screen.blit(myimage_coinCounter, pygame.rect.Rect(0,0, 100,38 ))
    drawText('%r' %(coins_collected), font, WHITE, screen, 80, 5)

    # Display hearts depending on how many HP the player has left
    if playerHP == 1:
        screen.blit(myimage_hp, pygame.rect.Rect(150,0, 37,33 ))
    if playerHP == 2:
        screen.blit(myimage_hp, pygame.rect.Rect(150,0, 37,33 ))
        screen.blit(myimage_hp, pygame.rect.Rect(200,0, 37,33 ))
    if playerHP == 3:
        screen.blit(myimage_hp, pygame.rect.Rect(150,0, 37,33 ))
        screen.blit(myimage_hp, pygame.rect.Rect(200,0, 37,33 ))
        screen.blit(myimage_hp, pygame.rect.Rect(250,0, 37,33 ))



####### HITBOX CALCULATIONS #########


#____________ Collision detection of hearts/apples/coins/flags/barbs ____________#
    # Checking for hitboxes of hearts/apples/coins/flags/barbs
    coinTuple =  checkhitboxes (player.left, player.bottom)

    # Following first line acted as a safety net - in case checkhitboxes didnt return anything.
    # Fixed old bug. Probably deprecated, as checkhitboxes now ALWAYS returns something. (in case no hitbox was found it reutrn (0,0)
    if isinstance(coinTuple, tuple):
        if coinTuple != (0,0): # if (0,0) => no hitbox found.
            change_graphic(coinTuple[0],coinTuple[1])


#____________ Collision detection of enemies ____________#


    if not hitenemy:

        for x in listenemies:

        # shot collision detection with enemy:
            if shot== True:
                # right side
                if shotdirF == "R" and (shotXCoord-camerax+shotMove) in range ((x[0]*BLOCKWIDTH)-camerax-x[3]-70, (x[0]*BLOCKWIDTH)-camerax-x[3]):
                    if (shotYCoord-cameray) in range ((x[1]*BLOCKHEIGHT)-cameray-100,(x[1]*BLOCKHEIGHT)-cameray+100):
                        shotMove = 0
                        shot = False
                        shotXCoord = 0
                        shotYCoord = 0
                        enemyWasHit = True
                        enemyBlink = True
                        IndexOfBlink = listenemies.index(x)
                        blinkCounter = 30

                        x[7] -= 1
                        if x[7] == 0:
                            deadEnemy = listenemies.index(x)

                # left side
                if shotdirF == "L" and (shotXCoord-camerax-shotMove) in range ((x[0]*BLOCKWIDTH)-camerax-x[3]-50, (x[0]*BLOCKWIDTH)-camerax-x[3]+20):# X Axis
                    if (shotYCoord-cameray) in range ((x[1]*BLOCKHEIGHT)-cameray-100,(x[1]*BLOCKHEIGHT)-cameray+100 ):# Y Axis
                        shotMove = 0
                        shot = False
                        shotXCoord = 0
                        shotYCoord = 0
                        enemyWasHit = True
                        enemyBlink = True
                        IndexOfBlink = listenemies.index(x)
                        blinkCounter = 30

                        x[7] -= 1
                        if x[7] == 0:
                            deadEnemy = listenemies.index(x)


    # Left side collision detection character with an enemy:
            if (player.left - camerax) in range ((x[0]*BLOCKWIDTH)-camerax-x[3], (x[0]*BLOCKWIDTH)-camerax-x[3]+50): # X Axis
                if (player.top - cameray) in range ((x[1]*BLOCKHEIGHT)-cameray-100,(x[1]*BLOCKHEIGHT)-cameray+100): # Y Axis
                    playerHP -= 1
                    if coins_collected != 0:
                        coins_collected -= 1
                    if playerHP == 0:
                        dying()
                    else:
                        hitenemy = True

                        rowsToCheck2 = []
    # The for loop appends all rows in which the player is moving (e.g. can be moving in two if he is between two)
                        for y in range(LEVELHEIGHT):
                            if player.colliderect(pygame.Rect(0, y*BLOCKHEIGHT, LEVELWIDTH*BLOCKWIDTH, BLOCKHEIGHT)):
                                rowsToCheck2.append(y)

                        minXDistance2 = calculateDistance(player.left, rowsToCheck, 'right')
                        if minXDistance2 >= 100:
                            player.left += 100


    # Right side collision detection with an enemy:
            if (player.right - camerax) in range ((x[0]*BLOCKWIDTH)-camerax-x[3], (x[0]*BLOCKWIDTH)-camerax-x[3]+50):# X Axis
                if (player.top - cameray) in range ((x[1]*BLOCKHEIGHT)-cameray-100,(x[1]*BLOCKHEIGHT)-cameray+100 ):# Y Axis
                    playerHP -= 1
                    if coins_collected != 0:
                        coins_collected -= 1
                    if playerHP == 0:
                        dying()
                    else:
                        hitenemy = True

                        rowsToCheck2 = []
    # The for loop appends all rows in which the player is moving (e.g. can be moving in two if he is between two)
                        for y in range(LEVELHEIGHT):
                            if player.colliderect(pygame.Rect(0, y*BLOCKHEIGHT, LEVELWIDTH*BLOCKWIDTH, BLOCKHEIGHT)):
                                rowsToCheck2.append(y)

    # The calculateDistance() function needs to know which way the player is moving

                        minXDistance2 = calculateDistance(player.left, rowsToCheck, 'left')

                        if minXDistance2 <= -100:
                            player.left -= 100



    if hitenemy:
        if cooldown == 0:
            for x in listenemies:
            # Left side collision detection with an enemy:
                if (player.left - camerax) in range ((x[0]*BLOCKWIDTH)-camerax-x[3], (x[0]*BLOCKWIDTH)-camerax-x[3]+50): # X Axis
                    if (player.top - cameray) in range ((x[1]*BLOCKHEIGHT)-cameray-100,(x[1]*BLOCKHEIGHT)-cameray+100): # Y Axis
                        cooldown = 40
            # Right side collision detection with an enemy:
                elif (player.right - camerax) in range ((x[0]*BLOCKWIDTH)-camerax-x[3], (x[0]*BLOCKWIDTH)-camerax-x[3]+50):# X Axis
                    if (player.top - cameray) in range ((x[1]*BLOCKHEIGHT)-cameray-100,(x[1]*BLOCKHEIGHT)-cameray+100 ):# Y Axis
                        cooldown = 40
            if cooldown == 0:
                hitenemy = False
                cooldown = 40
        else:
            cooldown -= 1




    if not hitenemy:
        for x in listblocks:
            if (player.right - camerax) in range ((x[0]*BLOCKWIDTH)-camerax, (x[0]*BLOCKWIDTH)-camerax+150): #X Axis
                 if (player.top - cameray) in range ((x[1]*BLOCKHEIGHT)-cameray-x[3],(x[1]*BLOCKHEIGHT)-cameray-x[3]+190):# Y Axis
                    hitenemy = True
                    cooldown = 40
                    playerHP -= 1
                    if playerHP == 0:
                        dying()
                    else:
                        hitenemy = True

                    rowsToCheck2 = []
    # The for loop appends all rows in which the player is moving (e.g. can be moving in two if he is between two)
                    for y in range(LEVELHEIGHT):
                        if player.colliderect(pygame.Rect(0, y*BLOCKHEIGHT, LEVELWIDTH*BLOCKWIDTH, BLOCKHEIGHT)):
                            rowsToCheck2.append(y)

    # The calculateDistance() function needs to know which way the player is moving
                    if playerSpeedX >= 0 :
                        minXDistance2 = calculateDistance(player.left, rowsToCheck, 'right')
                        if minXDistance2 >= 100 :
                            player.left -= 100
                        else:
                            player.left -= (minXDistance2 -2)
                    else:
                        minXDistance2 = calculateDistance(player.left, rowsToCheck, 'left')
                        if minXDistance2 <= -100:
                            player.left += 100
                        else:
                            player.left += (minXDistance2 -2)
    if enemyWasHit:
        if listenemies[deadEnemy][7] == 0:
            listenemies.pop(deadEnemy)
            coins_collected += 10
        enemyWasHit = False

#____________ Flag handling ____________#

    if currentflags != []: # checks if he lately ran into a flag
        if remaining_flags != []: # checks if there is another flag left to collect => if no, next level, if yes => coding lessons
            save_file = open("saveLevel.txt","w")
            save_file.write(str(levelcounter)+"\nsavedAt") # write into file
            save_file.close()

            start_communication(levelcounter)
            # Piping didnt work, but we still need to configure them if we want to compile a .pyc/.pyw file which can run the game without needing to open it with pycharm/via console
            process = Popen(["Python", "python_tk_text.pyc"],stdin=PIPE,stdout=PIPE,stderr=PIPE,shell=False,bufsize= 0)
            currentflags.remove(currentflags[0]) # remove flag from remaining (collected now)

        else:
            currentflags.remove(currentflags[0]) # remove flag from remaining (collected now)
            levelcounter+=1
            save_file = open("saveLevel.txt","w")
            save_file.write(str(levelcounter)+"\nsavedAt") # write into file
            save_file.close()
            if levelcounter == 9:
                endgamebool = True # Enable endscreen
            prepare_level(levelcounter) # load next level


    if shot==True:
        displayAttack()


    button("Inventar", 700,0,90,30 ,GREEN, LIGHTGREEN , "Inventar")

    if displayInventarButton:
        displayInventar()

    if displayInvCounter > 0:
        displayInvMessages()
        displayInvCounter -= 1



############ FIXED SCREEN RENDERING #############


#____________ Endscreen ____________#

    if endgamebool: # Display endscreen
        screen.blit(myimage_endscreen, endRect)
        drawText('Eingesammelte Muenzen:  %i' %(coins_collected), font, BLACK, screen, 120, 320)
        drawText('Flaggen erreicht:  %i' %(flag_counter), font, BLACK, screen, 520, 320)
        drawText('Anzahl Tode:  %i' %(death_counter), font, BLACK, screen, 120, 360)
        drawText('_____________________________________________', font, RED, screen, 120, 365)
        drawText('Score:  %i' %(coins_collected+(flag_counter*10)-(death_counter*5)), font, RED, screen, 120, 400)
        button("Weiter", 810,620,90,30 ,GREEN, LIGHTGREEN , "endgame_continue")

#____________ Scoreboard ____________#

    if scorebool: # Display InGame score board
        screen.blit(myimage_score, endRect)
        drawText('Eingesammelte Muenzen:  %i' %(coins_collected), font, BLACK, screen, 120, 320)
        drawText('Flaggen erreicht:  %i' %(flag_counter), font, BLACK, screen, 520, 320)
        drawText('Anzahl Tode:  %i' %(death_counter), font, BLACK, screen, 120, 360)
        drawText('_____________________________________________', font, RED, screen, 120, 365)
        drawText('Score:  %i' %(coins_collected+(flag_counter*10)-(death_counter*5)), font, RED, screen, 120, 400)
        button("Weiter", 810,620,90,30 ,GREEN, LIGHTGREEN , "score")

#____________ Startscreen ____________#

    if starterbool:# Display starting screen
        screen.blit(myimage_start, endRect)
        button("START", 400,300,150,75 ,BLUE, BLUE , "start")


    if levelcounter == 3  and levelThree <= 150:
        levelThree += 1
        drawText('Wir koennen ab jetzt Gegner mit Zaubern besiegen!', font, RED, screen, 120, 420)
        drawText('Druecke einfach die Taste:  <  a  >' , font, RED, screen, 120, 460)
        drawText('Du zauberst immer in Laufrichtung.' , font, RED, screen, 120, 500)








###### DISPLAY UPDATE #########

    pygame.display.flip() # Update the screen with all things we blitted.
    clock.tick(FPS) # maximum of Gameloop runs is 30 - this function delays the game after the gameloop is done for just enough to get down to about 30FPS.



