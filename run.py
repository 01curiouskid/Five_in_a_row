import pygame
import math
import sys
import Agent
import game

# Initialize pygame
pygame.init()

# Set up the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Select Board Size")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define fonts
font = pygame.font.Font(None, 36)

# Global score variables
player_score = 0
ai_score = 0

# Function to draw buttons for board size selection
def draw_board_size_selection():
    # Load background image
    background_image = pygame.image.load('background_image.png')
    screen.blit(background_image, (0, 0))

    # Draw buttons for board size selection with rounded rectangles
    button_color = (255, 0, 0)  # Red
    button_hover_color = (200, 0, 0)  # Darker red on hover
    font = pygame.font.Font('freesansbold.ttf', 32)

    # List of board sizes and their corresponding scores
    board_sizes = [(6, 7), (8, 9), (10, 11)]

    # Draw buttons for board size selection
    for i, (rows, cols) in enumerate(board_sizes):
        button_rect = pygame.Rect(50, 100 + 100 * i, 200, 50)
        pygame.draw.rect(screen, button_color, button_rect, border_radius=5)
        text = font.render(f"{rows}x{cols}", True, (255, 255, 255))
        text_rect = text.get_rect(center=button_rect.center)
        screen.blit(text, text_rect)

    pygame.display.update()

    return board_sizes

# Function to run the game loop and return the winner
def run_game(board_size):
    global player_score, ai_score

    game_instance = game.game(board_size)  # Use game instead of Game
    MM = Agent.MinimaxAgent()
    AB = Agent.AlphaBetaAgent()
    MCST=Agent.MonteCarloAgent()

    board = game_instance.create_board()  # create board
    game_instance.draw_board(board)
    pygame.display.update()

    player_score = 0
    ai_score = 0

    for _ in range(5):  # Run for 5 rounds
        while not game_instance.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Ask for Player1 input
                    if game_instance.turn == game_instance.PLAYER:
                        posx = event.pos[0]
                        col = int(math.floor(posx / game_instance.SQUARESIZE))
                        if game_instance.is_valid_location(board, col):
                            row = game_instance.get_next_open_row(board, col)
                            game_instance.drop_piece(board, row, col, game_instance.PLAYER_PIECE)
                            if game_instance.winning_move(board, game_instance.PLAYER_PIECE):
                                print("Player1 won !! Congrats !!")
                                player_score += 1  # Increment player score
                                game_instance.game_over = True
                            if game_instance.is_draw(board):
                                game_instance.game_over = True
                        game_instance.print_board(board)
                        game_instance.draw_board(board)
                        game_instance.turn += 1
                        game_instance.turn = game_instance.turn % 2

            # Ask for AI input
            if game_instance.turn == game_instance.AI and not game_instance.game_over:
                col, minimax_score = AB.alphabeta(board, 4, True, game_instance)
                # col=MCST.monte_carlo_search(board,game_instance)
                if game_instance.is_valid_location(board, col):
                    row = game_instance.get_next_open_row(board, col)
                    game_instance.drop_piece(board, row, col, game_instance.AI_PIECE)
                    if game_instance.winning_move(board, game_instance.AI_PIECE):
                        print("Player2 won !! Congrats !!")
                        ai_score += 1  # Increment AI score
                        game_instance.game_over = True
                    if game_instance.is_draw(board):
                        game_instance.game_over = True

                    # game_instance.print_board(board)
                    game_instance.draw_board(board)
                    game_instance.turn += 1
                    game_instance.turn = game_instance.turn % 2

        # Display scores after each round
        screen.fill(BLACK)  # Clear the screen
        font = pygame.font.SysFont(None, 25)
        player_score_text = font.render(f'Player1 Score: {player_score}', True, WHITE)
        ai_score_text = font.render(f'Player2 Score: {ai_score}', True, WHITE)
        screen.blit(player_score_text, (20, 20))
        screen.blit(ai_score_text, (190, 20))
        pygame.display.flip()

        # Reset the game for the next round
        game_instance.game_over = False
        game_instance.turn = 0
        board = game_instance.create_board()
        game_instance.draw_board(board)
        pygame.display.update()

    return player_score, ai_score

# Call the function to draw the board size selection
board_sizes = draw_board_size_selection()

# Event loop for selecting board size
board_size = None
while board_size is None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for i, (rows, cols) in enumerate(board_sizes):
                if 50 <= mouse_pos[0] <= 250 and 100 + 100 * i <= mouse_pos[1] <= 100 + 100 * (i + 1):
                    board_size = (rows, cols)
                    break

# Run the game loop
player_score, ai_score = run_game(board_size)

# Print final scores
print(f"Final scores - Player1: {player_score}, Player2: {ai_score}")

# Quit pygame
pygame.quit()
