import os, sys
import time 
import pygame as pg
import levels_new as lvl
import home
import sprites
from sprite import Player
from functions import*

# initializing pygame module
pg.init()

# setting default location as the title screen
location = 'title'

# initializing the screen
height = 500
width = 900
screen = pg.display.set_mode((width,height))

# boolean for while game runs
running = True

while running:

    # if the location is title, call the title function
    if location == 'title':
        location = home.title(screen, location)
    
    # if the location is help page, call the help function
    elif location == 'help':
        location = home.help(screen, location)

     # if the location is level 1 start, call the level1 start page function function
    elif location == 'lvl1 start':
        location = home.startOne(screen, location)

     # if the location is level 1, call the level 1 function
    elif location == 'lvl1':
        location = lvl.levelOne(screen, location)

     # if the location is game over, call the title function
    elif location == 'game over':
        location = lvl.gameOver(screen, location)
    
    # updating the display
    pg.display.flip()