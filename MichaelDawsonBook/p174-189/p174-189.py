def unnamed(q,w):
    print(f'q+w = {q + w}')

unnamed(1,2)

def named(q=1,w=2):
    print(f'q+w = {q + w}')
named(2)
named(w=4)
named(q='1',w='2')

#tic tac toe - the game (teaches how to use pseudocode)

# pseudocode
#
# instructions
# first step
# create an empty board
# view this board
# while draw or somb win
#     if user turn
#         get position from user
#         redraw board view
#     else
#         math computer move
#         redraw board view
#     view new board
#     change turn
# congrads the winner

def display_instruct() #show instruction
    '''Instruction for the player'''
    print('''Welcome to Tic-Tac-Toe Game
     0 | 1 | 2 
    -----------
     3 | 4 | 5 
    -----------
     6 | 7 | 8 
    ''')

def ask_yes_no(question):
    '''take text of question, ask user somth, return - y/n'''
    response = ''
    while response not in ('y','n','yes','no'):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    '''ask user for number in range, return - integer'''
    response = ''
    while response not in range(low, high):
        response = int(input(question))
    return response

def pieces():
    '''whose first move'''
    go_first = ask_yes_no('Do you want to do the First Move ? (y/n): ')
    if go_first in ('y','yes'):
        print('OK. Play with X ')
        human = X
        computer = O
    else:
        print('So. My turn than. You next.')
        computer = X
        human = O
    return computer, human

def new_board():
    '''empty board and return it'''
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    '''shows board'''
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('-----------')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('-----------')
    print(f' {board[6]} | {board[7]} | {board[8]} ')

def legal_moves(board):
    '''Takes board, return - list of moves'''
    moves=[]
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    '''shows the winner. Takes board, return - type of chips'''
    WAYS_TO_WIN = ((0,1,2),
                   (3,4,5),
                   (6,7,8),
                   (0,3,6),
                   (1,4,7),
                   (2,5,8),
                   (0,4,8),
                   (2,4,6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None

def human_move(board, human):
    '''input player move'''
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number('Your move. Chose from (0-8): ', 0, NUM_SQUARES)
        if move not in legal:
            print('This field is busy already')
    print('Okay...')
    return move

computer_move(board, computer, human) #calc computer move
next_turn(turn) #takes type of chips and return it
congrat_winner(the_winner, computer, human) #congrats the winner

X = 'X'
O = 'O'
EMPTY = ' '
TIE = 'Draw'
NUM_SQUARES = 9
