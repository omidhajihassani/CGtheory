import numpy as np
from solver import solver
import time
start = time.time()
"the code you want to test stays here"

# Print(columnOrder)

def get_position_on_board(move_j, board_mesh):
    move_i = 0;
    for i in range(6):
        if (board_mesh[i, move_j] == 0):
            move_i = i
            break
    return move_i;

def can_win(board_mesh,player_number):
    for columns in range(0,4):
        for rows in range (0,6):
            if board_mesh[rows][columns]==board_mesh[rows][columns+1]==board_mesh[rows][columns+2]==board_mesh[rows][columns+3]==player_number:
                return True
    for columns in range(0,7):
        for rows in range (0,3):
            if board_mesh[rows][columns]==board_mesh[rows+1][columns]==board_mesh[rows+2][columns]==board_mesh[rows+3][columns]==player_number:
                return True
    for columns in range(0,4):
        for rows in range (0,3):
            if board_mesh[rows][columns]==board_mesh[rows+1][columns+1]==board_mesh[rows+2][columns+2]==board_mesh[rows+3][columns+3]==player_number:
                return True
    for columns in range(0,4):
        for rows in range (3,6):
            if board_mesh[rows][columns]==board_mesh[rows-1][columns+1]==board_mesh[rows-2][columns+2]==board_mesh[rows-3][columns+3]==player_number:
                return True
    return False

f = open("Test_L3_R1.txt", "r")

def state2mesh():
    for i in range(1):
        entry = f.readline()
    # entry = f.readline()
    # print(entry)
    state, value = entry.split(" ")
    print(value)
    # print (len(state))
    # print (state)
    # print (value)
    board_mesh = np.zeros((6,7), int)
    turn = 1;
    for i in range(len(state)):
        # print("state is", str(int(state[i])-1));
        # print("whose turn is it "+ str(turn%2 + 1))
        board_mesh[get_position_on_board(int(state[i])-1, board_mesh), int(state[i])-1] = turn%2 + 1
        turn = turn + 1
        # visualize(board_mesh)
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

# board_mesh = np.zeros((6,7), int)

board_mesh = np.array([[0, 0, 1, 2, 2, 0, 1],
                [0, 0, 1, 1, 0, 0, 0],
                [0, 0, 1, 2, 0, 0, 0],
                [0, 0, 0, 2, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 2, 0, 0, 0]])
# board_mesh = state2mesh();
# for i in range(6):
#     for j in range(7):
#         if board_mesh[i, j] == 0:
#             break
#         if board_mesh[i, j] == 1:
#             board_mesh[i, j] = 2
#         else:
#             board_mesh[i, j] = 1


visualize(board_mesh)
# board_mesh[1, 6] = 0
# board_mesh[2, 5] = 1
# board_mesh[2, 4] = 1
#board_mesh[5, 5] = 2

print("")
# board_mesh = np.zeros((6, 7), int)
visualize(board_mesh)
#
# print(can_win(board_mesh, 2))
# print(can_win(board_mesh, 1))
# print("")
print(start)
slvr = solver()
slvr.solve(board_mesh, 2, 10)
end = time.time()
print("execution time is : ",end - start)
