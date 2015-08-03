#! /usr/bin/env python
#------------------------------------------------------------------------------
# File: 		test1.py
# Description:	This is the initial code which contains player move along x-axis
#				 
#------------------------------------------------------------------------------
#import libraries
import pygame

#To access methods within library you use .
pygame.init()

#Everything is obj even 30 is obj which contains the value 30.
# '-' are not allowed in variable names. It indicates minus sign.
#Declare vatiables
FRAME_RATE = 30

#Declare multiple vars
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

#This is how many pixels we move at every second
SPEED_MAX = 5

#set_mode requires a tuple so we need extra () around our variables.
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#To set the timer for the game. Clock is class, hence the capital 'C'.
game_clock = pygame.time.Clock()

#Declare a dictionary
player = {}

#player dic with key set as "image"
player["image"] = pygame.image.load("ball-pic.png")

#(0,0) is located at the top left of the screen. (800,600) is on the opposite side.
player["x"] = player["y"] = 0
player["width"], player["height"] = player["image"].get_size()
player["inc_x"] = player["inc_y"] = 0

#True and False are boolean
game_over = False

#Game loop
#TAB is considered two indentations in python. Indentations are considered 4 spaces.
#No {} for code blocks, we'll use indentations in python instead.
#When you ask for events, there are lot of things heppen at the same time. You get the
#list by callig event.get()
#KEYDOWN is a keyword in event libarary
while not game_over:
	for my_event in pygame.event.get():
		if my_event.type == pygame.KEYDOWN:
			if my_event.key == pygame.K_LEFT:
				player["inc_x"] = -SPEED_MAX
			elif my_event.key == pygame.K_RIGHT:
				player["inc_x"] = SPEED_MAX
		elif my_event.type == pygame.KEYUP:
			if my_event.key == pygame.K_LEFT or my_event.key == pygame.K_RIGHT:
				player["inc_x"] = 0
	player["x"] += player["inc_x"]
	if player["x"] < 0:
		player["x"] = 0
	elif player["x"] > SCREEN_WIDTH - player["width"]:
		player["x"] = SCREEN_WIDTH - player["width"];
	#(0,0,0) is black
	game_screen.fill((0,0,0))
	game_screen.blit(player["image"], (player["x"], player["y"]))
	#show the screen we rendered
	pygame.display.flip()
	game_clock.tick(FRAME_RATE)
