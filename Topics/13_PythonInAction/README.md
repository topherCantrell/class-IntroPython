# TicTacToe Example

Let's start with just basic functions ... no need to make it complicated.

Most of our work designing functions is the same thing we'll do for designing methods.

# Some comments

The basic flow of tic tac toe goes something like this

```python
# Loop
    # Ask player 'X' for a move
    # Put an 'X' on the board at that spot
    # Ask player 'O' for a move
    # Put an 'O on the board at that spot
```

We need to check the board after each move

```python
# Loop
    # Ask player 'X' for a move
    # Put an 'X' on the board at that spot
    # Check for win
    # Check for free space
    # Ask player 'O' for a move
    # Put an 'O on the board at that spot
    # Check for win
    # Check for free space
```

The "check for" are very similar ... probably the same kind of "looping over the cells".
Plus there is some important logic: you have to check for a win before looking to see
if every space is filled up.

```python
# Loop
    # Ask player 'X' for a move
    # Put an 'X' on the board at that spot
    # Check board status
    # Ask player 'O' for a move
    # Put an 'O on the board at that spot
    # Check board status
```

Notice the repeated code? We might (might) make the code easier to read/maintain by pulling them into
a loop?

```python
# Loop
    # Loop over player 'X' and 'O'
        # Ask player p for a move 
        # Put an p on the board at that spot 
        # Check board status        
```

# Identify some functions

Let's identify functions.

```python
# Loop
    # Ask player 'X' for a move: i = GET_MOVE('X')
    # Put an 'X' on the board at that spot: SET_TOKEN('X',i)
    # Check board status: s = GET_STATUS()
    #
    # Ask player 'O' for a move
    # Put an 'O on the board at that spot
    # Check board status
```

We'll need a PRINT_BOARD function too.

# Think about the parameters and returns

```python
def print_board():
    pass
    
def get_move(token):
    pass
    
def set_token(token,spot):
    pass
    
# Just planning for the future here. I've got a set ... maybe a
# get for symmetry?
def get_token(spot):
    pass
    
def get_status():
    pass
```

What is "token"? It has exactly 2 values: 'X' and 'O'. Do we use strings? Enumerations are a good choice. Python
DOES have enumerations. In other languages, mistakes can be caught at compile time. Since compile time IS runtime
for python, it doesn't help that much (but it does some and makes the code more readable). I think plain old strings 
are good here. How about integers 1 and 2? 

But if you want to see enum:

```python
from enum import Enum
class Token(Enum):
    X = 1
    O = 2

set_token(Token.X,2)
vs
set_token('X', 2)
```

What about `spot`? Range from 0 to 8? 1 to 9? The user input doesn't have to match this ... we could convert (subtract one).
Could be X,Y ... and we could convert.

I'm picking `0` for upper left through `8` for lower right with `4` being the center square.

What about board status? Another great place for an enum. Or integers.
  - 'Playing'
  - 'Tie'
  - 'X won'
  - 'O won'
  
# The board implementation

How do you want to keep the cell data ... what is in each "spot"?

A list of integers: 0=empty, 1=X, 2=O ? I like that
How about a list of strings: ' '=empty, 'X', or 'O' ? Or ''=empty. Or None=empty. 
Using enums: None=empty, Token.X, or Token.O

```python

board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
or
board = [' '] * 9

def print_board():
    #print(board)
    print(board[0]+'|'+board[1]+'|'+board[2])
    print('-+-+-')
    print(board[3]+'|'+board[4]+'|'+board[5])
    print('-+-+-')
    print(board[6]+'|'+board[7]+'|'+board[8])

board[0] = 'X'
board[4] = 'O'

print_board()
```

Unit test `print_board`? Might change `print_board` to `get_string_rep` and return a string. We'll do
that later.

# Ask player for move

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
    
while True:
    m = get_move('X')
    set_token('X',m)
    m = get_move('O')
    set_token('O',m)
```

# Board status

```python

# TODO: unit tests

def get_status():
    if board[0]=='X' and board[1]=='X' and board[2]=='X':
        return 'X won'
    # 3 rows, 3 columns, 2 diagonals
    # Repeat for O's ... or ...

def _check_token(t):
    if board[0]==t and board[1]==t and board[2]==t:
        return True
        
# How to check for a tie?
    for i in board:
        if i==' ':
            return 'Playing'
    return 'Tie'
    
    # Or better ...
    if ' ' in board:
        return 'Playing'
    return 'Tie'
```

