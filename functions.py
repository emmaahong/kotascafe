import os, sys
import time 
import pygame as pg

BLUE = (160, 195, 209)
PINK = (235, 213, 207)
YELLOW = (248, 244, 219)
GREEN = (222, 235, 217)
BROWN = (148, 102, 89)
BLACK = (0, 0, 0)
WHITE = (255,255,255)
DARK_RED = (148, 24, 10)


def getDim():
    """
	This function gets the dimensions of the screen.
	Args
		x: int
        y: int
		surface: pygame Surface
	Returns
		x and y, being the dimensions of the screen
	"""
    surface = pg.display.get_surface() # finding surface
    x,y = surface.get_width(), surface.get_height() # finding the x and y values of screen dimensions

    return x, y

def setBg(image, x, y, screen):
    """
	This function loads a background image and blits it onto the screen as the background.
	Args
		bg: pygame image
        x, y: size of the image
        screen: pygame Surface
	Returns
		None
	"""

    bg = pg.image.load(image) # load image
    bg = pg.transform.scale(bg, (x, y)) # scale accordingly
    screen.blit(bg, (0,0)) # blit to whole screen

def print_text(screen,font,x,y,text, size_x, size_y, color = BROWN):
    """
	This function blits text onto the screen.
	Args
		screen: pygame Surface
        font: pygame Font
        text: str
        size_x, size_y: int
        color: tuple
	Returns
		imgText blit onto screen
	"""

    imgText=font.render(text,True,color) # load font
    imgText = pg.transform.scale(imgText, (size_x, size_y)) # scale accordingly
    screen.blit(imgText,(x,y)) # blit to screen

    return imgText

def click():
    """
	This function plays a click sound effect
	AbbazGamez, “Powerup2.” Freesound.
	Args
		soundObj
	Returns
		None
	"""

    soundObj = pg.mixer.Sound('music/click.wav')
    soundObj.play()

def wrongObj():
    """
	This function plays a fault sound effect
	hmmm101, “Pixel Sound Effect #3.” Freesound
	Args
		soundObj
	Returns
		None
	"""

    soundObj = pg.mixer.Sound('music/wrongOrder.wav')
    soundObj.play()

def gameOv():
    """
	This function plays a dying noise
	 HappyParakeet, “Pixel Death.” Freesound.
	Args
		soundObj
	Returns
		None
	"""
    soundObj = pg.mixer.Sound('music/gameOver.wav')
    soundObj.play()

def gameMusic():
    """
	This function plays game background music
	originaljun, “Pixel Flute Melody Loop.” Freesound.
	Args
		soundObj
	Returns
		None
	"""
    soundObj = pg.mixer.Sound("music/gameMusic.wav")
    soundObj.set_volume(0.4)
    soundObj.play(-1)
    
def move(player,event):
	moveDir = 'none'
	# if player clicks 'w, a, s, d' or arrow keys, move player in desired direction
	
	if event.type == pg.KEYDOWN:
		if event.key == pg.K_LEFT or event.key == ord('a'):
			moveDir = 'left'
			
		if event.key == pg.K_RIGHT or event.key == ord('d'):          
			moveDir = 'right'
			
		if event.key == pg.K_UP or event.key == ord('w'):
			moveDir = 'up'
			
		if event.key == pg.K_DOWN or event.key == ord('s'):
			moveDir = 'down'

	# stop if not clicking key anymore
	if event.type == pg.KEYUP:
		moveDir = 'none'
  
	return moveDir