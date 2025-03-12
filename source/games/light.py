"""
Light Game

Press the A button and toggle the game_select_one LED.
Press the B button and toggle the game_select_two LED.
"""

import button
import led
from game import Game

class LightGame(Game):
    def __init__(self):
        super().__init__() # Call the parent class constructor

    def run(self):
        super().run() # Call the parent run method to clear buttons/leds.
        print("Running Light Game")
        print("Press A to toggle game_select_one LED")
        print("Press B to toggle game_select_two LED")
        print("Press SELECT to exit")

    def register_callbacks(self):
        # Register callbacks
        button.start.callback = None
        button.select.callback = self.clicked_select # type: ignore
        button.a.callback = self.clicked_a # type: ignore
        button.b.callback = self.clicked_b # type: ignore

    def clicked_a(self, pin, pressed, duration):
        if pressed:
            led.game_select_one.toggle()

    def clicked_b(self, pin, pressed, duration):
        if pressed:
            led.game_select_two.toggle()

    def clicked_select(self, pin, pressed, duration):
        if pressed:
            self.exit()