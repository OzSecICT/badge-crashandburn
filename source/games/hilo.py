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

import pinout
import state
import scoreboard


class HiLoGame(Game):
    def __init__(self):
        """
        Initialize the game class
        """
        super().__init__()  # Call the parent class constructor
        print("Initializing HiLo Game")
        self.score = 0
        self.choice = None
        self.guess = None
        self.options = ["HI", "LO"]
        self.complete = False

    def register_callbacks(self):
        button.up.callback = self.cycle  # type: ignore
        button.down.callback = self.cycle  # type: ignore
        button.a.callback = self.clicked_a  # type: ignore
        button.select.callback = self.clicked_select  # type: ignore

    def cycle(self, pin, pressed, duration):
        # Cycle through options
        if pressed:
            self.guess = "HI" if self.guess == "LO" else "LO"
            print(f"User guessed: {self.guess}")

    def clicked_a(self, pin, pressed, duration):
        """
        Handle the A button being pressed in HiLoGame
        """
        if pressed:
            print(f"User submitted guess: {self.guess}")
            self.check(self.guess)

    def run(self):
        """
        Game loop
        """
        super().run()  # Call the parent run method to clear buttons/leds.
        self.choice = random.choice(self.options)
        print(f"Selected random choice: {self.choice}")

    def check(self, guess):
        """
        Check the user's guess against the randomly selected choice
        """
        if guess == self.choice:
            if self.score >= 15:
                print("Maximum score reached! Game completed!")
                self.complete = True
                state.gamestate.complete("HiLoGame")
                self.exit()
                return
            self.score += 1
            scoreboard.scoreboard.add_score("HiLoGame")
            scoreboard.scoreboard.show_score("HiLoGame")
            print(f"Correct! Your score is now {self.score}.")
            self.run()
        else:
            scoreboard.scoreboard.show_score("HiLo")
            print(f"Wrong! Your score remains {self.score}.")
            print("Try again!")
            self.run()
