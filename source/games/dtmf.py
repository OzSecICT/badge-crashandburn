"""
DTMF Game

Listens for DTMF tones.
"""

import machine
import utime
import time

import button
import led
from game import Game

class DtmfGame(Game):
    def __init__(self):
        super().__init__() # Call the parent class constructor
        self.tones = ["1", "2", "3"]
        self.mic = machine.ADC(26)

    def run(self):
        super().run() # Call the parent run method to clear buttons/leds.
        print("Running DTMF Game")
        print("Press A to enter echo mode, echo's the registered DTMF tones")
        print("Press B to enter game mode. Enter the correct tones to win")
        print("Press SELECT to exit")

        while True:
            mic_value = self.mic.read_u16()
            print("Value: ", mic_value)
            time.sleep(1)

    def register_callbacks(self):
        # Register callbacks
        button.start.callback = None
        button.select.callback = self.clicked_select # type: ignore

    def clicked_select(self, pin, pressed, duration):
        if pressed:
            self.exit()
