def player_move(board):
    turn = 'X'
    plr_move = input("Turn for " + turn + "Where do you want to place?")
    for x in board:
        if plr_move == x:
            board[x] = turn