# This module gives the visualization and gameplay handler
import numpy as np
import pygame as pg
import sys
import os
import math
import Greedy
import time
from solver import solver
slvr = solver()
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
wlc=pg.image.load("Welcome.png")
wlc1 =pg.image.load("Welcome1.png")
wlc2 =pg.image.load("Welcome2.png")
select = pg.image.load("select.png")
pg.display.set_caption('Connect Four Game')
piece1 = pg.image.load("piece1.png")
piece2 = pg.image.load("piece2.png")
place_holder = pg.image.load("Player_place_holder.png")
Player1Wins=pg.image.load("Player1Wins.png")
Player2Wins=pg.image.load("Player2Wins.png")
Draw=pg.image.load("Drawww.png")
back = pg.image.load("Back.png")
Screen.blit(bg,(0,0))
pg.font.init()
font=pg.font.SysFont('Helvetica',30)
text_player1 = font.render("Player 1",False,(0,0,0))
text_player2 = font.render("Player 2",False,(0,0,0))
###########################
player1_mode = "manual"
player2_mode = "manual"
############ Depth of Solver
solver_depth = 10
#################

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
	#pg.display.update()
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

def res_Or_quit(restart,board_mesh):
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
				if ((event.pos[0]>=700 and event.pos[0]<=800) and ( event.pos[1]>=0 and event.pos[1]<=100)):
					restart = True
					board_mesh = initialize()
					global welcome
					global once
					welcome = True
					once = True
					turn = -1

			else:
				pass
	return board_mesh,turn

				

once =True
board_mesh = initialize()
live = True
restart = False
turn = -1
move_i = 0
player = True
welcome = True
board_UI(board_mesh)
pg.display.flip()



while live:

	while welcome :
		while once:
			Screen.blit(wlc,(0,0))
			pg.display.update()
			once = False
		for event in pg.event.get():
			if event.type == pg.QUIT:
				live = False
				pg.display.quit()
				pg.quit()
				#sys.exit()
				os._exit(0)
			if event.type == pg.MOUSEBUTTONDOWN : 
				if ((event.pos[0]>=80 and event.pos[0]<=80+260) and ( event.pos[1]>=280 and event.pos[1]<=330)):
					player1_mode = "manual"
					print("Manual")
					Screen.blit(wlc1,(0,0))
					Screen.blit(select,(60,280+20))
					pg.display.update()
				elif ((event.pos[0]>=80 and event.pos[0]<=80+260) and ( event.pos[1]>=331 and event.pos[1]<=390)):
					player1_mode = "random"
					print("Random")
					Screen.blit(wlc1,(0,0))
					Screen.blit(select,(60,340+20))
					pg.display.update()
				elif ((event.pos[0]>=80 and event.pos[0]<=80+260) and ( event.pos[1]>=391 and event.pos[1]<=460)):
					player1_mode = "greedy"
					print("Greedy")
					Screen.blit(wlc1,(0,0))
					Screen.blit(select,(60,400+20))
					pg.display.update()
				elif ((event.pos[0]>=80 and event.pos[0]<=80+260) and ( event.pos[1]>=461 and event.pos[1]<=510)):
					player1_mode = "solver"
					print("Slover")
					Screen.blit(wlc1,(0,0))
					Screen.blit(select,(60,460+20))
					pg.display.update()
				if ((event.pos[0]>=420 and event.pos[0]<=680) and ( event.pos[1]>=280 and event.pos[1]<=330)):
					player2_mode = "manual"
					print("Manual")
					Screen.blit(wlc2,(400,0))
					Screen.blit(select,(400,280+20))
					pg.display.update()
				elif ((event.pos[0]>=420 and event.pos[0]<=680) and ( event.pos[1]>=331 and event.pos[1]<=390)):
					player2_mode = "random"
					print("Random")
					Screen.blit(wlc2,(400,0))
					Screen.blit(select,(400,340+20))
					pg.display.update()
				elif ((event.pos[0]>=420 and event.pos[0]<=680) and ( event.pos[1]>=391 and event.pos[1]<=460)):
					player2_mode = "greedy"
					print("Greedy")
					Screen.blit(wlc2,(400,0))
					Screen.blit(select,(400,400+20))
					pg.display.update()
				elif ((event.pos[0]>=420 and event.pos[0]<=680) and ( event.pos[1]>=461 and event.pos[1]<=510)):
					player2_mode = "solver"
					print("Solver")	
					Screen.blit(wlc2,(400,0))
					Screen.blit(select,(400,460+20))
					pg.display.update()
				if ((event.pos[0]>=690 and event.pos[0]<=775) and ( event.pos[1]>=485 and event.pos[1]<=572)):
					print("Play")
					#Screen.blit(wlc,(0,0))
					Screen.blit(bg,(0,0))
					pg.display.update()
					welcome = False
					break
				else :
					pass
	if turn == -1:
		board_mesh = initialize()
		Screen.blit(piece1,(646,450))
		Screen.blit(place_holder,(620,403))
		Screen.blit(text_player1,(646,410))
		Screen.blit(back,(700,10))
		turn = 1
		pg.display.update()

	for event in pg.event.get():
		if event.type == pg.MOUSEBUTTONDOWN:
			if ((event.pos[0]>=700 and event.pos[0]<=800) and ( event.pos[1]>=0 and event.pos[1]<=100)):
				restart = True
				board_mesh = initialize()
				# global welcome
				# global once
				welcome = True
				once = True
				turn = -1
				pg.display.flip()
		elif event.type == pg.QUIT:
			live = False
			pg.display.quit()
			pg.quit()
			#sys.exit()
			os._exit
		#if event.type == pg.MOUSEBUTTONDOWN:
			# print(event.pos)

			# if event.pos[0] < 500 :
			# 	print("Turn is : ",turn)
			# 	X_position = event.pos[0]
			# 	# Initialization
	# if turn == -1:
	# 	board_mesh = initialize()
	# 	Screen.blit(piece1,(646,450))
	# 	Screen.blit(place_holder,(620,403))
	# 	Screen.blit(text_player1,(646,410))
	# 	pg.display.update()
	# 	turn = 1
	# else:
	# 	pass
	# 		# Gameplay
	if turn%2 == 1:
		print ("turn 1")
		if player1_mode =="manual":
			while player :
				for event in pg.event.get():
					if event.type == pg.QUIT:
						#sys.exit()
						os._exit(0)
					if event.type == pg.MOUSEBUTTONDOWN:
						if ((event.pos[0]>=700 and event.pos[0]<=800) and ( event.pos[1]>=0 and event.pos[1]<=100)):
							restart = True
							board_mesh = initialize()
							# global welcome
							# global once
							welcome = True
							once = True
							turn = -1
							pg.display.flip()
							player = False
						if event.pos[0] < 500 :
							print("Turn is : ",turn)
							X_position = event.pos[0]
							move_j,turn= get_action(turn%2, board_mesh,X_position)
							player = False
						
						else : 
							pass
			player = True
		elif player1_mode =="random":
			move_j,turn= Random_Action(turn%2,board_mesh)
			time.sleep(0.5)
			#time.sleep(1)
		elif player1_mode =="greedy":
			move_j,turn = Greedy.greedy_search(board_mesh,turn%2,get_position_on_board,Greedy.greedy_score,is_viable_action)
			time.sleep(0.5)
			#time.sleep(1)
		elif player1_mode =="solver" :	
			move_j = slvr.solve(board_mesh, 1, solver_depth) -1
			if is_viable_action(move_j,board_mesh) :
				turn = turn%2 +1
			else : 
				turn = 1
		
		
		move_i = get_position_on_board(move_j, board_mesh)
		if is_viable_action(move_j, board_mesh):
			board_mesh[move_i, move_j] = turn%2 + 1
			board_UI(board_mesh)
			pg.display.update()
			Screen.blit(piece2,(646,450))
			Screen.blit(place_holder,(620,403))
			Screen.blit(text_player2,(646,410))
			Screen.blit(back,(700,10))
			pg.display.flip()
			visualize(board_mesh)


	elif turn%2==0 :
		print ("turn 2")
		if player2_mode =="manual":
			while player :
				for event in pg.event.get():
					if event.type == pg.QUIT:
						os._exit(0)
						#sys.exit()
					if event.type == pg.MOUSEBUTTONDOWN:
						if ((event.pos[0]>=700 and event.pos[0]<=800) and ( event.pos[1]>=0 and event.pos[1]<=100)):
							restart = True
							board_mesh = initialize()
							# global welcome
							# global once
							welcome = True
							once = True
							turn = -1
							pg.display.flip()
							player = False
						if event.pos[0] < 500 :
							print("Turn is : ",turn)
							X_position = event.pos[0]
							move_j,turn= get_action(turn%2, board_mesh,X_position)
							player = False
						else:
							pass
			player = True
		elif player2_mode =="random":
			move_j,turn= Random_Action(turn%2,board_mesh)
			time.sleep(0.5)
			#time.sleep(1)
		elif player2_mode =="greedy":
			move_j,turn = Greedy.greedy_search(board_mesh,turn%2,get_position_on_board,Greedy.greedy_score,is_viable_action)
			time.sleep(0.5)
			#time.sleep(1)

		elif player2_mode =="solver" :	
			move_j = slvr.solve(board_mesh, 2, solver_depth) -1
			if is_viable_action(move_j,board_mesh) :
				turn = turn%2 +1
			else: 
				turn = 0

		move_i = get_position_on_board(move_j, board_mesh)
		if is_viable_action(move_j, board_mesh):
			board_mesh[move_i, move_j] = turn%2 +1
			board_UI(board_mesh)
			pg.display.update()
			Screen.blit(piece1,(646,450))
			Screen.blit(place_holder,(620,403))
			Screen.blit(text_player1,(646,410))	
			Screen.blit(back,(700,10))
			board_UI(board_mesh)
			pg.display.update()
			pg.display.flip()
			visualize(board_mesh)
		#board_UI(board_mesh)
		# Print latest Game Position

	else :
		board_UI(board_mesh)
		Screen.blit(back,(700,10))
		pg.display.flip()
	Screen.blit(back,(700,10))
	pg.display.flip()
	if winning_Condition(board_mesh,1):
		turn = -2
		board_UI(board_mesh)
		pg.display.update()
		pg.display.flip()
		print("Player 1 Wins !")
		print("Game Over!!")
		visualize(board_mesh)
		pg.display.update()
		#time.sleep(5)
		Screen.blit(Player1Wins,(0,0))
		Screen.blit(back,(700,10))
		pg.display.update()
		#live = False
		board_mesh,turn=res_Or_quit(restart,board_mesh)	
	if winning_Condition(board_mesh,2):
		turn = -2
		board_UI(board_mesh)
		pg.display.update()
		pg.display.flip()
		print("Player 2 Wins !")
		print("Game Over!!")
		visualize(board_mesh)
		pg.display.update()
		#time.sleep(5)
		#live= False
		Screen.blit(Player2Wins,(0,0))
		Screen.blit(back,(700,10))
		pg.display.update()
		board_mesh,turn=res_Or_quit(restart,board_mesh)

	#turn = turn + 1;
	
	# Check end of Game Conditions
	if 0 not in board_mesh:
		print ("Game OVER!")
		#live = False
		Screen.blit(Draw,(0,0))
		Screen.blit(back,(700,10))
		pg.display.update()
		board_mesh,turn=res_Or_quit(restart,board_mesh)
		pg.display.update()