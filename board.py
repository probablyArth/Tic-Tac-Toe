def show_board(board):
    print('   |   |')
    print(' ' + board['top-l'] + ' | ' + board['top-m'] + ' | ' + board['top-r'])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board['mid-l'] + ' | ' + board['mid-m'] + ' | ' + board['mid-r'])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board['bot-l'] + ' | ' + board['bot-m'] + ' | ' + board['bot-r'])
    print('   |   |')

board = {"top-l": " ", "top-m": ' ', "top-r": ' ',
         'mid-l': " ", "mid-m": ' ', "mid-r": ' ',
         'bot-l': " ", "bot-m": ' ', "bot-r": ' '}