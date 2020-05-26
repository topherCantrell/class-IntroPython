class Board:

    def __init__(self):
        self._board = [' ']* 9    
        
    def set_token(self,token,spot):
        self._board[spot] = token
        
    def get_token(self,spot):
        return self._board[spot]
    
    def __str__(self):
        ret = ''
        ret = ret + self._board[0]+'|'+self._board[1]+'|'+self._board[2]+'\n'
        ret = ret + '-+-+-\n'
        ret = ret + self._board[3]+'|'+self._board[4]+'|'+self._board[5]+'\n'
        ret = ret + '-+-+-\n'
        ret = ret + self._board[6]+'|'+self._board[7]+'|'+self._board[8]+'\n'
        return ret
    
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