
#written by ChatGPT prompt "write unit tests for SOSBoard.py:" <paste contents of SOSBoard.py
import unittest
from SOSBoard import SOSBoard  # Assuming SOSBoard.py is in the same directory

class TestSOSBoard(unittest.TestCase):
    
    def setUp(self):
        """Set up initial conditions before each test."""
        self.board = SOSBoard(3, 'Simple')  # Create a 3x3 board for testing with 'Simple' game type

    def test_initial_board_state(self):
        """Test the initial state of the board."""
        self.assertEqual(self.board.getPlace(1, 1), ' ')  # Board should be empty
        self.assertEqual(self.board.getPlace(3, 3), ' ')  # Board should be empty
        self.assertEqual(self.board.getBlueScore(), 0)  # Blue score should start at 0
        self.assertEqual(self.board.getRedScore(), 0)  # Red score should start at 0

    def test_make_move_valid(self):
        """Test making a valid move on the board."""
        self.board.makeMove('Blue', 'S', 1, 1)  # Blue player places 'S' at position (1,1)
        self.assertEqual(self.board.getPlace(1, 1), 'S')  # The cell should contain 'S'

    def test_make_move_invalid(self):
        """Test making an invalid move (occupied cell)."""
        self.board.makeMove('Blue', 'S', 1, 1)  # First move, valid
        result = self.board.makeMove('Red', 'O', 1, 1)  # Second move on the same cell, invalid
        self.assertEqual(result, False)  # The move should return False, indicating failure
 
