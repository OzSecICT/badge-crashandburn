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
        
def clicked_a(pin, pressed, duration):
    global user_choice
    if pressed:
        user_choice = 'left'
        

def clicked_b(pin, pressed, duration):
    global user_choice
    if pressed:
        user_choice = 'right'


def run():
    user_choice = None
    chosen_led = random.choice(['left', 'right'])

    while user_choice is None:
        flash_leds()
        print("Make a selection!")

    if chosen_led == 'left' and user_choice == 'left':
        print("You win!")
        for _ in range(5):
            led.badge_complete.on()
            time.sleep(0.5)
            led.badge_complete.off()
    
    if chosen_led == 'right' and user_choice == 'right':
        print("You win!")
        for _ in range(5):
            led.badge_complete.on()
            time.sleep(0.5)
            led.badge_complete.off()
    
    led.game_select_one.off()
    led.game_select_two.off()
    print("Game Over!")
    
if __name__ == '__main__':
    run()
