# This module gives the visualization and gameplay handler
import numpy as np
import pygame as pg
import sys
import os
import math
import Greedy
def initialize():
	board_mesh = np.zeros((6, 7), int)
	return board_mesh

############
pg.init()
DiskSize=70
Circle_rad= 30
Screen_Width= 800	
Screen_Height= 600	
Screen_Size = (Screen_Width,Screen_Height)
Screen = pg.display.set_mode(Screen_Size)
bg=pg.image.load("Board.png")
piece1 = pg.image.load("piece1.png")
piece2 = pg.image.load("piece2.png")
place_holder = pg.image.load("Player_place_holder.png")
Player1Wins=pg.image.load("Player1Wins.png")
Player2Wins=pg.image.load("Player2Wins.png")
Screen.blit(bg,(0,0))
pg.font.init()
font=pg.font.SysFont('Helvetica',30)
text_player1 = font.render("Player 1",False,(0,0,0))
text_player2 = font.render("Player 2",False,(0,0,0))
###########################
player1_mode = "manual"
player2_mode = "greedy"
############

def board_UI(board_mesh):
	# for c in range(7):
	# 	for r in range(6):
	# 		pg.draw.rect(Screen,(0,0,255),(c*DiskSize,(r+1)*DiskSize,DiskSize,DiskSize))
	# 		pg.draw.circle(Screen,(255,255,255),(int(c*DiskSize+DiskSize/2),int((r+1)*DiskSize+DiskSize/2)),Circle_rad)
	for c in range(7):
		for r in range(6):
			if board_mesh[r][c]== 1 :
				#pg.draw.circle(Screen,(255,0,0),(int(c*DiskSize+50),int(Screen_Height-(r+1)*DiskSize+DiskSize/2)),Circle_rad)
				Screen.blit(piece1,(18+c*70,515-r*70))
			elif board_mesh[r][c]== 2 :
				#pg.draw.circle(Screen,(0,255,0),(int(c*DiskSize+50),int(Screen_Height-(r+1)*DiskSize+DiskSize/2)),Circle_rad)
				Screen.blit(piece2,(18+c*70,515-r*70))
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
		if turn%2 == 0:
			Screen.blit(piece1,(646,450))
			Screen.blit(place_holder,(620,403))
			Screen.blit(text_player1,(646,410))
		if turn%2 == 1:
			Screen.blit(piece2,(646,450))
			Screen.blit(place_holder,(620,403))
			Screen.blit(text_player2,(646,410))
		player_number = player_number+1 
		#pass
	else:
		print("NOT a Legal Move!!!")
		player_number=player_number
		#move_j = get_action(player_number, board_mesh,X_position)
	pg.display.update()
	return move_j,player_number

def Random_Action(player_number, board_mesh):
	#move_j = int(input("Player"+str(player_number)+", Please input the column number of your move from 0 to 6   "));
	move_j=(np.random.randint(7,size=1))
	if is_viable_action(move_j, board_mesh):
		if turn%2 == 0:
			Screen.blit(piece1,(646,450))
			Screen.blit(place_holder,(620,403))
			Screen.blit(text_player1,(646,410))
		if turn%2 == 1:
			Screen.blit(piece2,(646,450))
			Screen.blit(place_holder,(620,403))
			Screen.blit(text_player2,(646,410))
		player_number = player_number+1 
		#pass
	else:
		print("NOT a Legal Move!!!")
		player_number=player_number
		#move_j = get_action(player_number, board_mesh,X_position)
	return move_j,player_number

def visualize(board_mesh):
	i = 5
	j = 0
	while i != -1:
		while j != 7:
			print(str(board_mesh[i, j]), end = ' ', flush=True)
			j = j + 1
		print("")
		i = i - 1
		j = 0

def get_position_on_board(move_j, board_mesh):
	move_i = 0
	for i in range(6):
		if (board_mesh[i, move_j] == 0):
			move_i = i
			break
	return move_i

def res_Or_quit(restart):
	while not restart:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()
				#os._exit(0)
			if event.type == pg.MOUSEBUTTONDOWN:
				print(event.pos[0])
				print(event.pos[1])
				if ((event.pos[0]>=137 and event.pos[0]<=137+239) and ( event.pos[1]>=303 and event.pos[1]<=141+303)):
					print("Quit")
					#sys.exit()
					os._exit(0)
				if ((event.pos[0]>=422 and event.pos[0]<=422+249) and ( event.pos[1]>=139 and event.pos[1]<=139+303)):
					print("restart")
					restart = True
					board_mesh = initialize()
					board_UI(board_mesh)
					Screen.blit(bg,(0,0))
					pg.display.update()
					turn = -1
	return board_mesh,turn

				


board_mesh = initialize()
live = True
restart = False
turn = -1
move_i = 0


board_UI(board_mesh)
pg.display.update()



while live:
	if turn == -1:
		board_mesh = initialize()
		Screen.blit(piece1,(646,450))
		Screen.blit(place_holder,(620,403))
		Screen.blit(text_player1,(646,410))
		turn = 1
		pg.display.update()

	for event in pg.event.get():
		if event.type == pg.QUIT:
			live = False
			pg.display.quit()
			pg.quit()
			#sys.exit()
			os._exit
		if event.type == pg.MOUSEBUTTONDOWN:
			print(event.pos)

			if event.pos[0] < 500 :
				print("Turn is : ",turn)
				X_position = event.pos[0]
				# Initialization
				if turn == -1:
					board_mesh = initialize()
					Screen.blit(piece1,(646,450))
					Screen.blit(place_holder,(620,403))
					Screen.blit(text_player1,(646,410))
					pg.display.update()
					turn = 0
				else:
					pass
				# Gameplay
				if turn%2 == 1:
					print ("turn 1")
					if player1_mode =="manual":
						move_j,turn= get_action(turn%2, board_mesh,X_position)
					elif player1_mode =="random":
						move_j,turn= Random_Action(turn%2,board_mesh)
					elif player1_mode =="greedy":
						move_j,turn = Greedy.greedy_search(board_mesh,turn%2,get_position_on_board,Greedy.greedy_score,is_viable_action)
					move_i = get_position_on_board(move_j, board_mesh)
					if is_viable_action(move_j, board_mesh):
						board_mesh[move_i, move_j] = turn%2 + 1
						Screen.blit(piece2,(646,450))
						Screen.blit(place_holder,(620,403))
						Screen.blit(text_player2,(646,410))		

				elif turn%2==0 :
					print ("turn 2")
					if player2_mode =="manual":
						move_j,turn= get_action(turn%2, board_mesh,X_position)
					elif player2_mode =="random":
						move_j,turn= Random_Action(turn%2,board_mesh)
					elif player2_mode =="greedy":
						move_j,turn = Greedy.greedy_search(board_mesh,turn%2,get_position_on_board,Greedy.greedy_score,is_viable_action)
					move_i = get_position_on_board(move_j, board_mesh)
					if is_viable_action(move_j, board_mesh):
						board_mesh[move_i, move_j] = turn%2 +1
						Screen.blit(piece1,(646,450))
						Screen.blit(place_holder,(620,403))
						Screen.blit(text_player1,(646,410))	
			# Print latest Game Position
			visualize(board_mesh)
			board_UI(board_mesh)
			if winning_Condition(board_mesh,1):
				print("Player 1 Wins !")
				print("Game Over!!")
				Screen.blit(Player1Wins,(0,0))
				pg.display.update()
				board_mesh,turn=res_Or_quit(restart)
				
				
			if winning_Condition(board_mesh,2):
				print("Player 2 Wins !")
				print("Game Over!!")
				Screen.blit(Player2Wins,(0,0))
				pg.display.update()
				board_mesh,turn=res_Or_quit(restart)

			#turn = turn + 1;

			# Check end of Game Conditions
			if turn == 6*7:
				print ("Game OVER!")
				live = False