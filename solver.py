import numpy

class solver:
    def __init__(self):
        pass

    def position2state(state, move_j):
    	state.append(move_j);

    def eval_function(board_mesh,player_number):
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

    def eval():
        pass

    def isTerminal(node):
        for i in range(7):
            for j in range(6):
                if node[i, j] != 0:
                        count = count + 1;
        if count == 42:
            return True
        else
            return False

    def is_viable_action(move_j, node):
    	if (move_j >= 0 and move_j <= 6):
    		if (board_mesh[5, move_j] == 0):
    			return True
    	else:
    		return False

    def get_position_on_board(move_j, board_mesh):
    	move_i = 0;
    	for i in range(6):
    		if (board_mesh[i, move_j] == 0):
    			move_i = i
    			break
    	return move_i;

    def Negamax(self, node, turn):
        if isTerminal(node):
            return 0;

        for(int x = 0; x < Position::WIDTH; x++) # check if current player can win next move
            if(P.canPlay(x) && P.isWinningMove(x))
                return (Position::WIDTH*Position::HEIGHT+1 - P.nbMoves())/2;

        value = -42

        for i in range(7):
            if not is_viable_action(i, node):
                continue;
            parent = node
            child = (parent[get_position_on_board(i, node), i] = turn)
            val = max(value, -Negamax(child, -color, (turn)%2))
            if (val > value):
                value = val
        return value

    def solve(self, state, board_mesh, player_number):
        self.state = state
        self.board_mesh = board_mesh
        self.player_number = player_number
        self.Negamax();
