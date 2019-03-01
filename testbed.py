import numpy as np
from solver import solver

def visualize(board_mesh):
	i = 5;
	j = 1;
	while i != -1:
		while j != 7:
			print(str(board_mesh[i, j]), end = ' ', flush=True);
			j = j + 1;
		print("")
		i = i - 1;
		j = 1;

board_mesh = np.zeros((6,7), int)
# for i in range(6):
#     for j in range(7):
#         board_mesh[5-i, 6-j] = 1
board_mesh = np.array([[1, 1, 1, 2, 2, 2, 0],
                [1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0]])
# visualize(board_mesh)
slvr = solver()
slvr.solve(board_mesh, 1, 3)
