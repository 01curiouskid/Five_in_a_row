from game import game
import math
import random

class evaluationFunction:

    def __init__(self):
        pass

    def evaluate_window(self, window, piece, gameState: game):
        opp_piece = gameState.PLAYER_PIECE
        score=0
        if piece == gameState.PLAYER_PIECE:
            opp_piece = gameState.AI_PIECE
        if window.count(piece) == 5:
            score+=100
        elif window.count(piece) == 4 and window.count(gameState.EMPTY) == 1:
            score += 5
        elif window.count(piece) == 3 and window.count(gameState.EMPTY) == 2:
            score += 2
        if window.count(opp_piece) == 4 and window.count(gameState.EMPTY) == 1:
            score -= 6

        return score
    

    def score_positions(self, board, piece, gameState: game):
        score = 0
        # score centre column
        center_array = [i for i in list(board[:, gameState.COLUMN_COUNTS//2])]
        center_count = center_array.count(piece)
        score += center_count * 3

        #giving scores to horizontal
        for r in range(gameState.ROW_COUNTS):
            row_array = [i for i in board[r,:]]
            for c in range(gameState.COLUMN_COUNTS-4):
                window = row_array[c:c+gameState.WINDOW_LENGTH]
                score += self.evaluate_window(window, piece, gameState)

        #score vertical
        for c in range(gameState.COLUMN_COUNTS):
            col_array=[i for i in list(board[:,c])]
            for r in range(gameState.ROW_COUNTS-4):
                window= col_array[r:r+gameState.WINDOW_LENGTH]
                score += self.evaluate_window(window, piece, gameState)

        # positive slope diagonals
                        
        for r in range(gameState.ROW_COUNTS-4):
            for c in range(gameState.COLUMN_COUNTS-4):
                window=[board[r+i][c+i] for i in range(gameState.WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece, gameState)

        # negatively slope diagonals
        
        for r in range(gameState.ROW_COUNTS-4):
            for c in range(gameState.COLUMN_COUNTS-4):
                window=[board[r+4-i][c+i] for i in range(gameState.WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece, gameState)
        
        return score