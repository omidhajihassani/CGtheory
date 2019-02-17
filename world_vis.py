# This module gives the visualization and gameplay handler
import numpy as np

def initialize():
	board_mesh = np.zeros((6, 7), int);
	return board_mesh

def is_viable_action(move_j, board_mesh):
	if (move_j >= 0 and move_j <= 6):
		if (board_mesh[5, move_j] == 0):
			return True
	else:
		return False

def get_action(player_number, board_mesh):
	move_j = int(input("Player"+str(player_number)+", Please input the column number of your move from 0 to 6   "));
	if is_viable_action(move_j, board_mesh):
		pass
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

board_mesh = None;
live = True;
turn = 0;
move_i = 0;
while live:
	# Initialization
	if turn == 0:
		board_mesh = initialize()
	# Gameplay
	if turn%2 == 0:
		print ("turn 1")
		move_j = get_action(turn%2, board_mesh);
		move_i = get_position_on_board(move_j, board_mesh);
		board_mesh[move_i, move_j] = turn%2 + 1
	else:
		print ("turn 2") 
		move_j = get_action(turn%2, board_mesh);
		move_i = get_position_on_board(move_j, board_mesh);
		board_mesh[move_i, move_j] = turn%2 + 1
	
	# Print latest Game Position
	visualize(board_mesh)

	turn = turn + 1;
	
	# Check end of Game Conditions
	if turn == 6*7:
		print ("Game OVER!");
		live = False;
