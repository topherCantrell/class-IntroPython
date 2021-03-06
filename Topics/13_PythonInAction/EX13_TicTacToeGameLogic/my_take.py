board = [' '] * 9

def print_board():    
    print(board[0]+'|'+board[1]+'|'+board[2])
    print('-+-+-')
    print(board[3]+'|'+board[4]+'|'+board[5])
    print('-+-+-')
    print(board[6]+'|'+board[7]+'|'+board[8])

def get_move(token):
    while True:
        print_board()
        print('Your move player',token)
        m = input('Where do you want to go? ')
        try:
            m = int(m)
            if m>=0 and m<=8 and get_token(m)==' ':
                return m            
        except Exception:
            pass
        print('Invalid input')        

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
    m = get_move('X')
    set_token('X',m)
    s = get_status()
    if s != 'Playing':
        break
    m = get_move('O')
    set_token('O',m)
    s = get_status()
    if s != 'Playing':
        break
    
print_board()
print(s)
 