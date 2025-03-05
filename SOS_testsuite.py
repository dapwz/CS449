import unittest
from SOSBoard import SOSBoard
from SOSPlayer import SOSPlayer

class TestSOSGame(unittest.TestCase):
    
    def setUp(self):
        self.board = SOSBoard(8, 'Simple')
        self.blue_player = SOSPlayer('Blue', 'Human', 'S')
        self.red_player = SOSPlayer('Red', 'Human', 'O')
    
    # AC 1.1, AC 3.1: Test valid board creation
    def test_board_initialization(self):
        self.assertEqual(self.board.boardSize, 8)
        self.assertEqual(self.board.emptySpaces, 64)
    
    # AC 1.2, AC 3.2: Test invalid board size handling
    def test_invalid_board_size(self):
        invalid_board = SOSBoard(20, 'Simple')
        self.assertEqual(invalid_board.boardSize, 8)  # Default to 8
        small_board = SOSBoard(2, 'Simple')
        self.assertEqual(small_board.boardSize, 8)  # Default to 8
    
    # AC 1.3: Test board defaults to 8 on launch or error
    def test_board_default_size(self):
        default_board = SOSBoard(8, 'Simple')
        self.assertEqual(default_board.boardSize, 8)
    
    # AC 2.1, AC 4.2: Test simple game mode win condition
    def test_check_win_simple(self):
        self.board.makeMove('Blue', 'S', 1, 1)
        self.board.makeMove('Red', 'O', 2, 2)
        self.board.makeMove('Blue', 'S', 3, 3)
        result = self.board.checkWin('Blue', 2, 2)
        self.assertTrue(result)
        self.assertEqual(self.board.blueScore, 1)
    
    # AC 2.2, AC 5.2: Test general game mode win condition when the board is full
    def test_check_win_general(self):
        general_board = SOSBoard(8, 'General')
        for x in range(1, 9):
            for y in range(1, 9):
                general_board.makeMove('Blue', 'S' if (x + y) % 2 == 0 else 'O', x, y)
        self.assertTrue(general_board.checkWin('Blue', 8, 8))
    
    # AC 4.1, AC 5.1: Test selecting an occupied space
    def test_invalid_move(self):
        self.board.makeMove('Blue', 'S', 1, 1)
        self.board.makeMove('Red', 'O', 1, 1)
        self.assertEqual(self.board.getPlace(1, 1), 'S')  # Should still be 'S'
    
    # AC 4.3, AC 5.3: Test selecting an unoccupied space updates board and changes turn
    def test_valid_move_updates_board(self):
        self.board.makeMove('Blue', 'S', 1, 1)
        self.assertEqual(self.board.getPlace(1, 1), 'S')
        self.assertEqual(self.board.emptySpaces, 63)
    
    # AC 3.1: Test creating a new board with a valid size
    def test_create_new_board(self):
        new_board = SOSBoard(5, 'Simple')
        self.assertEqual(new_board.boardSize, 5)
    
    # AC 5.2: Test selecting the last available space triggers game end
    def test_last_move_triggers_game_end(self):
        general_board = SOSBoard(3, 'General')
        for x in range(1, 4):
            for y in range(1, 4):
                general_board.makeMove('Blue', 'S' if (x + y) % 2 == 0 else 'O', x, y)
        self.assertTrue(general_board.checkWin('Blue', 3, 3))
    
    # Player tests
    def test_player_attributes(self):
        self.assertEqual(self.blue_player.getColor(), 'Blue')
        self.assertEqual(self.red_player.getType(), 'Human')
        self.assertEqual(self.red_player.getLetter(), 'O')
    
    def test_change_player_attributes(self):
        self.blue_player.setLetter('O')
        self.assertEqual(self.blue_player.getLetter(), 'O')
        self.red_player.setType('Computer')
        self.assertEqual(self.red_player.getType(), 'Computer')

if __name__ == '__main__':
    unittest.main()