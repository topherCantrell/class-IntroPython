# An OO approach

What's wrong with our code? Absolutely nothing! But it isn't very flexible to expand and reuse down the road.
Maybe that's OK? Without a crystal-ball, you can't be sure how the code will be used in the future. But
we can make some general improvements.

## Globals

Look at the global "board". All the functions use this one global board. What if we wanted to make a game
server with multiple games going at once? Ask the players of each game for their moves one by one.

We need to change the functions to pass in the board to work on as an argument. But remember "class" with
the "self"? Methods always take the pointer as the first argument. Sounds like what we need.

## Encapsulation

We also have the `get_move` wrapped mingled in with the game logic. We might need other kinds of players
in the future. It would be nice to keep the code neatly compartmentalized. Remember "class"? We can
group related things together into separate classes.

# The Board API

`board.py`

```python
class Board:

    def __init__():
        self._board = [' ']* 9
    
    # def __str__(self):
    # Like Java's toString
    def get_board_repr(self):
        pass
        
    def set_token(self,token,spot):
        pass
        
    def get_token(self,spot):
        pass
        
    def get_status(self):
        pass    
```

# The Player API

`player.py`

```python
class Player:

    def __init__(self,token):
        self._token = token
        
    def get_move(self,board):
        pass
```

# Fleshing out the board

Pretty straight forward. Just using "self" instead of the global.

```python
class Board:

    def __init__(self):
        self._board = [' ']* 9    
        
    def set_token(self,token,spot):
        self._board[spot] = token
        
    def get_token(self,spot):
        return self._board[spot]
```

And checking is the same as before, we just have to use "self" to identify which list to check.

```python
    def _check_token(self,t):
        if self._board[0]==t and self._board[1]==t and self._board[2]==t:
            return True # Top row
        if self._board[3]==t and self._board[4]==t and self._board[5]==t:
            return True # Middle row
        if self._board[6]==t and self._board[7]==t and self._board[8]==t:
            return True # Bottom row
        if self._board[0]==t and self._board[3]==t and self._board[6]==t:
            return True # Left column
        if self._board[1]==t and self._board[4]==t and self._board[7]==t:
            return True # Middle column
        if self._board[2]==t and self._board[5]==t and self._board[8]==t:
            return True # right column
        if self._board[0]==t and self._board[4]==t and self._board[8]==t:
            return True # Upper left to bottom right
        if self._board[2]==t and self._board[4]==t and self._board[6]==t:
            return True # Upper right to bottom left
        
    def get_status(self):
        if self._check_token('X'):
            return 'X won'
        if self._check_token('O'):
            return 'O won'
        if ' ' in self._board:
            return 'Playing'
        else:
            return 'Tie'
```

## The string repr

```python
    def __str__(self):
        ret = ''
        ret = ret + self._board[0]+'|'+self._board[1]+'|'+self._board[2]+'\n'
        ret = ret + '-+-+-\n'
        ret = ret + self._board[3]+'|'+self._board[4]+'|'+self._board[5]+'\n'
        ret = ret + '-+-+-\n'
        ret = ret + self._board[6]+'|'+self._board[7]+'|'+self._board[8]+'\n'
        return ret
```

Now we can:

```python
b = Board()
print(b) # calls b.__repr__
```

## The player

```python
class Player:

    def __init__(self,token):
        self._token = token
        
    def get_move(self,board):
        print(board)
        print('Your move player',self._token)
        m = input('Where do you want to go? ')
        m = int(m)
        # TODO: error checking ... use "board" to look for free space
        return m
```

## The game logic

```python
from board import Board
from player import Player

# The big-bang

board = Board()
player1 = Player('X')
player2 = Player('O')

while True:
    m = player1.get_move(board)
    board.set_token('X',m)
    s = board.get_status()    
    if s != 'Playing':
        break
    m = player2.get_move(board)
    board.set_token('O',m)
    s = board.get_status()
    if s != 'Playing':
        break
    
print(s)
```

Notice how all the code is separated into separate areas. All the player stuff in one file. All the board stuff in another.
All the game logic in one place.

# How about other kinds of players?

```python
from player import Player
import random

class MrRandom(Player):
    
    # __init__ is picked up with inheritance, but we can
    # override if ever needed
    
    def get_move(self,board):
        # Lots of ways to do this. "Choice" is much better.
        while True:
            m = random.randint(0,8)
            token = board.get_token(m)
            if token==' ':
                return m
                
        possibles = []
        for i in range(9):
            if board.get_token(i)==' ':
                possibles.append(i)
        return random.choice(possibles)
 
```

Now its about creating the objects and wiring them up. What kind of players? Who goes first?
The main loop doesn't care what the objects actually do ... just that they implement the
expected interface.

How about other players: "The Onder" or "CAT Woman" ? Do they inherit from each other?

```python
from board import Board
from player import Player
from mr_random import MrRandom

# The big-bang

board = Board()
#player1 = Player('X')
player1 = MrRandom('X')
#player2 = Player('O')
player2 = MrRandom('O')

while True:
    m = player1.get_move(board)
    board.set_token('X',m)
    s = board.get_status()    
    if s != 'Playing':
        break
    m = player2.get_move(board)
    board.set_token('O',m)
    s = board.get_status()
    if s != 'Playing':
        break
    
print(board)
print(s)
```
