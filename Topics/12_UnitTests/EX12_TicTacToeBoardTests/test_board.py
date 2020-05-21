import unittest
from tictactoe import TicTacToeBoard

class TestTicTacToeBoard(unittest.TestCase):
    
    def test_can_make_move(self):
        board = TicTacToeBoard()
        self.assertTrue(board.get_location(0)==' ')
        board.make_move(0,'X')
        self.assertTrue(board.get_location(0)=='X')
        
    def test_board_starts_empty(self):
        # A loop here would be nice.
        pass
    
    def test_move_range_negative(self):
        board = TicTacToeBoard()
        # Be specific ... show why
        self.assertRaises(IndexError,board.make_move,-1,'X')
        
        with self.assertRaises(IndexError) as ctx:       
            board.make_move(-1,'X')   
        ex = ctx.exception           
        # Notice the coma
        self.assertTrue(ex.args == ('Must be 0 to 8',))
        # Easier
        self.assertTrue(str(ex) == 'Must be 0 to 8')
        # Usually
        self.assertTrue(str(ctx.exception) == 'Must be 0 to 8')
    
    # TODO develop these together.
    
    def test_move_range_too_high(self):
        pass
    
    def test_move_taken(self):
        pass
    
    def test_tokens_other_than_X_O(self):
        pass
    
    def test_win_x(self):
        pass
    
    def test_win_o(self):
        pass
    
    def test_tie(self):
        pass
    
if __name__ == '__main__':
    unittest.main()        