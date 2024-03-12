from game import game
import math
import random
from EvaluationFunction import evaluationFunction

class MinimaxAgent():

    def __init__(self):
        self.evaluation_function=evaluationFunction()
        pass


    def minimax(self, board, depth, maximizingPlayer, gameState: game):
        if depth == 0 or gameState.isTerminalNode(board):
            if gameState.isTerminalNode(board):
                if gameState.winning_move(board,gameState.AI_PIECE):
                    return None, 10000000
                elif gameState.winning_move(board, gameState.PLAYER_PIECE):
                    return None, -10000000
                else:
                    return None, 0
            else:
                obj=self.evaluation_function
                return None, obj.score_positions(board, gameState.AI_PIECE, gameState)
        
        if maximizingPlayer:
            value = -math.inf
            column = random.choice(gameState.get_valid_locations(board))
            for col in gameState.get_valid_locations(board):
                row = gameState.get_next_open_row(board, col)
                b_copy = board.copy()
                gameState.drop_piece(b_copy, row, col, gameState.AI_PIECE)
                new_score = self.minimax(b_copy, depth-1, False, gameState)[1]
                if new_score > value:
                    value = new_score
                    column = col
            return column, value
            
        else:
            value = math.inf
            column = random.choice(gameState.get_valid_locations(board))
            for col in gameState.get_valid_locations(board):
                row = gameState.get_next_open_row(board, col)
                b_copy = board.copy()
                gameState.drop_piece(b_copy, row, col, gameState.PLAYER_PIECE)
                new_score = self.minimax(b_copy, depth-1, True, gameState)[1]
                if new_score < value:
                    value = new_score
                    column = col
            return column, value
        


# inst=MinimaxAgent()
        
class AlphaBetaAgent:
    pass