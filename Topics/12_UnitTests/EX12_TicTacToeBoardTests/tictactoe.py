
class TicTacToeBoard:
    
    def __init__(self):
        self.cells = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        #self.cells = [' ']*9
        
    def make_move(self,location,token):
        if location<0 or location>8:
            raise ValueError('Location must be 0 to 8')
        if token!='X' and token!='O':
            raise ValueError('Token must be X or O')
        if self.cells[location]!=' ':
            raise ValueError('That location is already taken')
        self.cells[location] = token
                
    def get_location(self,location):
        if location<0 or location>8:
            raise ValueError('Location must be 0 to 8')
        if token!='X' and token!='O':
            raise ValueError('Token must be X or O')
        return self.cells[location]        
    
    def check_game(self):
        if self.cells[0]=='X' and self.cells[1]=='X' and self.cells[2]=='X':
            return 'x-won'
        # TODO 3 colums, 3 rows, 2 diagonals
        # TODO repeat for 'O'
        for c in self.cells:
            # if there is an empty square, the game goes on!
            if c==' ':
                return 'playing'
        # No empty square. This is a tie.
        return 'tie'
    