"""
Test Game

This is a demonstration game that shows basic functionality of a simple
game class. Use this as an example for your own games.
"""
# Imports

import button
from game import Game
import state


class KodeGame(Game):  # Create a new class that inherits from Game
    def __init__(self):
        """
        Initialize the game class

        Perform any setup and create any variables you need.
        This is called once when the game class is instantiated.
        """
        super().__init__()  # Call the parent class constructor
        print("Initializing Kode Game")

        # Example variables
        self.pattern = "UUDDLRLRBAS"
        self.user_input = ""
        self.complete = False

    def register_callbacks(self):
        """
        Register button callbacks

        This is called by super().run()
        It is specified in the base Game class, but you should overload
        it with your own functions here.
        """
        # The "type: ignore" comments are used to
        # suppress type checking errors in VS Code
        # Set the callback to a local function to handle button presses.
        button.up.callback = self.clicked_up  # type: ignore
        button.down.callback = self.clicked_down  # type: ignore
        button.left.callback = self.clicked_left  # type: ignore
        button.right.callback = self.clicked_right  # type: ignore
        button.a.callback = self.clicked_a  # type: ignore
        button.b.callback = self.clicked_b  # type: ignore
        button.start.callback = self.clicked_start  # type: ignore

        # The select button is used to exit the game. clicked_select
        # is defined in the base Game class, so you don't need to
        # overload it unless you want to change its behavior.
        button.select.callback = self.clicked_select  # type: ignore

    def clicked_up(self, pin, pressed, duration):
        if pressed:
            self.user_input += "U"
            self.check()

    def clicked_down(self, pin, pressed, duration):
        if pressed:
            self.user_input += "D"
            self.check()

    def clicked_left(self, pin, pressed, duration):
        if pressed:
            self.user_input += "L"
            self.check()

    def clicked_right(self, pin, pressed, duration):
        if pressed:
            self.user_input += "R"
            self.check()

    def clicked_a(self, pin, pressed, duration):
        if pressed:
            self.user_input += "A"
            self.check()

    def clicked_b(self, pin, pressed, duration):
        if pressed:
            self.user_input += "B"
            self.check()

    def clicked_start(self, pin, pressed, duration):
        if pressed:
            self.user_input += "S"
            self.check()

    def check(self):
        if len(self.user_input) == len(self.pattern):
            if self.user_input == self.pattern:
                print("Correct Kode entered! Game completed!")
                self.complete = True
                state.gamestate.complete("KodeGame")
                self.exit()
            else:
                print("Incorrect Kode. Try again!")
                self.user_input = ""

    def run(self):
        """
        Game run logic

        This method is called by main.py when this game is executed.
        """
        super().run()  # Call the parent run method to clear buttons/leds.
        print("Running Test Game")
