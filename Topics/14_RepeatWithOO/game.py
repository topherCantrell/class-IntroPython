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