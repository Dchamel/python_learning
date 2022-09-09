#Notice 1
#this program for my student to learn refactoring

import random
from random import choice

rules = '''How to play.
Input number of the position from 0-8
 0 | 1 | 2 
 -----------
 3 | 4 | 5 
 -----------
 6 | 7 | 8 
 ==================='''

board = {}
boardForPc = {}

def choseChips():
    '''Chose of the Chips'''
    userChips = ''
    while userChips not in ('X','O'):
        userChips = input('Chose your Chips(X or O): ').capitalize()
    if userChips == 'X':
        compChips = 'O'
    else:
        compChips = 'X'

    return userChips, compChips

def emptyField():
    for i in range(9):
        board[i] = SPACE
    boardForPc = dict(board)
    return board, boardForPc

def field(board):
    '''shows board'''
    print(f' {"0" if board[0] == " " else board[0]} | {"1" if board[1] == " " else board[1]} | {"2" if board[2] == " " else board[2]} ')
    print('-----------')
    print(f' {"3" if board[3] == " " else board[3]} | {"4" if board[4] == " " else board[4]} | {"5" if board[5] == " " else board[5]} ')
    print('-----------')
    print(f' {"6" if board[6] == " " else board[6]} | {"7" if board[7] == " " else board[7]} | {"8" if board[8] == " " else board[8]} ')

def userMove(userChips, board, boardForPc):
    move = ''
    while move not in range(9) or board[move] in ('X', 'O'):
        move = int(input('Make your move (0-8): '))
    board[move] = userChips
    del boardForPc[move]

    return board, boardForPc

def compMove(compChips, board, boardForPc):
    move = choice(list(boardForPc.keys()))
    board[move] = compChips
    del boardForPc[move]

    return board, boardForPc

def winDrawCheck(board):
    winCompositions = ((0,1,2),
                   (3,4,5),
                   (6,7,8),
                   (0,3,6),
                   (1,4,7),
                   (2,5,8),
                   (0,4,8),
                   (2,4,6))

    for i in winCompositions:
        if board[i[0]] == board[i[1]] == board[i[2]] != SPACE:
            winner = board[i[0]]
            # print(winner)
            return winner

    if SPACE not in board.values():
        print(board)
        return 'Draw'

    return None


def theGame(userChips, compChips, board, boardForPc):
    print('Free moves')
    field(board)
    board, boardForPc = userMove(userChips, board, boardForPc)
    winner = winDrawCheck(board)
    if winner:
        print(winner)
        return winner
    board, boardForPc = compMove(compChips, board, boardForPc)
    winner = winDrawCheck(board)
    if winner:
        print(winner)
        return winner
    # print(board)
    # print(boardForPc)
    field(board)
    return None


SPACE = ' '
print(rules)
board, boardForPc = emptyField()
userChips, compChips = choseChips()
winner = None
while winner is None:
    winner = theGame(userChips, compChips, board, boardForPc)
print(f'The winner is - "{winner}"')
# field(board)
