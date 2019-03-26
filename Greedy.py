import numpy as np
def get_position_on_board(move_j, board_mesh):
	move_i = 0
	for i in range(6):
		if (board_mesh[i, move_j] == 0):
			move_i = i
			break
	return move_i

def greedy_score(board_mesh,player_number):
    Num_4=0
    Num_3=0
    Num_2=0
    if player_number%2 ==1 : player_number =1
    else: player_number = 2
    ################ 4 Piece
    #Horizaontal
    for columns in range(0,4):
        for rows in range(0,6):
            if board_mesh[rows][columns]==board_mesh[rows][columns+1]==board_mesh[rows][columns+2]==board_mesh[rows][columns+3]==player_number:
                Num_4=Num_4+1
    #Vertical
    for columns in range(0,7):
        for rows in range (0,3):
            if board_mesh[rows][columns]==board_mesh[rows+1][columns]==board_mesh[rows+2][columns]==board_mesh[rows+3][columns]==player_number:
                Num_4=Num_4+1	
    #Positive Diag
    for columns in range(0,4):
        for rows in range (0,3):
            if board_mesh[rows][columns]==board_mesh[rows+1][columns+1]==board_mesh[rows+2][columns+2]==board_mesh[rows+3][columns+3]==player_number:
                Num_4=Num_4+1
    #Negative Diag
    for columns in range(0,4):
        for rows in range (3,6):
            if board_mesh[rows][columns]==board_mesh[rows-1][columns+1]==board_mesh[rows-2][columns+2]==board_mesh[rows-3][columns+3]==player_number:
                Num_4=Num_4+1	

    ################ 3 Piece
    #Horizaontal
    for columns in range(0,5):
        for rows in range (0,6):
            if board_mesh[rows][columns]==board_mesh[rows][columns+1]==board_mesh[rows][columns+2]==player_number:
                Num_3=Num_3+1
    #Vertical
    for columns in range(0,7):
        for rows in range (0,4):
            if board_mesh[rows][columns]==board_mesh[rows+1][columns]==board_mesh[rows+2][columns]==player_number:
                Num_3=Num_3+1	
    #Positive Diag
    for columns in range(0,5):
        for rows in range (0,4):
            if board_mesh[rows][columns]==board_mesh[rows+1][columns+1]==board_mesh[rows+2][columns+2]==player_number:
                Num_3=Num_3+1
    #Negative Diag
    for columns in range(0,5):
        for rows in range (2,6):
            if board_mesh[rows][columns]==board_mesh[rows-1][columns+1]==board_mesh[rows-2][columns+2]==player_number:
                Num_3=Num_3+1	




    ################ 2 Piece
    #Horizaontal
    for columns in range(0,6):
        for rows in range (0,6):
            if board_mesh[rows][columns]==board_mesh[rows][columns+1]==player_number:
                Num_2=Num_2+1
    #Vertical
    for columns in range(0,7):
        for rows in range (0,5):
            if board_mesh[rows][columns]==board_mesh[rows+1][columns]==player_number:
                Num_2=Num_2+1
    #Positive Diag
    for columns in range(0,6):
        for rows in range (0,5):
            if board_mesh[rows][columns]==board_mesh[rows+1][columns+1]==player_number:
                Num_2=Num_2+1
    #Negative Diag
    for columns in range(0,6):
        for rows in range (1,6):
            if board_mesh[rows][columns]==board_mesh[rows-1][columns+1]==player_number:
                Num_2=Num_2+1	
    print("Num 2 : ",Num_2,"Num 3 : ",Num_3,"Num 4 : ",Num_4)
    Num_2_Weight = 1
    Num_3_Weight = 4
    Num_4_Weight = 10000
    score= Num_2*Num_2_Weight + Num_3*Num_3_Weight + Num_4*Num_4_Weight
    return score 
def is_viable_action(move_j, board_mesh):
	if (move_j >= 0 and move_j <= 6):
		if (board_mesh[5][move_j] == 0):
			return True
	else:
		return False

def greedy_search(board_mesh,player_number,get_position_on_board,greedy_score,is_viable_action):
    #player_number=player_number+1
    if player_number== 1: player_number = 1
    elif player_number==0 : player_number = 2
    column_score = [0,0,0,0,0,0,0]
    board_mesh_new = board_mesh
    for i in range(0,7):
        board_mesh_new = np.zeros((6,7))
        board_mesh_new = board_mesh
        move_row = get_position_on_board(i,board_mesh)
        if is_viable_action(i,board_mesh_new) :
            board_mesh_new[move_row][i]=player_number
            print("Number of Stones for Column ( %c )",i)
            score= greedy_score(board_mesh_new,player_number)
            board_mesh_new[move_row][i]=0
            column_score[i]=score
            turn=player_number%2+1

        else:
            #board_mesh_new[move_row][i]=player_number
            score= greedy_score(board_mesh_new,player_number)
            #board_mesh_new[move_row][i]=0
            column_score[i]=score
    print(column_score)
    occurences = np.argwhere(column_score == np.amax(column_score))
    all_values = occurences.flatten().tolist()
    Greedy_index = np.random.choice(all_values)
    print("Max Value is : ",Greedy_index)
    return Greedy_index,turn

A= np.zeros((6,7))
A[0][0]=0
A[1][0]=0
A[2][0]=0
A[3][0]=0
A[4][0]=0
A[5][0]=0

A[0][1]=0
A[0][2]=0
A[0][3]=1
Score = greedy_score(A,1)
print("Score is : " ,Score)
greedy_search(A,1,get_position_on_board,greedy_score,is_viable_action)