"""
CRASHANDBURN Main.py

This is the main script for the CRASHANDBURN badge firmware. 

By default this script will blink LED's, and wait for input to
select a different game/mode.


"""

from machine import Timer
import time
import random

import button
import led
from games.hilo import HiLoGame
from games.rps import RPSGame
# from games.light import LightGame
# from games.left_right import LeftRightGame
# from games.dtmf import DtmfGame

class GameSelector:
    def __init__(self):
        self.games = [
            {"led": led.hilo_complete, "class": HiLoGame},
            {"led": led.rps_complete, "class": RPSGame}
        ]
        self.current_index = 0
        self.current_game = None
        print(f"Initialized GameSelector with {len(self.games)} games.")

    def next_game(self):
        self.current_index = (self.current_index + 1) % len(self.games)
        print(f"Selected next game: index {self.current_index}")
        self.update_leds()

    def update_leds(self):
        for i, game in enumerate(self.games):
            if i == self.current_index:
                print(f"Selected game {i}")
                game["led"].on()
            else:
                game["led"].off()

    def run_current_game(self):
        print(f"Running game at index {self.current_index}")
        self.current_game = self.games[self.current_index]["class"]()
        self.current_game.run()

def callback_next_game(pin, pressed, duration):
    global game_selector
    if pressed:
        game_selector.next_game()

def callback_start_game(pin, pressed, duration):
    global game_selector
    if pressed:
        game_selector.run_current_game()

def callback_toggle_led(pin, pressed, duration):
    """
    Callback to toggle the LED state.
    This is a placeholder for any LED toggling logic.
    """
    if pressed:
        print("Toggle LED between idle and score state.")
        led.badge_complete.toggle()

def register_callbacks():
    button.start.callback = callback_start_game # type: ignore
    button.select.callback = callback_next_game # type: ignore
    button.a.callback = callback_toggle_led # type: ignore
    button.b.callback = callback_toggle_led # type: ignore

def idle_blink():
    time.sleep(random.uniform(0.01, 0.1)) # why is this here?
    led.badge_complete.flash(100)

print("Starting CRASHANDBURN")
game_selector = GameSelector()

# Clear buttons and leds
button.clear()
led.clear()

# Register our button callbacks
register_callbacks()

# Start the idle blink
idle_blink()

while True:
    if game_selector.current_game is not None:
        if game_selector.current_game.is_running == False:
            game_selector.current_game = None # Clear the current game
            button.clear() # Clear button callbacks
            led.clear() # Clear LEDs
            register_callbacks() # Re-register the callbacks
            idle_blink() # Start the idle blink
    time.sleep(0.1)
    pass