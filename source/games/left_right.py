"""
Left Right Game

This game is a simple guessing game where the player needs to determine
which LED will light up by pressing a left or right button. Success will
result in a success LED, while failure will continue the game.

This is intended to be a very simple game to be used during development
of the overall badge firmware, and to demonstrate how to create a game
and launch into that game from the main.py.

Requirements:
- Two decision LED's
- One success LED
- Optional fail LED
- Two buttons

NOTE: This script is not tested and likely not working at the moment.
"""

import time
import random

import button
import led

# Use led.game_select_one and led.game_select_two for the decision LEDs
# Use led.badge_complete for the success LED
# Use led.pico_internal for the fail LED

def flash_leds():
    for _ in range(5):
        led.game_select_one.on()
        led.game_select_two.on()
        time.sleep(0.2)
        led.game_select_one.off()
        led.game_select_two.off()
        time.sleep(0.2)

def wait_for_button_press():
    while True:
        if not button.left.value():
            return 'left'
        if not button.right.value():
            return 'right'

def run():
    while True:
        if button.select.value():
            return
        
        chosen_led = random.choice(['left', 'right'])
        flash_leds()
        
        user_choice = wait_for_button_press()
        
        if chosen_led == 'left':
            led.game_select_one.on()
        else:
            led.game_select_two.on()
        
        time.sleep(1)
        
        if user_choice == chosen_led:
            led.badge_complete.on()
            time.sleep(1)
            led.badge_complete.off()
        
        led.game_select_one.off()
        led.game_select_two.off()
    
if __name__ == '__main__':
    run()
