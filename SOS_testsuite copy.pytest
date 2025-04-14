import unittest
from SOSBoard import SOSSimpleBoard, SOSGeneralBoard, SOSSimpleBoardCPU, SOSGeneralBoardCPU, SOSBoardCPU
from SOSPlayer import SOSPlayer


# === ACCEPTANCE CRITERIA 1.X – Choose a board size ===

class TestBoardSize(unittest.TestCase):
    def test_valid_board_size(self):
        board = SOSSimpleBoard(5)
        self.assertEqual(board.getBoardSize(), 5)  # AC 1.1

        default_board = SOSSimpleBoard(99)
        self.assertEqual(default_board.getBoardSize(), 8)  # AC 1.3

    def test_invalid_board_size(self):
        board = SOSSimpleBoard(2)
        self.assertEqual(board.getBoardSize(), 8)  # AC 1.2


# === ACCEPTANCE CRITERIA 2.X – Choose the game mode ===

class TestGameModeLogic(unittest.TestCase):
    def test_simple_game_win_condition(self):
        board = SOSSimpleBoard(3)
        board.boardArray = [['S', 'O', ' ']]
        board.emptySpaces -= 2
        board.getTurn().setLetter('S')
        board.makeMove(0, 2)
        self.assertTrue(board.checkEnd())  # AC 2.1

    def test_general_game_win_condition(self):
        board = SOSGeneralBoard(3)
        board.emptySpaces = 1
        board.getTurn().setLetter('S')
        board.makeMove(2, 2)
        self.assertTrue(board.checkEnd())  # AC 2.2


# === ACCEPTANCE CRITERIA 3.X – Start a new game ===

class TestNewGameSetup(unittest.TestCase):
    def test_new_game_with_valid_input(self):
        board = SOSSimpleBoard(10)
        self.assertEqual(board.getBoardSize(), 10)  # AC 3.1

    def test_new_game_with_invalid_input(self):
        board = SOSSimpleBoard(100)
        self.assertEqual(board.getBoardSize(), 8)  # AC 3.2


# === ACCEPTANCE CRITERIA 4.X – Make a move in a simple game ===

class TestSimpleGameMoves(unittest.TestCase):
    def test_simple_game_occupied_space(self):
        board = SOSSimpleBoard(3)
        board.boardArray[1][1] = 'S'
        move = board.makeMove(1, 1)
        self.assertIsNone(move)  # AC 4.1

    def test_simple_game_sos_and_win(self):
        board = SOSSimpleBoard(3)
        board.boardArray = [['S', 'O', ' ']]
        board.emptySpaces -= 2
        board.getTurn().setLetter('S')
        game_over = board.makeMove(0, 2)
        self.assertTrue(game_over)  # AC 4.2

    def test_simple_game_valid_move(self):
        board = SOSSimpleBoard(3)
        board.getTurn().setLetter('S')
        current_turn = board.getTurn()
        board.makeMove(1, 1)
        self.assertNotEqual(board.getTurn(), current_turn)  # AC 4.3


# === ACCEPTANCE CRITERIA 5.X – A simple game is over ===

class TestSimpleGameEnd(unittest.TestCase):
    def test_simple_game_end_on_sos(self):
        board = SOSSimpleBoard(3)
        board.boardArray = [['S', 'O', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
        board.emptySpaces -= 2
        board.getTurn().setLetter('S')
        game_over = board.makeMove(0, 2)
        self.assertTrue(game_over)  # AC 5.1

    def test_simple_game_no_more_moves_after_win(self):
        board = SOSSimpleBoard(3)
        board.boardArray = [['S', 'O', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
        board.emptySpaces -= 2
        board.getTurn().setLetter('S')
        board.makeMove(0, 2)
        board.makeMove(1, 1)
        self.assertNotEqual(board.getPlace(1, 1), 'S')  # AC 5.2


# === ACCEPTANCE CRITERIA 6.X – Make a move in a general game ===

class TestGeneralGameMoves(unittest.TestCase):
    def test_general_game_occupied_space(self):
        board = SOSGeneralBoard(3)
        board.boardArray[1][1] = 'O'
        result = board.makeMove(1, 1)
        self.assertIsNone(result)  # AC 6.1

    def test_general_game_last_move(self):
        board = SOSGeneralBoard(3)
        board.emptySpaces = 1
        board.makeMove(0, 0)
        board.getTurn().setLetter('S')
        board.makeMove(2, 2)
        self.assertNotEqual(board.getPlace(2, 2), 'S')  # AC 6.2

    def test_general_game_valid_move(self):
        board = SOSGeneralBoard(3)
        current_turn = board.getTurn()
        board.getTurn().setLetter('S')
        board.makeMove(1, 1)
        self.assertNotEqual(board.getTurn(), current_turn)  # AC 6.3


# === ACCEPTANCE CRITERIA 7.X – A general game is over ===

class TestGeneralGameEnd(unittest.TestCase):
    def test_general_game_end_no_spaces(self):
        board = SOSGeneralBoard(3)
        board.emptySpaces = 1
        board.getTurn().setLetter('O')
        board.makeMove(2, 2)
        self.assertTrue(board.checkEnd())  # AC 7.1

    def test_general_game_no_more_moves_after_end(self):
        board = SOSGeneralBoard(3)
        board.emptySpaces = 1
        board.getTurn().setLetter('S')
        board.makeMove(2, 2)
        board.makeMove(0, 0)
        self.assertNotEqual(board.getPlace(0, 0), 'S')  # AC 7.2


# === ACCEPTANCE CRITERIA 8.X – Choose player type ===

class TestPlayerTypeSelection(unittest.TestCase):
    def test_player_type_selection(self):
        blue = SOSPlayer("Blue")
        red = SOSPlayer("Red")
        blue.setType("Computer")
        red.setType("Human")
        self.assertEqual(blue.getType(), "Computer")  # AC 8.1
        self.assertEqual(red.getType(), "Human")      # AC 8.2

        game = SOSSimpleBoard(8)
        game.getBluePlayer().setType('Computer')
        self.assertEqual(game.getBluePlayer().getType(), 'Computer')  # AC 8.3


# === ACCEPTANCE CRITERIA 9.X – Computer makes a move ===

class TestComputerMove(unittest.TestCase):
    def test_computer_move_validity(self):
        game = SOSSimpleBoardCPU(8)
        x, y = game.findMove()
        self.assertTrue(0 <= x < 8 and 0 <= y < 8)  # AC 9.1
        self.assertEqual(game.getPlace(x, y), " ")  # AC 9.2
        game.makeMove(x, y)
        self.assertIn(game.getPlace(x, y), ["S", "O"])  # AC 9.2 continued
        self.assertIsNotNone(game.checkEnd())  # AC 9.3


# === ACCEPTANCE CRITERIA 10.X – Play complete game against computer ===

class TestComputerFullGame(unittest.TestCase):
    def test_full_game_execution_simple(self):
        game = SOSSimpleBoardCPU(3)
        while not game.checkEnd():
            x, y = game.findMove()
            game.makeMove(x, y)
        self.assertTrue(game.checkEnd())  # AC 10.3

    def test_full_game_execution_general(self):
        game = SOSGeneralBoardCPU(3)
        while not game.checkEnd():
            x, y = game.findMove()
            game.makeMove(x, y)
        self.assertTrue(game.checkEnd())  # AC 10.3


# === ACCEPTANCE CRITERIA 11.X – Computer strategy support ===

class TestComputerStrategy(unittest.TestCase):
    def test_computer_strategy_applied(self):
        game = SOSSimpleBoardCPU(3)
        game.getTurn().setLetter('S')
        game.boardArray[0][1] = 'O'
        game.boardArray[0][2] = 'S'
        game.emptySpaces -= 2
        move = game.findMove()
        game.makeMove(*move)
        self.assertTrue(game.getBlueScore() > 0 or game.getRedScore() > 0)  # AC 11.1 & 11.3

    def test_strategy_used_in_simple_and_general(self):
        simple = SOSSimpleBoardCPU(3)
        general = SOSGeneralBoardCPU(3)
        move1 = simple.findMove()
        move2 = general.findMove()
        self.assertIsInstance(move1, tuple)  # AC 11.2
        self.assertIsInstance(move2, tuple)


if __name__ == '__main__':
    unittest.main()
