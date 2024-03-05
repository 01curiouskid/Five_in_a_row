# Importing Python modules
import numpy as np
 
# Declaraing Global variables
TARGET = 5 # minimum of dots that should be in a row to game to finish
ROW_COUNTS = 8  # number of Rows in a board
COLUMN_COUNTS = 9 # number of Columns in a board


"""
Creating Board using matrix with initial values 0.
"""
def create_board():
    board = np.zeros((ROW_COUNTS,COLUMN_COUNTS))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece


"""
Finding first open position i.e. 0 in this case, in the particular column col, and replacing it with 1 or 2
"""
def get_next_open_row(board,col):
    for r in range(ROW_COUNTS):
        if board[r][col] == 0:
            return r

"""
Checking input from user is valid or not
"""
def is_valid_location(board,col):
    return board[ROW_COUNTS - 1][col] == 0

"""
This function is called in order to print the board
"""
def print_board(board):
    print(np.flip(board,0))

"""
Everytime player 1 or 2 make their move this function checks whether winning condition is met or not, if condition is fullfilled, loops end there.
"""
def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNTS - TARGET + 1):
        for r in range(ROW_COUNTS):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece and board[r][c+4] == piece:
                return True
    # Check vertical locations for win
    for r in range(ROW_COUNTS - TARGET + 1):
        for c in range(COLUMN_COUNTS):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece and board[r+4][c] == piece:
                return True
    # Check positively sloped diagonals
    for c in range(COLUMN_COUNTS - TARGET + 1):
        for r in range(ROW_COUNTS - TARGET + 1):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece and board[r+4][c+4] == piece:
                return True
    # Check negatively sloped diagonals
    for c in range(COLUMN_COUNTS - TARGET + 1):
        for r in range(TARGET - 1, ROW_COUNTS):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece and board[r-4][c+4] == piece:
                return True

    

board = create_board() # create board
print_board(board) # print board on terminal
game_over = False 
turn = 0 # its player1 turn if variable = 0 otherwise its player2 turn, variable remains 0 or 1 only

while not game_over:
    # Ask for Player1 i/p
    if turn == 0:
        col = int(input("Player 1 make your selection(0-8): "))

        if is_valid_location(board,col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)

            if winning_move(board,1):
                print("Player1 won !! Congrats !!")
                game_over = True
    # Ask for Player2 i/p
    else:
        col = int(input("Player 2 make your selection(0-8): "))

        if is_valid_location(board,col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

            if winning_move(board,2):
                print("Player2 won !! Congrats !!")
                game_over = True
           
    print_board(board)
    turn += 1
    turn = turn % 2




