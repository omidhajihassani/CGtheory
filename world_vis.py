# This module gives the visualization and gameplay handler
import numpy as np
import pygame as pg
import sys
import UI 
import math
def initialize():
	board_mesh = np.zeros((6, 7), int);
	return board_mesh

############
pg.init()
DiskSize=100
Circle_rad= 35
Screen_Width= 7*DiskSize
Screen_Height= 7*DiskSize
Screen_Size = (Screen_Width,Screen_Height)
Screen = pg.display.set_mode(Screen_Size)

############

def board_UI(board_mesh):
	for c in range(7):
		for r in range(6):
			pg.draw.rect(Screen,(0,0,255),(c*DiskSize,(r+1)*DiskSize,DiskSize,DiskSize))
			pg.draw.circle(Screen,(255,255,255),(int(c*DiskSize+DiskSize/2),int((r+1)*DiskSize+DiskSize/2)),Circle_rad)
	for c in range(7):
		for r in range(6):
			if board_mesh[r][c]== 1 :
				pg.draw.circle(Screen,(255,0,0),(int(c*DiskSize+DiskSize/2),int(Screen_Height-(r+1)*DiskSize+DiskSize/2)),Circle_rad)
			elif board_mesh[r][c]== 2 :
				pg.draw.circle(Screen,(0,255,0),(int(c*DiskSize+DiskSize/2),int(Screen_Height-(r+1)*DiskSize+DiskSize/2)),Circle_rad)
	pg.display.update()
def is_viable_action(move_j, board_mesh):
	if (move_j >= 0 and move_j <= 6):
		if (board_mesh[5][move_j] == 0):
			return True
	else:
		return False
## Defining the Condition of the winnings
def winning_Condition(board_mesh,player_number):
## Checking the Horizontal Winning Strategies
	for columns in range(0,4):
		for rows in range (0,6):
			if board_mesh[rows][columns]==board_mesh[rows][columns+1]==board_mesh[rows][columns+2]==board_mesh[rows][columns+3]==player_number:
				return True
## Checking the Vertical Winning Strtegies
	for columns in range(0,7):
		for rows in range (0,3):
			if board_mesh[rows][columns]==board_mesh[rows+1][columns]==board_mesh[rows+2][columns]==board_mesh[rows+3][columns]==player_number:
				return True
## Checking the Positive Diagonal Strategies
	for columns in range(0,4):
		for rows in range (0,3):
			if board_mesh[rows][columns]==board_mesh[rows+1][columns+1]==board_mesh[rows+2][columns+2]==board_mesh[rows+3][columns+3]==player_number:
				return True
## Checking the Negative Diagonal Strategies
	for columns in range(0,4):
		for rows in range (3,6):
			if board_mesh[rows][columns]==board_mesh[rows-1][columns+1]==board_mesh[rows-2][columns+2]==board_mesh[rows-3][columns+3]==player_number:
				return True

def get_action(player_number, board_mesh,X_position):
	#move_j = int(input("Player"+str(player_number)+", Please input the column number of your move from 0 to 6   "));
	move_j=int(math.floor(X_position/DiskSize))
	if is_viable_action(move_j, board_mesh):
		player_number = player_number+1 
		pass
	else:
		print("NOT a Legal Move!!!")
		#move_j = get_action(player_number, board_mesh,X_position)
	return move_j,player_number;

def visualize(board_mesh):
	i = 5;
	j = 0;
	while i != -1:
		while j != 7:
			print(str(board_mesh[i, j]), end = ' ', flush=True);
			j = j + 1;
		print("")
		i = i - 1;
		j = 0;

def get_position_on_board(move_j, board_mesh):
	move_i = 0;
	for i in range(6):
		if (board_mesh[i, move_j] == 0):
			move_i = i
			break
	return move_i;

board_mesh = initialize();
live = True;
turn = -1;
move_i = 0;


board_UI(board_mesh)
pg.display.update()



while live:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()
		if event.type == pg.MOUSEBUTTONDOWN:
			print(event.pos)
			X_position = event.pos[0]
			# Initialization
			if turn == -1:
				board_mesh = initialize()
			# Gameplay
			if turn%2 == 0:
				print ("turn 1")
				move_j,turn= get_action(turn%2, board_mesh,X_position);
				move_i = get_position_on_board(move_j, board_mesh);
				if is_viable_action(move_j, board_mesh):
					board_mesh[move_i, move_j] = turn%2 + 1

			else:
				print ("turn 2")
				move_j,turn = get_action(turn%2, board_mesh,X_position);
				move_i = get_position_on_board(move_j, board_mesh);
				if is_viable_action(move_j, board_mesh):
					board_mesh[move_i, move_j] = turn%2 + 1

			# Print latest Game Position
			visualize(board_mesh)
			board_UI(board_mesh)
			if winning_Condition(board_mesh,1):
				print("Player 1 Won the Game !")
				print("Game Over!!")
				live = False
			if winning_Condition(board_mesh,2):
				print("Player 2 Won the Game !")
				print("Game Over!!")
				live = False
			#turn = turn + 1;

			# Check end of Game Conditions
			if turn == 6*7:
				print ("Game OVER!");
				live = False