"""
Left Right Game

This game is a simple guessing game where the player needs to determine
which LED will light up by pressing a left or right button. Success will
result in a success LED, while failure will continue the game.
"""

import time
import random

import button
import led
from game import Game

class LeftRightGame(Game):
    def __init__(self):
        super().__init__() # Call the parent class constructor
        self.user_choice = None
        self.chosen_led = None

    def run(self):
        super().run() # Call the parent run method to clear buttons/leds.
        self.chosen_led = random.choice(['left', 'right'])
        print("Running Left Right Game")
        print("A random LED has been chosen, left or right.")
        print("Make your choice, and see if you guessed correctly!")
        print("Press A for left, B for right.")
        print("Press SELECT to exit")
        self.flash_leds()

    def register_callbacks(self):
        button.left.callback = self.clicked_a
        button.right.callback = self.clicked_b
        button.a.callback = self.clicked_a
        button.b.callback = self.clicked_b
        button.select.callback = self.clicked_select
    
    def clicked_a(self, pin, pressed, duration):
        if pressed:
            self.user_choice = 'left'
            self.check_guess()

    def clicked_b(self, pin, pressed, duration):
        if pressed:
            self.user_choice = 'right'
            self.check_guess()

    def clicked_select(self, pin, pressed, duration):
        if pressed:
            self.exit()

    def flash_leds(self):
        for _ in range(5):
            led.game_select_one.on()
            led.game_select_two.on()
            time.sleep(0.2)
            led.game_select_one.off()
            led.game_select_two.off()
            time.sleep(0.2)

    def check_guess(self):
        if self.chosen_led == self.user_choice:
            print("You win!")
            led.badge_complete.on()
        else:
            print("You're wrong! Try again!")
            self.run()