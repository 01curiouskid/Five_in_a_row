import game
import pygame
import math
import sys
from Agent import MinimaxAgent


game_instance=game.game()
MM=MinimaxAgent()


board = game_instance.create_board() # create board

while not game_instance.game_over:

    if game_instance.turn == game_instance.PLAYER:
       
        col= int(input("PLayer 1 enter your choice(0-8): "))
        if game_instance.is_valid_location(board,col):
            row = game_instance.get_next_open_row(board, col)
            game_instance.drop_piece(board, row, col, game_instance.PLAYER_PIECE)
            if game_instance.winning_move(board,game_instance.PLAYER_PIECE):
                print("Player1 won !! Congrats !!")
                game_instance.game_over = True
        game_instance.print_board(board)

        game_instance.turn += 1
        game_instance.turn = game_instance.turn % 2

    # Ask for Player2 i/p
    if game_instance.turn == game_instance.AI:
        col, minimax_score = MM.minimax(board, 3, True, game_instance)
        if game_instance.is_valid_location(board,col):
            row = game_instance.get_next_open_row(board, col)
            game_instance.drop_piece(board, row, col, game_instance.AI_PIECE) 
            if game_instance.winning_move(board, game_instance.AI_PIECE):
                print("Player2 won !! Congrats !!")
                game_instance.game_over = True
                
            game_instance.print_board(board)

            game_instance.turn += 1
            game_instance.turn = game_instance.turn % 2

