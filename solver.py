import numpy

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
    	if (move_j >= 0 and move_j <= 6):
    		if (node[5, move_j] == 0):
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
        return (count + 1 - 42)/2

    def get_position_on_board(self, move_j, board_mesh):
    	move_i = 0;
    	for i in range(7):
    		if (board_mesh[i, move_j] == 0):
    			move_i = i
    			break
    	return move_i;

    def Negamax(self, node, turn):
        if self.isTerminal(node):
            return 0;
        # for(int x = 0; x < Position::WIDTH; x++) # check if current player can win next move
        #     if(P.canPlay(x) && P.isWinningMove(x))
        #         return (Position::WIDTH*Position::HEIGHT+1 - P.nbMoves())/2;
        for i in range(7):
            if not self.is_viable_action(i, node):
                print("This is not available")
                continue;
            else:
                parent = node
                parent[self.get_position_on_board(i, parent), i] = turn
                child = parent
                if self.can_win(child, turn):
                    self.visualize(child);
                    return self.eval_function(child)

        value = -42
        for i in range(7):
            if not self.is_viable_action(i, node):
                continue;
            parent = node
            parent[self.get_position_on_board(i, node), i] = turn
            child = parent
            val = max(value, -self.Negamax(child, (turn)%2))
            if (val > value):
                value = val
        return value

    def solve(self, board_mesh, turn):
        self.board_mesh = board_mesh
        self.turn = turn
        print(self.Negamax(board_mesh, turn))
