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
game_on = False
stop_execution = False
play_w_comp = False
play_w_opp = False
#A function that will move the ball either both left&down, left&up, right&down, right&up  

#A function that displays a Message

#a function that asks th user do we stArt or nah then moves the ball when spacekey is pressed
def popup_message(ftext,color):
    """
    Purpose: asks th user do we stArt or nah
    """
    ftext = font.render(ftext,True,color)
    gm_window.blit(ftext,[2,window_height/2])
# end def

# a function that will ask the user if play with robot or another player
#ask the user if they want to play against user or computer
#play_type = input("Play against Computer(C) or Player(P)? ")

# a function that will decide the score and if one has a score of three they win

#a function that will detect the collision between the ball and the players or the opp
def check_collisions():
    """
    Purpose: it checks if the ball collided with the player or the opp
             if so it has to change its direction by multiplicational
             incrementation(*= -1)
    """
    if (pl_y_pos < ball_y_pos + ball_height and pl_y_pos + pl_height > ball_y_pos and pl_x_pos < ball_x_pos + ball_width and pl_x_pos + pl_width > ball_x_pos) or (opp_y_pos < ball_y_pos + ball_height and opp_y_pos + opp_height > ball_y_pos and opp_x_pos < ball_x_pos + ball_width and opp_x_pos + opp_width > ball_x_pos):
       #this where tha ball would move up or down
       ball_y_pos *= -1
# end def

# def ball_x_movement_collision():
#     """
#     Purpose: this function defines the movement of the ball then also check for collisions if wall is hit and if player or opp is hit
#     """
#     #first check for walls +-20
#     """
#         #move the computer opp
#         opp_x_pos += opp_velocity
#         if opp_x_pos <= 0 or opp_x_pos >= window_width - opp_width:
#             opp_velocity *= -1
#     """
#     global ball_x_pos
#     global ball_velocity
    
#     ball_x_pos = ball_velocity
#     if ball_x_pos <= 30 or ball_x_pos >= window_width-30:
#         ball_velocity *= -1 
# # end def

#score
score = 0
font = pyg.font.Font(None, 30)
#calling the message functin to see if game starts or not
gm_window.fill(lemon)
popup_message("Start the game? Y-Start or N-Don't Start", blue)
# create an if statement that will check if which character is clicked if "y" then the game must go on moving the ball, if "n" then the game must terminate 

# gm_window.fill(lemon)
# popup_message("Play with C-Computer or O-Opponent?", dblue)
#on the Y (on game start) if statement decide if play with opp or computer  
pyg.display.update()

# main loop
while game_start:
    pyg.time.delay(100)

    #to continuously move the player
    keys = pyg.key.get_pressed()

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            game_start = False
        
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_y:
                game_on = True

            elif event.key == pyg.K_n:
                game_on = False
                
        # if key y is clicked then the code below must be implemented
        # check for events and collisions
        
        if game_on == True:             
            #before we move the opp the user must be prompted if they want to play against another user or computer
            #call the message function to ask the player if play against another user or computer
            gm_window.fill(lemon)
            ball_x_pos += ball_velocity
            # if play_type.upper() == "C":
            #         #move the computer opp
            #         opp_x_pos += opp_velocity
            #         if opp_x_pos <= 0 or opp_x_pos >= window_width - opp_width:
            #             opp_velocity *= -1
            # elif play_type.upper() == "P":
            # ball_x_pos -= ball_velocity
            #Move the player
            #check direction which the player moved towards (left or right )
            if keys[pyg.K_LEFT] and pl_x_pos > pl_velocity:
                pl_x_pos -= pl_velocity
            if keys[pyg.K_RIGHT] and pl_x_pos < window_width - 20:
                pl_x_pos += pl_velocity
            #move opponent
            #check direction which the player moved towards (left or right ) 
            if keys[pyg.K_a] and opp_x_pos > opp_velocity:
                opp_x_pos -= opp_velocity
            if keys[pyg.K_d] and opp_x_pos < window_width - 20:
                opp_x_pos += opp_velocity    
            #move the ball
            
            
            # if ball_x_pos <= 30 or ball_x_pos >= window_width-30:
            #     ball_velocity *= -1 
                
            ball_y_pos += ball_velocity
            if (ball_x_pos == opp_x_pos and ball_y_pos == opp_y_pos) or (ball_x_pos == pl_x_pos and ball_y_pos == pl_y_pos) or ( ):
                ball_velocity *= -1     
            #ball_y_pos -= ball_velocity
            # ball_x_movement_collision()
            #fill background with color
            gm_window.fill(lemon)

            #draw the objects / players
            pyg.draw.rect(gm_window, blue, (pl_x_pos, pl_y_pos, pl_width, pl_height))
            pyg.draw.rect(gm_window, dblue, (opp_x_pos, opp_y_pos, opp_width, opp_height) )
            #draw the ball
            pyg.draw.rect(gm_window, white, (ball_x_pos, ball_y_pos, ball_width, ball_height))

            #update the display
            pyg.display.update()
            #else if the n key is pressed the game must terminate
        elif game_on == True:
            game_start = False
            pyg.quit()    
            '''this would mark the end of the start or not if statement'''
pyg.quit()            