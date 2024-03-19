import game
import pygame
import math
import sys
import Agent


game_instance=game.game()
MM=Agent.MinimaxAgent()
AB=Agent.AlphaBetaAgent()


board = game_instance.create_board() # create board
game_instance.draw_board(board)
pygame.display.update()
while not game_instance.game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Ask for Player1 i/p
            if game_instance.turn == game_instance.PLAYER:
                posx = event.pos[0]
                col = int(math.floor( posx/game_instance.SQUARESIZE))
                # col= int(input("PLayer 1 enter your choice(0-8): "))
                if game_instance.is_valid_location(board,col):
                    row = game_instance.get_next_open_row(board, col)
                    game_instance.drop_piece(board, row, col, game_instance.PLAYER_PIECE)
                    if game_instance.winning_move(board,game_instance.PLAYER_PIECE):
                        print("Player1 won !! Congrats !!")
                        game_instance.game_over = True
                game_instance.print_board(board)
                game_instance.draw_board(board)
                game_instance.turn += 1
                game_instance.turn = game_instance.turn % 2

    # Ask for AI i/p
    # bug : when player1 won but game did not end
    # fix : added another condition "not game_instance.game_over"
    if game_instance.turn == game_instance.AI and not game_instance.game_over:
        posx = event.pos[0]
        col = int(math.floor( posx/game_instance.SQUARESIZE))
        col, minimax_score = AB.alphabeta(board, 4, True, game_instance)
        # game_instance.print_hello()
        if game_instance.is_valid_location(board,col):
            row = game_instance.get_next_open_row(board, col)
            game_instance.drop_piece(board, row, col, game_instance.AI_PIECE) 
            if game_instance.winning_move(board, game_instance.AI_PIECE):
                print("Player2 won !! Congrats !!")
                game_instance.game_over = True
                
            game_instance.print_board(board)
            game_instance.draw_board(board)
            game_instance.turn += 1
            game_instance.turn = game_instance.turn % 2

