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

# Function to draw buttons for board size selection
def draw_board_size_selection():
    # Load background image
    background_image = pygame.image.load('background_image.png')
    screen.blit(background_image, (0, 0))

    # Draw buttons for board size selection with rounded rectangles
    button_color = (255, 0, 0)  # Red
    button_hover_color = (200, 0, 0)  # Darker red on hover
    font = pygame.font.Font('freesansbold.ttf', 32)

    # Small button
    small_button_rect = pygame.Rect(50, 100, 200, 50)
    pygame.draw.rect(screen, button_color, small_button_rect, border_radius=5)
    small_text = font.render("Small (6x7)", True, (255, 255, 255))
    small_text_rect = small_text.get_rect(center=small_button_rect.center)
    screen.blit(small_text, small_text_rect)

    # Medium button
    medium_button_rect = pygame.Rect(50, 200, 200, 50)
    pygame.draw.rect(screen, button_color, medium_button_rect, border_radius=5)
    medium_text = font.render("Medium (8x9)", True, (255, 255, 255))
    medium_text_rect = medium_text.get_rect(center=medium_button_rect.center)
    screen.blit(medium_text, medium_text_rect)

    # Large button
    large_button_rect = pygame.Rect(50, 300, 200, 50)
    pygame.draw.rect(screen, button_color, large_button_rect, border_radius=5)
    large_text = font.render("Large (10x11)", True, (255, 255, 255))
    large_text_rect = large_text.get_rect(center=large_button_rect.center)
    screen.blit(large_text, large_text_rect)

    pygame.display.update()

# Function to run the game loop and return the winner
def run_game(board_size):
    player_score = 0
    ai_score = 0

    game_instance = game.game(board_size)  # Use game instead of Game
    MM = Agent.MinimaxAgent()
    AB = Agent.AlphaBetaAgent()

    board = game_instance.create_board()  # create board
    game_instance.draw_board(board)
    pygame.display.update()

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
                        game_instance.print_board(board)
                        game_instance.draw_board(board)
                        game_instance.turn += 1
                        game_instance.turn = game_instance.turn % 2

            # Ask for AI input
            if game_instance.turn == game_instance.AI and not game_instance.game_over:
                col, minimax_score = AB.alphabeta(board, 4, True, game_instance)
                if game_instance.is_valid_location(board, col):
                    row = game_instance.get_next_open_row(board, col)
                    game_instance.drop_piece(board, row, col, game_instance.AI_PIECE)
                    if game_instance.winning_move(board, game_instance.AI_PIECE):
                        print("Player2 won !! Congrats !!")
                        ai_score += 1  # Increment AI score
                        game_instance.game_over = True

                    game_instance.print_board(board)
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

# Call the function to draw the board size selection
draw_board_size_selection()

# Variable to hold the selected board size
board_size = None

# Event loop for selecting board size
while board_size is None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if 50 <= mouse_pos[0] <= 250:
                if 100 <= mouse_pos[1] <= 150:
                    board_size = 6, 7
                elif 200 <= mouse_pos[1] <= 250:
                    board_size = 8, 9
                elif 300 <= mouse_pos[1] <= 350:
                    board_size = 10, 11

# Run the game loop
run_game(board_size)

# Quit pygame
pygame.quit()
