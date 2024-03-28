import game
import pygame
import math
import sys
import Agent

# Define global variables for scores
player_score = 0
ai_score = 0

# Function to run the game loop and return the winner
def run_game():
    global player_score, ai_score

    game_instance = game.game()
    MM = Agent.MinimaxAgent()
    AB = Agent.AlphaBetaAgent()

    board = game_instance.create_board()  # create board
    game_instance.draw_board(board)
    pygame.display.update()

    while not game_instance.game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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

        # Display scores on screen
        font = pygame.font.SysFont(None, 25)
        player_score_text = font.render(f'Player1 Score: {player_score}', True, (255, 255, 255))
        ai_score_text = font.render(f'Player2 Score: {ai_score}', True, (255, 255, 255))
        game_instance.screen.blit(player_score_text, (20, 20))
        game_instance.screen.blit(ai_score_text, (190, 20))
        pygame.display.flip()

    # Return the winner of the game
    if player_score > ai_score:
        return "Player1"
    elif ai_score > player_score:
        return "Player2"
    else:
        return "It's a tie!"

# Initialize scores
player1_total_score = 0
player2_total_score = 0

# Run the game loop 5 times
for i in range(5):
    winner = run_game()
    print(f"Game {i+1} Winner: {winner}")
    if winner == "Player1":
        player1_total_score += 1
    elif winner == "Player2":
        player2_total_score += 1

    # Display total scores after each game
    print(f"Total scores after {i+1} games - Player1: {player1_total_score}, Player2: {player2_total_score}")

# Print final total scores after 5 games
print(f"Final Total scores after 5 games - Player1: {player1_total_score}, Player2: {player2_total_score}")
