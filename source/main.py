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
    global game_selector
    if pressed:
        stop_blink_timer()
        game_selector.next_game()

def callback_start_game(pin, pressed, duration):
    global game_selector
    if pressed:
        game_selector.run_current_game()

def callback_toggle_led_mode(pin, pressed, duration):
    """
    Callback to toggle the LED state.
    """
    global blinky_mode

    if pressed:
        if blinky_mode:
            stop_blink_timer()
        else:
            start_blink_timer()

def start_blink_timer():
    global idle_timer, blinky_mode

    idle_timer = Timer(-1)
    idle_timer.init(period=1000, mode=Timer.PERIODIC, callback=blink_random)
    blinky_mode = True

def stop_blink_timer():
    global idle_timer, blinky_mode

    if idle_timer is not None:
        idle_timer.deinit()
    blinky_mode = False
    led.clear()

def register_callbacks():
    print("Registering button callbacks...")
    button.start.callback = callback_start_game # type: ignore
    button.select.callback = callback_next_game # type: ignore
    button.a.callback = callback_toggle_led_mode # type: ignore
    button.b.callback = callback_toggle_led_mode # type: ignore

def blink_random(run=True):
    """
    Randomly selects an LED to blink
    """
    global led, blinky_mode
    if run:
        blinky_mode = True
        # Select a random LED
        leds = led.get_all_leds()
        pwm = random.choice(leds)
        pwm.toggle(fade=True)
    else:
        blinky_mode = False
        led.clear()

print("Starting CRASHANDBURN")
game_selector = GameSelector()
idle_timer = None
blinky_mode = False



# Clear buttons and leds
button.clear()
led.clear()

# Register our button callbacks
register_callbacks()

# Start the idle blink
start_blink_timer()

while True:
    if game_selector.current_game is not None:
        if game_selector.current_game.is_running == False:
            game_selector.current_game = None # Clear the current game
            button.clear() # Clear button callbacks
            led.clear() # Clear LEDs
            register_callbacks() # Re-register the callbacks
            
    time.sleep(0.1)
    pass