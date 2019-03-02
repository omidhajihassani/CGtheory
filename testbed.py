import numpy as np
from solver import solver

def get_position_on_board(move_j, board_mesh):
    move_i = 0;
    for i in range(5):
        if (board_mesh[i, move_j] == 0):
            move_i = i
            break
    return move_i;

f = open("Test_L3_R1.txt", "r")

def state2mesh():
    entry = f.readline()
    print(entry)
    state, value = entry.split(" ")
    print (len(state))
    print (state)
    print (value)
    board_mesh = np.zeros((6,7), int)
    turn = 1;
    for i in range(len(state)):
        print("state is", str(int(state[i])-1));
        print("whose turn is it "+ str(turn))
        board_mesh[get_position_on_board(int(state[i])-1, board_mesh), int(state[i])-1] = turn%2 + 1
        turn = turn + 1
        visualize(board_mesh)
    return board_mesh

# print(state2mesh());

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

board_mesh = np.zeros((6,7), int)

board_mesh = np.array([[1, 1, 1, 2, 2, 2, 0],
                [1, 1, 1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0]])
visualize(state2mesh())
slvr = solver()
slvr.solve(board_mesh, 1, 2)
