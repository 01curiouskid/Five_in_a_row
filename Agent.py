from game import game
import math
import random
from EvaluationFunction import evaluationFunction

class MinimaxAgent:
    def __init__(self):
        self.evaluation_function = evaluationFunction()

    def minimax(self, board, depth, maximizingPlayer, gameState, alpha=-math.inf, beta=math.inf):
    
	 if depth == 0 or gameState.isTerminalNode(board):
            if gameState.isTerminalNode(board):
                # Evaluate the terminal state
                if gameState.winning_move(board, gameState.AI_PIECE):
                    return None, 10000000  # Large reward for winning AI
                elif gameState.winning_move(board, gameState.PLAYER_PIECE):
                    return None, -10000000  # Large penalty for losing AI
                else:
                    return None, 0  # Tie

            else:  # Non-terminal state (evaluate using evaluation function)
                score = self.evaluation_function.score_positions(board, gameState.AI_PIECE, gameState)
                return None, score

        # Maximizing Player (explore all valid moves)
        if maximizingPlayer:
            value = -math.inf
            best_column = None
            for col in gameState.get_valid_locations(board):
                row = gameState.get_next_open_row(board, col)
                b_copy = board.copy()
                gameState.drop_piece(b_copy, row, col, gameState.AI_PIECE)
                _, new_score = self.minimax(b_copy, depth - 1, False, gameState, alpha, beta)
                if new_score > value:
                    value = new_score
                    best_column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    return best_column, value  # Beta cut-off

        # Minimizing Player
        else:
            value = math.inf
            best_column = None
            for col in gameState.get_valid_locations(board):
                row = gameState.get_next_open_row(board, col)
                b_copy = board.copy()
                gameState.drop_piece(b_copy, row, col, gameState.PLAYER_PIECE)
                _, new_score = self.minimax(b_copy, depth - 1, True, gameState, alpha, beta)
                if new_score < value:
                    value = new_score
                    best_column = col
                beta = min(beta, value)
                if beta <= alpha:
                    return best_column, value  # Alpha cut-off

        return best_column, value

class AlphaBetaAgent:
    pass
