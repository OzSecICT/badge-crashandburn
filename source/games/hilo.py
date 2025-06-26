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
        self.options = ["HI", "LO"]

    def register_callbacks(self):
        button.up.callback = self.clicked_a  # type: ignore
        button.down.callback = self.clicked_b  # type: ignore
        button.a.callback = self.clicked_a  # type: ignore
        button.b.callback = self.clicked_b  # type: ignore
        button.select.callback = self.clicked_select  # type: ignore

    def clicked_a(self, pin, pressed, duration):
        """
        Handle the A button being pressed in HiLoGame
        """
        if pressed:
            self.guess = "HI"
            print(f"User guessed: {self.guess}")
            self.check(self.guess)

    def clicked_b(self, pin, pressed, duration):
        """
        Handle the B button being pressed in HiLoGame
        """
        if pressed:
            self.guess = "LO"
            print(f"User guessed: {self.guess}")
            self.check(self.guess)

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
                self.exit()
                return
            self.score += 1
            print(f"Correct! Your score is now {self.score}.")
            self.run()
        else:
            print(f"Wrong! Your score remains {self.score}.")
            print("Try again!")
            self.run()