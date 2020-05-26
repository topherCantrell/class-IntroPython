from player import Player
import random

class MrRandom(Player):
    
    # __init__ is picked up with inheritance, but we can
    # override if ever needed
    
    def get_move(self,board):
        # Lots of ways to do this. Choice is much better.
        while True:
            m = random.randint(0,8)
            token = board.get_token(m)
            if token==' ':
                return m
    
    
