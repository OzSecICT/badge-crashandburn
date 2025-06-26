"""
Test Game

This is a demonstration game that shows basic functionality of a simple
game class. Use this as an example for your own games.
"""
# Imports

import button
from game import Game

class TestGame(Game): # Create a new class that inherits from Game
    def __init__(self):
        """
        Initialize the game class

        Perform any setup and create any variables you need.
        This is called once when the game class is instantiated.
        """
        super().__init__() # Call the parent class constructor
        print("Initializing Test Game")
        
        # Example variables
        self.my_variable = "Hello, World!"
        self.printed = False

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
        button.up.callback = self.clicked  # type: ignore
        button.down.callback = self.clicked  # type: ignore
        button.left.callback = self.clicked  # type: ignore
        button.right.callback = self.clicked  # type: ignore
        button.a.callback = self.clicked  # type: ignore
        button.b.callback = self.clicked  # type: ignore
        button.start.callback = self.clicked  # type: ignore
        
        # The select button is used to exit the game. clicked_select
        # is defined in the base Game class, so you don't need to
        # overload it unless you want to change its behavior.
        button.select.callback = self.clicked_select  # type: ignore

    def clicked(self, pin, pressed, duration):
        """
        Handle button presses

        Every button press callback needs to accept the above parameters.
        The pin parameter is the button that was pressed and
        pressed is a boolean. You can use this to determine if the button
        was pressed or released. The duration parameter is the time in milliseconds
        that the button was pressed for.
        """
        # If you don't check this, your function will run when
        # the button is pressed AND when released
        if pressed:
            print(f"Button pressed: {pin}")

    def run(self):
        """
        Game run logic

        This method is called by main.py when this game is executed.
        """
        super().run() # Call the parent run method to clear buttons/leds.
        print("Running Test Game")