#written by ChatGPT prompt "write unit tests for SOSPlayer.py:" <paste contents of SOSPlayer.py
import unittest
from SOSPlayer import SOSPlayer  # Make sure to import your class correctly

class TestSOSPlayer(unittest.TestCase):

    def setUp(self):
        """Set up the initial state before each test."""
        self.player = SOSPlayer('Blue', 'Human', 'S')  # Initialize the player with example data

    def test_initial_values(self):
        """Test if the initial values are set correctly."""
        self.assertEqual(self.player.getColor(), 'Blue')  # Test initial PlayerColor
        self.assertEqual(self.player.getType(), 'Human')  # Test initial PlayerType
        self.assertEqual(self.player.getLetter(), 'S')  # Test initial PlayerLetter

    def test_setLetter(self):
        """Test the setLetter method."""
        self.player.setLetter('O')  # Set new letter
        self.assertEqual(self.player.getLetter(), 'O')  # Ensure the letter was updated correctly

    def test_setColor(self):
        """Test the setColor method."""
        self.player.setColor('Red')  # Change color
        self.assertEqual(self.player.getColor(), 'Red')  # Ensure the color was updated

    def test_setType(self):
        """Test the setType method."""
        self.player.setType('Computer')  # Change type
        self.assertEqual(self.player.getType(), 'Computer')  # Ensure the type was updated

    def test_edge_cases(self):
        """Test edge cases for setting attributes to invalid or empty values."""
        # Set to empty values
        self.player.setLetter('')
        self.player.setColor('')
        self.player.setType('')
        
        self.assertEqual(self.player.getLetter(), '')
        self.assertEqual(self.player.getColor(), '')
        self.assertEqual(self.player.getType(), '')

    def test_invalid_setColor(self):
        """Test if the setColor method handles invalid color."""
        # Invalid color, but we are not restricting input here
        self.player.setColor('Purple')  # Assigning a color that isn't necessarily valid
        self.assertEqual(self.player.getColor(), 'Purple')  # Ensure the color is set regardless of validity

    def test_invalid_setLetter(self):
        """Test if the setLetter method handles invalid letter."""
        self.player.setLetter('Z')  # Change to an invalid letter
        self.assertEqual(self.player.getLetter(), 'Z')  # Ensure the letter is updated

if __name__ == '__main__':
    unittest.main()
