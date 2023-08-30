from random import choice
from hangman_words import word_list
from hangman_art import logo, stages
from logging_config import hangman_logging

logger = hangman_logging()


class HangmanGame:
    """
    This class is responsible for the hangman game.
    """

    def __init__(self) -> None:
        logger.info("HangmanGame class instance is created")
        self.chosen_word = choice(word_list)
        self.display = ["_" for _ in range(len(self.chosen_word))]
        self.lives = 6
        self.end_of_game = False

    @staticmethod
    def get_user_guess() -> str:
        """
        Get user guess.
        :return: str
        """
        logger.info("get_user_guess method is called")
        return input("Guess a letter: ").lower()

    @staticmethod
    def is_valid_guess(guess: str, already_guessed: str) -> (bool, str):
        """
        Check if the guess is valid.
        :param guess:
        :param already_guessed:
        :return: bool, str
        """
        logger.info("is_valid_guess method is called")

        error_msg = ""

        if len(guess) != 1:
            error_msg = "You can only guess one letter at a time."
        elif not guess.isalpha():
            error_msg = "You can only guess letters."
        elif guess in already_guessed:
            error_msg = f"You have already guessed {guess}."

        if error_msg:
            logger.warning(error_msg)
            return False, error_msg

        return True, ""

    def update_display(self, guess: str) -> None:
        """
        Update the display.
        :param guess:
        :return: None
        """
        logger.info("update_display method is called")
        for index, letter in enumerate(self.chosen_word):
            logger.info(f"index: {index}, letter: {letter}")
            if letter == guess:
                self.display[index] = letter
                logger.info(f"self.display: {self.display}")

    def update_lives(self, guess: str) -> None:
        """
        Update the lives.
        :param guess:
        :return: None
        """
        logger.info("update_lives method is called")
        if guess not in self.chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            self.lives -= 1
            logger.info(f"self.lives: {self.lives}")

    def display_game_state(self) -> None:
        """
        Display the game state.
        :return: None
        """
        print(f"{' '.join(self.display)}")
        print(stages[self.lives])
        logger.info(f"{' '.join(self.display)}")

    def check_game_outcome(self) -> None:
        """
        Check if the game is over.
        :return: None
        """
        logger.info("check_game_outcome method is called")
        if "_" not in self.display:
            self.end_of_game = True
            print("You win.")
            logger.info("You win.")
        elif self.lives == 0:
            self.end_of_game = True
            print("You lose.")
            logger.info("You lose.")

    def play(self) -> None:
        """
        Play the game.
        :return: None
        """
        logger.info("play method is called")
        print(logo)
        already_guessed = set()

        while not self.end_of_game:
            logger.info("while loop is called")
            guess = self.get_user_guess()
            is_valid, error_msg = self.is_valid_guess(guess, already_guessed)

            if not is_valid:
                print(error_msg)
                logger.info(error_msg)
                continue

            already_guessed.add(guess)
            self.update_display(guess)
            self.update_lives(guess)
            self.display_game_state()
            self.check_game_outcome()


if __name__ == "__main__":
    logger.info("main method is called")
    game = HangmanGame()
    game.play()
