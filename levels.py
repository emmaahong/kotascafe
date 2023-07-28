import os, sys
import pygame as pg
from functions import *
import sprite
from sprite import Player
from sprite import Customer
import random

def levelOne(screen, location):
    """
	This function is the game location and lets the user play the game
	Args
		screen: pygame Surface
        location: str
        mouse: tuple
        x, y: tuple
        bg_lvl1: pygame Image
        event: pygame Event
        steam_anim: list
        steam_framerate: int
        imgIndex: int
        counter: int
        coffee_touch: bool
        croissant_touch: bool
        sandwich_touch: bool
        coffee: bool
        croissant: bool
        sandwich: bool
        quit: bool
        font: pygame Font
        time_left: int
        moveR: bool
        moveL: bool
        moveU: bool
        moveD: bool
        cof_l: int
        cof_r: int
        cof_b: int
        cro_l: int
        cro_t: int
        cro_b: int
        sand_t: int
        all_sprites: pygame Sprite Group
        customers: pygame Sprite Group
        customer_list: list
        current_cust: list
        new_cust_counter: int
        score: int
        player: Player
        border_left: int
        counter_bottom: int
        counter_top_side: int
        counter_low_side: int
        border_top: int
        border_bottom: int
        lastUp: int
        total_mins: int
        total_sec: int
        diff_cust: pygame Sprite
        collide: pygame Sprite
        collide_time: int  

	Returns
		location: str
        depends on where user chooses to go
	"""

    # checking size of screen
    x, y = getDim()

    # loading images and setting background
    bg_lvl1 = setBg('imagesProjec/lvl1.png', x, y, screen)

    gameMusic() # bg music
    
    # initializing variables
    steam_anim = []
    steam_framerate = 60
    imgIndex = 0
    counter = 0
    coffee_touch = False
    croissant_touch = False
    sandwich_touch = False
    coffee = False
    croissant = False
    sandwich = False

    for i in range(5): # loading steam images into list
        steam_img = pg.image.load(os.path.join("gif_frames", f"steam{i}.png")).convert()
        steam_img.set_colorkey(BLACK)
        steam_anim.append(pg.transform.scale(steam_img, (75, 75)))

    # setting booleans for game loop and other
    quit = False

    font = pg.font.SysFont("georgia bold", 30) # initializing font
    time_left = 90 # time remaining for game

    pg.time.set_timer(pg.USEREVENT, 1000) # setting timer
    
    # setting bool values to if player is walking in given direction
    moveR = False
    moveL = False
    moveU = False
    moveD = False

    # setting x and y values for certain boundaries where you can get food
    cof_l = 424
    cof_r = 560
    cof_b = 114

    cro_l = 620
    cro_t = 110
    cro_b = 210

    sand_t = 250
    all_sprites = pg.sprite.Group()
    customers = pg.sprite.Group()
    customer_list = [1,2,3]
    current_cust = []
    new_cust_counter = 0
    score = 0

    # initializing the player
    player = Player('imagesProjec/player.png')

    all_sprites.add(player)
    
    # coordinates for features of the game/borders to prevent player from walking to certain places
    border_left = 210
    counter_bottom = 105
    counter_top_side = 460
    counter_low_side = 646
    border_top = 17
    border_bottom = 434 - player.imageSize[1]

    # game loop
    while not quit:
 
        # checking event queue
        for event in pg.event.get():
           # getting mouse position 
            mouse = pg.mouse.get_pos()  

            if event.type == pg.MOUSEBUTTONDOWN:
                click()

                # if player is in a certain area and clicked in a certain area
                if cof_l < player.rect.x < cof_r:
                    if player.rect.y < cof_b:
                        if (485<mouse[0]<652) and (69 < mouse[1] < 295):
                            
                            # touched coffee machine
                            coffee_touch = True

                            # has coffee
                            coffee = True
                            croissant = False
                            sandwich = False

                            # setting a last update time point 
                            lastUp = pg.time.get_ticks()

                            # blit coffee onto screen
                            print_text(screen, font, 550, 155, "+1 Coffee", 50, 30, color = BLUE)
                
                # if customer is in area where they can get croissant, the customer then has the croissant
                elif player.rect.x > cro_l:
                    if cro_t < player.rect.y < cro_b:
                        if (731<mouse[0]<783) and (170 < mouse[1] < 250):
                            
                            croissant_touch = True
                            croissant = True
                            coffee = False
                            sandwich = False
                            lastUp = pg.time.get_ticks()

                    # if customer is in area where they can get sandwich, the customer can get the sandwich
                    if sand_t < player.rect.y:

                        if (731<mouse[0]<783) and (295 < mouse[1] < 396):
                            
                            sandwich_touch = True
                            sandwich = True
                            coffee = False
                            croissant = False
                            lastUp = pg.time.get_ticks()               

            # if event is quit, stop program
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            
            # timer counting every second going by for countdown 
            if event.type == pg.USEREVENT:
                time_left -= 1
                new_cust_counter += 1

            # if player clicks 'w, a, s, d' or arrow keys, move player in desired direction
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT or event.key == ord('a'):
                    moveL = True 
                    
                if event.key == pg.K_RIGHT or event.key == ord('d'):          
                    moveR = True
                    
                if event.key == pg.K_UP or event.key == ord('w'):
                    moveU = True
                    
                if event.key == pg.K_DOWN or event.key == ord('s'):
                    moveD = True

            # stop if not clicking key anymore
            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT or event.key == ord('a'):
                    moveL = False
                    

                if event.key == pg.K_RIGHT or event.key == ord('d'): 
                    moveR = False
                    

                if event.key == pg.K_UP or event.key == ord('w'):
                    moveU = False

                if event.key == pg.K_DOWN or event.key == ord('s'):
                    moveD = False
            
            # checking where barriers are and where player cannot move past
            if(moveL):
                if player.rect.x > border_left:
                    player.walk("left")
            
            if(moveR):
                if player.rect.y > counter_bottom - 40:  
                    if player.rect.x < counter_low_side:   
                        player.walk("right")
                
                elif player.rect.y < counter_bottom+40:
                    if player.rect.x < counter_top_side:
                        player.walk("right")
                
            if(moveU):
                if player.rect.x > counter_top_side - 10:
                    if player.rect.y > counter_bottom:
                        player.walk("up")

                elif player.rect.x < counter_top_side + 10:
                    if player.rect.y > border_top:
                        player.walk("up")   
            
            if(moveD):
                if player.rect.y < border_bottom:
                    player.walk("down")

        # blit background onto screen
        bg_lvl1 = setBg('imagesProjec/lvl1.png', x, y, screen)
        screen.blit(player.image, player.rect)
        
        # checking how many customers so new customer may appear at a random interval
        if new_cust_counter == random.randint(5,10):

            # for every customer not on the screen, add it back to current customer list and create new customer
            for which in customers:
                if which.number not in current_cust:
                    current_cust.append(which.number)
            
            diff_cust = set(customer_list).difference(set(current_cust)) # checking which customers are not on screen

            # add new customer for the customer not on the screen
            if diff_cust:
                num = random.choice(list(diff_cust))
                c = Customer(num)
                customers.add(c)
                all_sprites.add(c)

            new_cust_counter = 0
            current_cust.clear()


        # going through steam images and blitting indicators of if user has collected item or not
        if coffee_touch:
            now = pg.time.get_ticks()
            if now - lastUp > steam_framerate:
                lastUp = now
                imgIndex += 1

                if imgIndex == len(steam_anim):
                    imgIndex = 0
                    counter += 1

                if counter == 3:
                    coffee_touch = False
                    imgIndex = 0
                    counter = 0

            screen.blit(steam_anim[imgIndex], (495,50))
            print_text(screen, font, 563, 104, "+1 Coffee", 70, 20, color = WHITE)

        # checking if customer clicked to receive item and giving the item
        if croissant_touch:
            now = pg.time.get_ticks()
            if now - lastUp > 10*steam_framerate:
                croissant_touch = False

            print_text(screen,font,695,130,"+1 Croissant", 100, 20, color = WHITE)

        # checking if customer clicked to receive item and giving the item
        if sandwich_touch:
            now = pg.time.get_ticks()
            if now - lastUp > 10*steam_framerate:
                sandwich_touch = False
            print_text(screen,font,695,280,"+1 Sandwich", 100, 20, color = WHITE)

        
        # initializing timer
        total_mins = time_left//60
        total_sec = time_left-(60*(total_mins))
        
        if time_left > -1: # if time remaining is greater than one, print the timer
            if total_sec > 9:
                print_text(screen,font, 747, 30, str(total_mins)+":"+(str(total_sec)), 60, 37)

            else: print_text(screen,font, 747, 30, str(total_mins)+":0"+(str(total_sec)), 60, 37) 
       
        # if timer runs out, game over
        else:
            location = "game over"
            return location

        # collisions
        collide = pg.sprite.spritecollide(player, customers, False)

        # for collision between player and customer sprite group
        for c in collide:
            
            player.rect.x += 1 # move customer away to only record one collision
           
            collide_time = pg.time.get_ticks() # initializing variable for when player collided with a customer
            
            if coffee == True:  # if player has coffee at time of collision

                # checking if customer wanted coffee
                if "Coffee" in c.items:  

                    # player does not have coffee anymore, customer receives it
                    coffee = False
                    c.received.append("Coffee")

                # if customer was not supposed to receive coffee, remove coffee from player and stop showing order to show anger
                else: 
                    c.show_anger = True
                    coffee = False
                    c.show_order = False
            
            # if player has croissant at time of collision
            if croissant == True:

                # checking if customer wanted croissant
                if "Croissant" in c.items:

                    # player does not have croissant anymore, customer receives it
                    croissant = False
                    c.received.append("Croissant")
                
                # if customer was not supposed to receive croissant, remove croissant from player and stop showing order to show anger
                else:
                    croissant = False
                    c.show_anger = True
                    c.show_order = False

            # if player has sandwich at time of collision
            if sandwich == True:

                if "Sandwich" in c.items: # checking if customer wanted sandwich

                    # player does not have sandwich anymore, customer receives it
                    sandwich = False
                    c.received.append("Sandwich")

               
                else:  # if customer was not supposed to receive sandwich
                    
                    # remove sandwich from player and stop showing order to show anger
                    sandwich = False
                    c.show_anger = True
                    c.show_order = False

            # if customer should be showing anger
            if c.show_anger == True:
                # play wrong object sound effect
                wrongObj()
                print_text(screen, font, c.rect.x, c.rect.y - 31, "I didn't order that!", 180, 30, DARK_RED)

        # for customer in customer group
        for cust in customers:
            if cust.show_order == False:
                # get time of starting to show anger
                now = pg.time.get_ticks() 
                # # while time between current ticks and collision is less than 1.5s, print anger message
                if (now - collide_time)/1000 > 1.5:
                #     # after time elapses, show order again and stop showing anger
                    cust.show_order = True
                    cust.show_anger = False

            # if the customer should be waiting for order and showing its order
            if cust.phase == 1:
                if cust.show_order == True:
                    
                    if cust.number == 1:  # checking customer type

                        # printing order depending on what has been fulfilled already
                        if cust.items[0] in cust.received and cust.items[1] not in cust.received:
                            print_text(screen, font, cust.rect.x + 20, cust.rect.y - 20, "1 Croissant", 90, 20, DARK_RED)
                        
                        if cust.items[1] in cust.received and cust.items[0] not in cust.received:
                            print_text(screen, font, cust.rect.x + 20, cust.rect.y - 20, "1 Sandwich", 90, 20, DARK_RED)
                        
                        else:
                            print_text(screen, font, cust.rect.x + 20, cust.rect.y - 40, "1 Sandwich", 90, 20, DARK_RED)
                            print_text(screen, font, cust.rect.x + 20, cust.rect.y - 20, "1 Croissant", 90, 20, DARK_RED)

                    if cust.number == 2: # checking customer type

                        # printing order depending on what has been fulfilled already
                        if cust.items[0] in cust.received and cust.items[1] not in cust.received:
                            print_text(screen, font, cust.rect.x + 20, cust.rect.y - 20, "1 Croissant", 90, 20, DARK_RED)
                            
                        if cust.items[1] in cust.received and cust.items[0] not in cust.received:
                            print_text(screen, font, cust.rect.x + 20, cust.rect.y - 20, "1 Coffee", 90, 20, DARK_RED)
                        
                        else: 
                            print_text(screen, font, cust.rect.x + 20, cust.rect.y - 20, "1 Coffee", 70, 20, DARK_RED)
                            print_text(screen, font, cust.rect.x + 20, cust.rect.y - 40, "1 Croissant", 90, 20, DARK_RED)
                    
                    if cust.number == 3: # checking customer type

                        # printing order
                        print_text(screen, font, cust.rect.x + 20, cust.rect.y - 20, "1 Coffee", 70, 20, DARK_RED)
            
            # checking if received items matches what was ordered regardless of what order received
            if(sorted(cust.received) == sorted(cust.items)):

                score += 10 # adding points to the score
                cust.received.clear() # clearing list of received items
                cust.hasOrd = True # setting bool value as True for items received

            # if the customer has received the order
            if cust.hasOrd == True:

                # record what time order was received
                ord_ready_time = pg.time.get_ticks()

                cust.show_order = False # stop showing order

                if ord_ready_time - collide_time < 1000: # while 1s has not passed between colliding and order reception
                    
                    # print thank you
                    print_text(screen, font, c.rect.x, c.rect.y - 20, "Thank you!", 90, 20)

                else: # customer enter leaving phase, and customer does not have order anymore
                    cust.phase = 2
                    cust.hasOrd = False

        
        customers.update() # update customers group
        all_sprites.draw(screen) # draw sprites on screen
        print_text(screen, font, 585, 27, "Your Score: "+(str(score)), 130, 30) # print score
        pg.display.flip() # update display

    return location # return location

def gameOver(screen, location):
    """
	This function is the game over screen.
	Args
		quit: bool
        : int
	Returns
		x and y, being the dimensions of the screen
	"""

    pg.mixer.stop()

    gameOv() 

    
    quit = False

    while not quit:

        # set background
        x,y = getDim()
        bg_over = setBg('imagesProjec/game_over.png', x, y, screen)

        # for every event that occurs
        for event in pg.event.get():
            mouse = pg.mouse.get_pos()

            # if event type is quit, quit program
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            
           # if player clicks on area, change to title location
            elif event.type == pg.MOUSEBUTTONDOWN:

                if 355<= mouse[0]<=530 and 248 <= mouse[1] <= 305:
                    location = 'title'
                    quit = True

        pg.display.flip() #update display


    return location # return location
                    
    

        
    

