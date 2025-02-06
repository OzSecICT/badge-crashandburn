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

from machine import Pin
import time
import random
import sys

sys.path.append("..")  # Add parent directory to import path for butt

import button
import led

# TODO: redefine this using the above imports.
# Define pins for LEDs and buttons
led_left = Pin(2, Pin.OUT)
led_right = Pin(3, Pin.OUT)
button_left = Pin(4, Pin.IN, Pin.PULL_UP)
button_right = Pin(5, Pin.IN, Pin.PULL_UP)
success_led = Pin(6, Pin.OUT)
fail_led = Pin(7, Pin.OUT)

def flash_leds():
    for _ in range(5):
        led_left.on()
        led_right.on()
        time.sleep(0.2)
        led_left.off()
        led_right.off()
        time.sleep(0.2)

def wait_for_button_press():
    while True:
        if not button_left.value():
            return 'left'
        if not button_right.value():
            return 'right'

def run():
    while True:
        chosen_led = random.choice(['left', 'right'])
        flash_leds()
        
        user_choice = wait_for_button_press()
        
        if chosen_led == 'left':
            led_left.on()
        else:
            led_right.on()
        
        time.sleep(1)
        
        if user_choice == chosen_led:
            success_led.on()
            time.sleep(1)
            success_led.off()
        
        led_left.off()
        led_right.off()
    
if __name__ == '__main__':
    run()
