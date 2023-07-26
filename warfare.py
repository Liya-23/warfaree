# handle imports
import pygame as pyg
import random

#initialize pygame
pyg.init()

#set the screen size
window_width = 400
window_height = 600
gm_window = pyg.display.set_mode((window_width,window_height))
pyg.display.set_caption("Warfare by 'The HERO'")

#set up the colors
black = (51, 51, 51)
white = (225,225,225)
blue = (0,0,255)
dblue =(0,0,139)
lemon = (127,225,0)
dgreen = (69,139,0)
purple = (191,62,255)
dpurple = (104,34,139)
red = (238,59,59)

# set up the properties 
#players
#player
pl_width = 40
pl_height = 10
pl_x_pos = window_width/2
pl_y_pos = window_height-50
pl_velocity = 8
#opposition
opp_width = 40
opp_height = 10
opp_x_pos = window_width/2
opp_y_pos = 50
opp_velocity = 15
#projectiles
ball_width = 8
ball_height = 8
ball_x_pos = window_width/2
ball_y_pos = window_height/2
ball_velocity = 12

#other variables
game_start = True

#ask the user if they want to play against user or computer
play_type = input("Play against Computer(C) or Player(P)? ")

#score
score = 0
font = pyg.font.Font(None, 30)

# main loop
while game_start:
    pyg.time.delay(100)

    # check for events and collisions
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            game_start = False
        
        #to continuously move the player
        keys = pyg.key.get_pressed()
        #before we move the opp the user must be prompted if they want to play against another user or computer
        if play_type.upper() == "C":
                #move the computer opp
                opp_x_pos += opp_velocity
                if opp_x_pos <= 0 or opp_x_pos >= window_width - opp_width:
                    opp_velocity *= -1
        # elif play_type.upper() == "P":
            
        
        #Move the player
        #check direction which the player moved towards (left or right )
        if keys[pyg.K_LEFT] and pl_x_pos > pl_velocity:
            pl_x_pos -= pl_velocity
        if keys[pyg.K_RIGHT] and pl_x_pos < window_width - pl_width :
            pl_x_pos += pl_velocity
        
        #fill background with color
        gm_window.fill(lemon)
        
        #draw the objects / players
        pyg.draw.rect(gm_window, blue, (pl_x_pos, pl_y_pos, pl_width, pl_height))
        pyg.draw.rect(gm_window, dblue, (opp_x_pos, opp_y_pos, opp_width, opp_height) )
        #draw the ball
        pyg.draw.rect(gm_window, white, (ball_x_pos, ball_y_pos, ball_width, ball_height))
        
        #update the display
        pyg.display.update()
        
pyg.quit()            