import unittest
from SOSPlayer import SOSPlayer
from SOSBoard import SOSSimpleBoard, SOSGeneralBoard

class TestSOSGame(unittest.TestCase):
    # AC 1.1: New game boards will be the size of the entered value
    def test_board_size_valid(self):
        board = SOSSimpleBoard(5)
        self.assertEqual(board.boardSize, 5)

    # AC 1.2: New game boards will fail to be created
    def test_board_size_invalid(self):
        board = SOSSimpleBoard(2)
        self.assertEqual(board.boardSize, 8)
        board = SOSSimpleBoard(17)
        self.assertEqual(board.boardSize, 8)

    # AC 1.3: Board size value defaults to 8
    def test_board_default_size(self):
        board = SOSSimpleBoard(0)
        self.assertEqual(board.boardSize, 8)

    # AC 2.1: Simple game mode win condition
    def test_simple_game_win(self):
        board = SOSSimpleBoard(3)
        board.getRedPlayer().setLetter('O')
        board.makeMove(0, 1)
        board.makeMove(1, 1)
        result = board.makeMove(2, 1)
        self.assertTrue(result)

    # AC 2.2: General game mode win condition
    def test_general_game_win(self):
        board = SOSGeneralBoard(3)
        for x in range(3):
            for y in range(3):
                board.makeMove(x, y)
        self.assertTrue(board.checkEnd())

    # AC 4.1 & 5.1: Selecting an occupied space
    def test_occupied_space_error(self):
        board = SOSSimpleBoard(3)
        board.makeMove(1, 1)
        self.assertEqual(board.getPlace(1, 1), 'S')
        board.makeMove(1, 1)
        self.assertEqual(board.getPlace(1, 1), 'S')

    # AC 4.3 & 5.3: Selecting an unoccupied space
    def test_valid_move_updates_board(self):
        board = SOSSimpleBoard(3)
        board.makeMove(1, 1)
        self.assertEqual(board.getPlace(1, 1), 'S')

    # Player switching (not explicitly covered in ACs but relevant to gameplay)
    def test_player_switch_after_move(self):
        board = SOSSimpleBoard(3)
        first_turn = board.getTurn()
        board.makeMove(1, 1)
        self.assertNotEqual(first_turn, board.getTurn())

if __name__ == '__main__':
    unittest.main()
