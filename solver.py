import numpy

class solver:
    def __init__(self):
        pass

    def winning_Condition(board_mesh,player_number):
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

    def Negamax(self):
        if len(self.state) == 42:
            return 0;
        print(len(self.state))
        print(self.player_number)

    def solve(self, state, board_mesh, player_number):
        self.state = state
        self.board_mesh = board_mesh
        self.player_number = player_number
        self.Negamax();
