
class TicTacToeBoard:
    
    def __init__(self):
        print('In constructor')
        
    def make_move(self,location,token):
        print('Setting',location,'to',token)
        
    def get_location(self,location):
        print('Getting',location)
        return 'X'
    
    def check_game(self):
        print('Checking')
        return 'playing'
    

board = TicTacToeBoard()
while True:
    
    move = input('Where to player X? ')
    move = int(move)
    
    board.make_move(move,'X')
    
    status = board.check_game()
    if status=='x-won':
        pass
    elif status=='tie':
        pass
    
    move = input('Where to player O? ')
    move = int(move)
    
    board.make_move(move,'O')
    
    status = board.check_game()
    if status=='o-won':
        pass
    #elif status=='tie':
    #    pass
    