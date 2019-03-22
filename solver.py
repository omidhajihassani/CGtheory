import numpy as np
countr = 0
columnOrder = np.array([4, 5, 3, 6, 2, 1, 7])
moves = np.zeros(7, float);
class solver:
    def __init__(self):
        pass

    def can_win(self, board_mesh,player_number):
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

    def isTerminal(self, node):
        count = 0
        for i in range(6):
            for j in range(7):
                if node[i, j] != 0:
                        count = count + 1;
        if count == 42:
            return True
        else:
            return False

    def is_viable_action(self, move_j, node):
    	if node[5, move_j] == 0:
    		return True
    	else:
    		return False

    def visualize(self, board_mesh):
    	i = 5;
    	j = 0;
    	while i != -1:
    		while j != 7:
    			print(str(board_mesh[i, j]), end = ' ', flush=True);
    			j = j + 1;
    		print("")
    		i = i - 1;
    		j = 0;

    def eval_function(self, node):
        count = 0
        for i in range(6):
            for j in range(7):
                if node[i, j] != 0:
                        count = count + 1;
        return (42 - count)
        # return (42 + 1 - count)/2

    def get_position_on_board(self, move_j, board_mesh):
    	move_i = 0;
    	for i in range(7):
    		if (board_mesh[i, move_j] == 0):
    			move_i = i
    			break
    	return move_i;

    def Negamax(self, node, turn, depth):
        global countr
        countr = countr + 1

        if depth == 0:
            return 0
        if turn == 1:
            nexturn = 2
        if turn == 2:
            nexturn = 1
        if self.isTerminal(node):
            return 0;

        for j in range(7):
            i = columnOrder[j] - 1;
            if self.is_viable_action(i, node):
                parent = np.copy(node)
                parent[self.get_position_on_board(i, parent), i] = turn
                child = parent
                if self.can_win(child, turn):
                    print("%%%%%%%%%%%%%%%%%%%%%%%%%")
                    print("depth is "+str(depth))
                    print("%%%%%%%%%%%%%%%%%%%%%%%%%")
                    print(str(turn)+" has won the game")
                    self.visualize(child);
                    print()
                    print(self.eval_function(child))
                    return self.eval_function(child)
        value = -42

        for j in range(7):
            i = columnOrder[j] - 1;
            if self.is_viable_action(i, node):
                # print("%%%%%%%%%%%%%%%%%%%%%%%%%")
                # print("depth is "+str(depth))
                # print("%%%%%%%%%%%%%%%%%%%%%%%%%")
                parent = np.copy(node)
                parent[self.get_position_on_board(i, parent), i] = turn
                child = np.copy(parent)
                # self.visualize(child)
                # print()
                valv = -self.Negamax(child, nexturn, depth - 1)
                # print (valv)
                val = max(value, valv)
                if (val > value):
                    value = val
        return value

    def Negamax_wab(self, node, turn, depth, alpha, beta):
        global countr
        countr = countr + 1
        if alpha > beta:
            return False
        if depth == 0:
            return 0
        if turn == 1:
            nexturn = 2
        if turn == 2:
            nexturn = 1
        if self.isTerminal(node):
            return 0;

        for j in range(7):
            i = columnOrder[j] - 1;
            if self.is_viable_action(i, node):
                parent = np.copy(node)
                parent[self.get_position_on_board(i, parent), i] = turn
                child = parent
                if self.can_win(child, turn):
                    print("%%%%%%%%%%%%%%%%%%%%%%%%%")
                    print("depth is "+str(depth))
                    print("%%%%%%%%%%%%%%%%%%%%%%%%%")
                    print(str(turn)+" has won the game")
                    self.visualize(child);
                    print()
                    if depth == 7:
                        moves[i] = self.eval_function(child);
                    return self.eval_function(child)

        max = self.eval_function(child)
        if beta > max:
            beta = max;                     # there is no need to keep beta above our max possible score.
        if alpha >= beta:
            return beta;                    # prune the exploration if the [alpha;beta] window is empty.

        for j in range(7):
            i = columnOrder[j] - 1;
            if self.is_viable_action(i, node):
                print("%%%%%%%%%%%%%%%%%%%%%%%%%")
                print("depth is "+str(depth))
                print("%%%%%%%%%%%%%%%%%%%%%%%%%")
                parent = np.copy(node)
                parent[self.get_position_on_board(i, parent), i] = turn
                child = np.copy(parent)
                self.visualize(child)
                print()
                score = -self.Negamax_wab(child, nexturn, depth - 1, -beta, -alpha);
                if depth == 7:
                    moves[i] = score;
                if score >= beta:
                    return score
                if score > alpha:
                    alpha = score
            else:
                if depth == 7:
                    moves[i] = -100;
        return alpha

    def solve(self, board_mesh, turn, depth):
        global countr
        self.board_mesh = board_mesh
        self.turn = turn
        self.depth = depth
        print(self.Negamax(board_mesh, turn, depth))
        print("HIIII")
        print("Negamax: "+str(countr))
        countr = 0
        print(self.Negamax_wab(board_mesh, turn, depth, -12, 12))
        print("Negamax w alpha beta pruning: "+str(countr))
        print(moves)
        best_move = np.argmax(moves) + 1
        print(best_move)
