# This module gives the visualization and gameplay handler
import numpy as np

def initialize():
	board_mesh = np.zeros((6, 7), int);
	return board_mesh

def is_viable_action(move_i, move_j):
	if(move_i >= 0 and move_i <= 5) and (move_j >= 0 and move_j <= 6):
		return True
	else:
		return False
def get_action(player_number):
	move_j = int(input("Player"+str(player_number)+", Please input the column number of your move from 0 to 6   "));
	move_i = int(input("Player"+str(player_number)+", Please input the row number of your move from 0 to 5   "));
	
	if is_viable_action(move_i, move_j):
		pass
	else:
		print("NOT a Legal Move!!!")
		move_i, move_j = get_action(player_number)
	return move_i, move_j;

board_mesh = None;
live = True;
turn = 0;

while live:
	# Initialization
	if turn == 0:
		board_mesh = initialize()
	# Gameplay
	if turn%2 == 0:
		print ("turn 1")
		get_action(turn%2);
	else:
		print ("turn 2") 
		get_action(turn%2);

	# Print latest Game Position
	print(initialize())
	
	turn = turn + 1;
	
	# Check end of Game Conditions
	if turn == 6*7:
		print ("Game OVER!");
		live = False;
