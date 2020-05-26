# Tic Tac Toe Game Logic

Use the functions we created to make a functional game! Flesh out the game loop with calls to the
functions and check the board status after each move.

If you feel ambitious, add error checking. If you want to go nuts, add unit test cases!

Start with the code-so-far here:

```python
board = [' '] * 9

def print_board():
    #print(board)
    print(board[0]+'|'+board[1]+'|'+board[2])
    print('-+-+-')
    print(board[3]+'|'+board[4]+'|'+board[5])
    print('-+-+-')
    print(board[6]+'|'+board[7]+'|'+board[8])

def get_move(token):
    print_board()
    print('Your move player',token)
    m = input('Where do you want to go? ')
    m = int(m)
    # TODO: error checking
    return m

def set_token(token,spot):
    board[spot] = token
    # TODO: error checking, unit tests

def get_token(spot):
    return board[spot]
    # TODO: error checking, unit tests
    
def _check_token(t):
    if board[0]==t and board[1]==t and board[2]==t:
        return True # Top row
    if board[3]==t and board[4]==t and board[5]==t:
        return True # Middle row
    if board[6]==t and board[7]==t and board[8]==t:
        return True # Bottom row
    if board[0]==t and board[3]==t and board[6]==t:
        return True # Left column
    if board[1]==t and board[4]==t and board[7]==t:
        return True # Middle column
    if board[2]==t and board[5]==t and board[8]==t:
        return True # right column
    if board[0]==t and board[4]==t and board[8]==t:
        return True # Upper left to bottom right
    if board[2]==t and board[4]==t and board[6]==t:
        return True # Upper right to bottom left
    
def get_status():
    if _check_token('X'):
        return 'X won'
    if _check_token('O'):
        return 'O won'
    if ' ' in board:
        return 'Playing'
    else:
        return 'Tie'

while True:
    # TODO: your code here!
    pass
```