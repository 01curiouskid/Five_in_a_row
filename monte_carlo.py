import math
import random
from game import game
from EvaluationFunction import evaluationFunction

class MonteCarloAgent:
    def __init__(self, simulations=100):
        self.simulations = simulations
        self.evaluation_function = evaluationFunction()

    def monte_carlo_search(self, board, gameState):
        root = Node(board, None, gameState)

        for _ in range(self.simulations):
            node = root
            temp_game_state = gameState.copy()
            temp_board = board.copy()

            # Selection phase
            while not node.is_terminal():
                if not node.is_fully_expanded():
                    node = node.expand()
                    break
                else:
                    node = node.select_child()

            # Simulation phase
            winner = node.simulate(temp_board, temp_game_state)

            # Backpropagation phase
            while node is not None:
                node.update(winner)
                node = node.parent

        # Choose the best move based on the most visited child
        return root.best_child().move


class Node:
    def __init__(self, board, move, game_state, parent=None):
        self.board = board
        self.move = move
        self.game_state = game_state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.wins = 0

    def is_terminal(self):
        return self.game_state.isTerminalNode(self.board)

    def is_fully_expanded(self):
        return len(self.children) == len(self.game_state.get_valid_locations(self.board))

    def expand(self):
        valid_moves = self.game_state.get_valid_locations(self.board)
        for move in valid_moves:
            temp_board = self.board.copy()
            temp_game_state = self.game_state.copy()
            row = temp_game_state.get_next_open_row(temp_board, move)
            temp_game_state.drop_piece(temp_board, row, move, temp_game_state.AI_PIECE)
            self.children.append(Node(temp_board, move, temp_game_state, self))
        return random.choice(self.children)

    def select_child(self):
        C = 1.414  # Exploration parameter
        selected_child = None
        max_uct = -math.inf

        for child in self.children:
            uct = (child.wins / child.visits) + C * math.sqrt(math.log(self.visits) / child.visits)
            if uct > max_uct:
                max_uct = uct
                selected_child = child

        return selected_child

    def simulate(self, board, game_state):
        temp_board = board.copy()
        temp_game_state = game_state.copy()
        while not temp_game_state.isTerminalNode(temp_board):
            valid_moves = temp_game_state.get_valid_locations(temp_board)
            random_move = random.choice(valid_moves)
            row = temp_game_state.get_next_open_row(temp_board, random_move)
            temp_game_state.drop_piece(temp_board, row, random_move, temp_game_state.AI_PIECE)

            if temp_game_state.isTerminalNode(temp_board):
                return temp_game_state.get_winning_piece(temp_board)

        return 0  # Tie

    def update(self, winner):
        self.visits += 1
        if winner == self.game_state.AI_PIECE:
            self.wins += 1

    def best_child(self):
        return max(self.children, key=lambda x: x.visits)


# Usage
if __name__ == "__main__":
    board = ...  # Initialize game board
    game_state = ...  # Initialize game state
    agent = MonteCarloAgent()
    best_move = agent.monte_carlo_search(board, game_state)
    print("Best Move:", best_move)

