import unittest
from unittest.mock import patch
from main import HangmanGame


class TestHangmanGame(unittest.TestCase):
    def setUp(self):
        self.game = HangmanGame()

    def test_get_user_guess(self):
        with patch("builtins.input", return_value="a"):
            guess = self.game.get_user_guess()
        self.assertEqual(guess, "a")

    def test_is_valid_guess_valid(self):
        valid, error_msg = self.game.is_valid_guess("t", set())
        self.assertTrue(valid)
        self.assertEqual(error_msg, "")

    def test_is_valid_guess_invalid_length(self):
        valid, error_msg = self.game.is_valid_guess("ab", set())
        self.assertFalse(valid)
        self.assertEqual(error_msg, "You can only guess one letter at a time.")

    def test_is_valid_guess_invalid_non_alpha(self):
        valid, error_msg = self.game.is_valid_guess("1", set())
        self.assertFalse(valid)
        self.assertEqual(error_msg, "You can only guess letters.")

    def test_is_valid_guess_invalid_already_guessed(self):
        valid, error_msg = self.game.is_valid_guess("a", {"a", "b"})
        self.assertFalse(valid)
        self.assertEqual(error_msg, "You have already guessed a.")

    def test_update_lives(self):
        self.game.chosen_word = "test"
        self.game.update_lives("x")
        self.assertEqual(self.game.lives, 5)

    def test_check_game_outcome_win(self):
        self.game.display = ["t", "e", "s", "t"]
        self.game.check_game_outcome()
        self.assertTrue(self.game.end_of_game)

    def test_check_game_outcome_lose(self):
        self.game.display = ["_", "_", "_", "_"]
        self.game.lives = 0
        self.game.check_game_outcome()
        self.assertTrue(self.game.end_of_game)


if __name__ == "__main__":
    unittest.main()
