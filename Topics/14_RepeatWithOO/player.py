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
    