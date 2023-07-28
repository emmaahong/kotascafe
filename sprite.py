from calendar import c
import os, sys
import time 
import pygame as pg
from functions import *
import random

class Player(pg.sprite.Sprite):
    def __init__(self, picture_path):
        super(Player, self).__init__()
        """
	    Player class with method that enables movement
	    """
        
        self.image = pg.image.load(picture_path)
        self.imageSize = (50,120)
        self.image = pg.transform.scale(self.image, self.imageSize)

        self.image_left = pg.transform.flip(self.image, True, False)
        self.image_right = self.image
        
        self.rect = self.image.get_rect()

        self.rect.center = (560,215)

        self.movex = 8
        self.movey = 8
        self.frame = 0

    def walk(self, direction):
        """
	    This function allows player movement
	    Args
            direction: str
            self: pygame Sprite
	    Returns
            None
	"""

        if direction == "left": # if the direction chosen is left, move left according to self speed
            self.rect.x = self.rect.x - self.movex
            self.image = self.image_left
        
        elif direction == "right":# if the direction chosen is right, move right according to self speed
            self.rect.x = self.rect.x + self.movex
            self.image = self.image_right
        
        elif direction == "up":# if the direction chosen is up, move up according to self speed
            self.rect.y = self.rect.y - self.movey
           
        elif direction == "down":# if the direction chosen is down, move down according to self speed
            self.rect.y = self.rect.y + self.movey

    
class Customer(pg.sprite.Sprite):
    def __init__(self, cust_num):
        super(Customer, self).__init__()
        """
	Customer class that has methods allowing automatic movement and individual attributes
	    """

        self.coord = [[120, 110], [150, 330]]

        self.number = cust_num

        if self.number == 1:
            self.movex = 10
            self.movey = 10
            self.frame = 0
            self.center = (-50, 120)
            self.image = pg.image.load("imagesProjec/customer1.png")
            self.items = ["Sandwich", "Croissant"]
        
        elif self.number == 2:
            self.movex = 6
            self.movey = 6
            self.frame = 0
            self.center = (-50, 240)
            self.image = pg.image.load("imagesProjec/customer2.png")
            self.items = ["Coffee", "Croissant"]
        
        elif self.number == 3:
            self.movex = 8
            self.movey = 8
            self.frame = 0
            self.center = (-50, 360)
            self.image = pg.image.load("imagesProjec/customer3.png")
            self.items = ["Coffee"]

        self.imageSize = (50, 120)
        self.image = pg.transform.scale(self.image, self.imageSize)

        self.show_anger = False
        self.show_order = True
        self.received = []
        self.hasOrd = False
        self.phase = 0
        
        self.rect = self.image.get_rect()
        self.rect.center = self.center
        
    def update(self):
        """
	This function allows Customer movement
	Args
		self: pygame Sprite
	Returns
		None
	"""
        
        if self.phase == 0: # if customer is supposed to be moving towards cafe

            if self.number == 1: # if customer is type 1, move right until reached spot
                if self.rect.x < 180:
                    self.rect.x = self.rect.x + self.movex
                else:
                        self.phase +=1

            if self.number == 2:# if customer is type 2, move right until reached spot
                if self.rect.x < 220:
                    self.rect.x = self.rect.x + self.movex
                else:
                        self.phase +=1

            if self.number == 3:# if customer is type 3, move right until reached spot
                if self.rect.x < 200:
                    self.rect.x = self.rect.x + self.movex
                else:
                        self.phase +=1

        if self.phase == 2: # if customer is supposed to be leaving, move left until off the screen
            if self.rect.left > -50 :
                self.rect.x = self.rect.x - self.movex

            else: # kill sprite off screen
                self.kill()

