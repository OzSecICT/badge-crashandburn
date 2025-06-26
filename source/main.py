"""
CRASHANDBURN Main.py

This is the main script for the CRASHANDBURN badge firmware. 

By default this script will blink LED's, and wait for input to
select a different game/mode.


"""

import _thread
from machine import Timer
import time
import random


import button
import led
from games.hilo import HiLoGame
from games.rps import RPSGame
from games.test import TestGame
# from games.light import LightGame
# from games.left_right import LeftRightGame
# from games.dtmf import DtmfGame

class GameSelector:
    def __init__(self):
        self.games = [
            {"name": "HiLo", "led": led.hilo_complete, "class": HiLoGame},
            {"name": "RPS", "led": led.rps_complete, "class": RPSGame},
            {"name": "Test", "led": led.badge_complete, "class": TestGame}
        ]
        self.current_index = 0
        self.current_game = None
        print(f"Initialized GameSelector with {len(self.games)} games.")

    def next_game(self):
        self.current_index = (self.current_index + 1) % len(self.games)
        print(f"Selected next game: [{self.current_index}] {self.games[self.current_index]['name']}")
        self.update_leds()

    def update_leds(self):
        for i, game in enumerate(self.games):
            if i == self.current_index:
                print(f"Selected game [{i}]: {game['name']}")
                game["led"].on()
            else:
                game["led"].off()

    def run_current_game(self):
        print(f"Running game [{self.current_index}] {self.games[self.current_index]['name']}")
        self.current_game = self.games[self.current_index]["class"]()
        self.current_game.run()

def callback_next_game(pin, pressed, duration):
    global game_selector, idle_blink
    if pressed:
        idle_blink = False
        led.clear()
        game_selector.next_game()

def callback_start_game(pin, pressed, duration):
    global game_selector
    if pressed:
        game_selector.run_current_game()

def callback_toggle_led_mode(pin, pressed, duration):
    """
    Toggles between idle blink mode
    """
    global idle_blink

    if pressed:
        if idle_blink:
            idle_blink = False
            led.clear()
        else:
            idle_blink = True

def register_callbacks():
    print("Registering button callbacks...")
    button.start.callback = callback_start_game # type: ignore
    button.select.callback = callback_next_game # type: ignore
    button.a.callback = callback_toggle_led_mode # type: ignore
    button.b.callback = callback_toggle_led_mode # type: ignore

def blink_controller():
    global idle_blink
    leds = led.get_all_leds()
    while True:
        if idle_blink:
            pwm = random.choice(leds)
            pwm.toggle() # Do not fade, as that is blocking and breaks USB
            # TODO: Find a different way to fade the LEDs...
        time.sleep_ms(500)


print("Starting CRASHANDBURN")
game_selector = GameSelector()

idle_blink = True

# Clear buttons and leds
button.clear()
led.clear()

# Register our button callbacks
register_callbacks()

# Start blink controller on second core
_thread.start_new_thread(blink_controller, ())

while True:
    if game_selector.current_game is not None:
        if game_selector.current_game.is_running == False:
            game_selector.current_game = None # Clear the current game
            button.clear() # Clear button callbacks
            led.clear() # Clear LEDs
            register_callbacks() # Re-register the callbacks
    time.sleep(0.1)
    pass