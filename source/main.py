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
# import games.left_right
import games.light

class GameSelector:
    def __init__(self):
        self.games = [
            # {"led": led.game_select_one, "module": games.left_right},
            {"led": led.game_select_two, "module": games.light}
        ]
        self.current_index = 0
        print(f"Initialized GameSelector with {len(self.games)} games.")

    def next_game(self):
        self.current_index = (self.current_index + 1) % len(self.games)
        print(f"Selected next game: index {self.current_index}")
        self.update_leds()

    def update_leds(self):
        for i, game in enumerate(self.games):
            if i == self.current_index:
                print(f"Turning on LED for game {i}")
                game["led"].on()
            else:
                print(f"Turning off LED for game {i}")
                game["led"].off()

    def run_current_game(self):
        print(f"Running game at index {self.current_index}")
        self.games[self.current_index]["module"].start()



def callback_next_game(pin, pressed, duration):
    global game_selector
    if pressed:
        game_selector.next_game()

def callback_start_game(pin, pressed, duration):
    global game_selector
    if pressed:
        game_selector.run_current_game()


def register_callbacks():
    button.start.callback = callback_start_game
    button.select.callback = callback_next_game

def idle_blink():
    time.sleep(random.uniform(0.01, 0.1))
    led.pico_internal.flash(100)

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
    if 
    time.sleep(0.1)
    pass