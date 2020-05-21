# Test-driven Development of the TicTacToeBoard

Start with the TicTacToe board code given below (or use your own).

Create the `test_board.py` file and make a class that extends `unittest.TestCase`. Add a unit
test to place a token on the board then confirm the token is there. This test case will fail the
first time your run your code (because there is no code in TicTacToeBoard).

Now add code to the TicTacToeBoard so that the test case passes.

Add other test cases. Think about:
  - What happens if you use a move outside the range 0-8?
  - What happens if you use a token besides 'X' and 'O'?
  - Are you sure the board starts out empty?
  - Are you going to test ever possible win scenario for both players?
  
# Starting point

`tictactoe.py`

```python
class TicTacToeBoard:
    
    def __init__(self):
        pass
        
    def make_move(self,location,token):
        pass
                
    def get_location(self,location):
        pass        
    
    def check_game(self):
        pass
```