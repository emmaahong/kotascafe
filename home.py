import os, sys
import time 
import pygame as pg
from functions import *

pg.init()

def title(screen, location):
    """
	This function is the title screen and checks for next location
	Args
		screen: pygame Surface
        location: str
        mouse: tuple
        x, y: tuple
        bg_title: pygame Image
        event: pygame Event

	Returns
		location: str
        depends on where user chooses to go
	"""
   
    # initializing mouse, dimensions of screen, and background
    mouse = pg.mouse.get_pos()
    x, y = getDim()
    bg_title = setBg('imagesProjec/title.png', x, y, screen)
    
    for event in pg.event.get():
#        pg.display.update()
        
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
       
        elif event.type == pg.MOUSEBUTTONDOWN:

            if (600 <= mouse[0] <= 740) and (280 <= mouse[1] <= 326):
                location = 'lvl1 start'
            
            if 600 <= mouse[0] <= 740 and 350 <= mouse[1] <= 390:
                location = 'help'
                print(location)
            
            elif 600 <= mouse[0] <= 740 and 420 <= mouse[1] <= 460:
                pg.quit()
                sys.exit()

    return location
    
def help(screen, location): 
    """
	This function is the help screen and checks for next location
	Args
		screen: pygame Surface
        location: str
        mouse: tuple
        x, y: tuple
        bg_help: pygame Image
        event: pygame Event

	Returns
		location: str
        depends on where user chooses to go
	"""

    # set background
    x,y = getDim()
    bg_help = setBg('imagesProjec/help_page.png', x, y, screen)

    mouse = pg.mouse.get_pos() # initializing mouse and getting its position
    
    # for every event that occurs
    for event in pg.event.get():

        # if event is quit, stop the program
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        
        # if player clicks on button area, change location
        elif event.type == pg.MOUSEBUTTONDOWN:
     
            if 600<= mouse[0]<=750 and 310 <= mouse[1] <= 360:
                location = 'title'
            
    return location # return location

def startOne(screen, location):
    """
	This function is the start level screen and checks for next location
	Args
		screen: pygame Surface
        location: str
        mouse: tuple
        x, y: tuple
        bg_title: pygame Image
        event: pygame Event

	Returns
		location: str
        depends on where user chooses to go
	"""
    # set background
    x, y = getDim()
    bg_menu1 = setBg('imagesProjec/lvl1_start.png', x, y, screen)

    mouse = pg.mouse.get_pos() # initializing mouse and getting its position

    # for every event that occurs
    for event in pg.event.get():
        
        # if event is quit, stop the program
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
       
        # if player clicks on button area, change location
        elif event.type == pg.MOUSEBUTTONDOWN:
            
            click() # sound effect

            if 474 <= mouse[0] <= 810 and 201 <= mouse[1] <= 254:
                location = 'lvl1'

    return location # return location