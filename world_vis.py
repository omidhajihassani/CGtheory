# This module gives the visualization and gameplay handler
import numpy as np
from solver import solver

state = []

def initialize():
	board_mesh = np.zeros((6, 7), int);
	return board_mesh

def is_viable_action(move_j, board_mesh):
	if (move_j >= 0 and move_j <= 6):
		if (board_mesh[5, move_j] == 0):
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

def get_action(player_number, board_mesh):
	move_j = int(input("Player"+str(player_number)+", Please input the column number of your move from 0 to 6   "));
	if is_viable_action(move_j, board_mesh):
		position2state(state, move_j);
	else:
		print("NOT a Legal Move!!!")
		move_j = get_action(player_number, board_mesh)
	return move_j;

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

def position2state(state, move_j):
	state.append(move_j);

board_mesh = None;
live = True;
turn = 0;
move_i = 0;
while live:
	slvr = solver();
	# Initialization
	if turn == 0:
		board_mesh = initialize()
	# Gameplay
	if turn%2 == 0:
		print ("turn 1")
		move_j = get_action(turn%2, board_mesh);
		move_i = get_position_on_board(move_j, board_mesh);
		board_mesh[move_i, move_j] = turn%2 + 1
		slvr.solve(state, board_mesh, turn%2);

	else:
		print ("turn 2")
		move_j = get_action(turn%2, board_mesh);
		move_i = get_position_on_board(move_j, board_mesh);
		board_mesh[move_i, move_j] = turn%2 + 1
		slvr.solve(state, board_mesh, turn%2);

	# Print latest Game Position
	visualize(board_mesh)
	if winning_Condition(board_mesh,1):
		print("Player 1 Won the Game !")
		print("Game Over!!")
		live = False
	if winning_Condition(board_mesh,2):
		print("Player 2 Won the Game !")
		print("Game Over!!")
		live = False
	turn = turn + 1;

	# Check end of Game Conditions
	if turn == 6*7:
		print ("Game OVER!");
		live = False;
