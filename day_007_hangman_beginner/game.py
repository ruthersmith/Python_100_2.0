"""
    Author: Ruthersmith Bercy

    Hangman Game

    A command-line implementation of the classic Hangman game.
    The game randomly selects a word, displays it as hidden letters,
    and allows the user to guess letters until the word is revealed
    or the player runs out of lives.

    ASCII art used for visual feedback is stored in a separate 'ascii_art.py' file
    to keep game logic clean and readable.

    How to run:
        python game.py
"""


import random
from ascii_art import hangman

class Game:
    """
        Encapsulates the core logic and state of a Hangman game.

        This class manages the selected word, remaining lives,
        and guessed letters. The `run()` method drives the game loop and handles
        user interaction via the command line.
    """

    WORDS = [
    "python",
    "developer",
    "keyboard",
    "function",
    "variable",
    "hangman",
    "iteration",
    "computer",
    "terminal",
    "debugging"
]

    def __init__(self):
        print("Welcome to Hangman, A game where you have six (6) tries to Guess the correct word")
        self.word = random.choice(Game.WORDS)
        self.user_word = ["_" for letter in self.word]
        self.guesses_left = 6

    def run(self):
        
        while "".join(self.user_word) != self.word and self.guesses_left > 0:
            found_letter = False
            print(f"This is the word to Guess: {"".join(self.user_word)}")
            user_guess = input("Guess a letter: ").lower()

            for index in range(len(self.word)):
                if user_guess == self.word[index]:
                    self.user_word[index] = user_guess
                    found_letter = True

            if not found_letter:
                self.guesses_left -= 1
                print(f"Unfortunately your guess {user_guess} is not in this word, you have {self.guesses_left} remaining guesses")

            print(hangman[self.guesses_left])

        if self.guesses_left <= 0:
            print("Unfortunately Game Over, no more guesses left. You lose!")
        else:
            print(f"You have correctly guessed the word {self.word}. You win!!")


if __name__ == "__main__":
    Game().run()