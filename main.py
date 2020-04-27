# Tic Tac Toe lol
from board import show_board, board
from player_move import player_move

possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
print(possibleMoves)
show_board(board)
player_move(board)
show_board(board)