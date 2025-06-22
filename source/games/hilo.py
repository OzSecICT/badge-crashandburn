"""
HiLo Guessing Game

This game is a guessing game. The player must guess either
hi-top or low-top sneakers on the badge. The game will
randomly select a sneaker, and if the player guesses correctly
their score increases.
"""
import random

import button
import led
from game import Game

class HiLoGame(Game):
    def __init__(self):
        """
        Initialize the game class
        """
        super().__init__() # Call the parent class constructor
        print("Initializing HiLo Game")
        self.score = 0
        self.choice = None
        self.guess = None
        self.options = ["hi", "lo"]

    def register_callbacks(self):
        button.up.callback = self.do_nothing  # type: ignore
        button.down.callback = self.do_nothing  # type: ignore
        button.left.callback = self.do_nothing  # type: ignore
        button.right.callback = self.do_nothing  # type: ignore
        button.a.callback = self.do_nothing  # type: ignore
        button.b.callback = self.do_nothing  # type: ignore
        button.start.callback = self.do_nothing  # type: ignore
        button.select.callback = self.do_nothing  # type: ignore

    def run(self):
        """
        Game loop
        """
        super().run() # Call the parent run method to clear buttons/leds.
        self.choice = random.choice(self.options)
        print(f"Selected random choice: {self.choice}")
        # Here you would normally wait for user input to guess

    def check(self, guess):
        """
        Check the user's guess against the randomly selected choice
        """
        if guess == self.choice:
            if self.score >= 15:
                print("Maximum score reached!")
                return
            self.score += 1
            print(f"Correct! Your score is now {self.score}.")
        else:
            print(f"Wrong! Your score remains {self.score}.")