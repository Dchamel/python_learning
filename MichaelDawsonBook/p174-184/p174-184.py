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

display_instruct() #show instruction
ask_yes_no(question) #take text of question, ask user somth, res - y/n
ask_number(question, low, high) #ask user for number in range, return - integer
pieces() #whose first move
new_board() #empty board and return it
display_board(board) #shows board
legal_moves(board) #Takes board, return - list of moves
winner(board) #shows the winner. Takes board, return - type of chips
human_move(board, human) #input player move
computer_move(board, computer, human) #calc computer move
next_turn(turn) #takes type of chips and return it
congrat_winner(the_winner, computer, human) #congrats the winner

