"""
Rock Paper Scissors Game

Single and multiplayer game of Rock Paper Scissors using UART communication
over GPIO pins for multiplayer mode.
"""
from machine import Pin, UART
import random
import time
import uart

import pinout
from game import Game

class RPSGame(Game):
    def __init__(self):
        super().__init__()
        print("Initializing Rock Paper Scissors Game")
        self.player_choice = None
        self.player_selected = False
        self.peer_choice = None
        self.peer_selected = False
        self.bot_choice = None
        self.score = 0
        self.options = ["rock", "paper", "scissors"]
        self.uart = UART(0, baudrate=9600, \
                        tx=pinout.pin_rps_tx, \
                        rx=pinout.pin_rps_rx)

    def register_callbacks(self):
        button.left.callback = self.cycle_left  # type: ignore
        button.right.callback = self.cycle_right  # type: ignore
        button.a.callback = self.cancel_choice  # type: ignore
        button.b.callback = self.select_choice  # type: ignore

    def cycle_left(self, pin, pressed, duration):
        """
        Cycle through the options (rock, paper, scissors) when left button is pressed.
        """
        if pressed:
            # Only allow cycling if player hasn't locked in a selection
            if not self.player_selected:
                # Start at the last option if no choice yet
                if self.player_choice is None:
                    self.player_choice = self.options[-1]
                else:
                    idx = self.options.index(self.player_choice)
                    self.player_choice = self.options[(idx - 1) % len(self.options)]
            else:
                print("Player has already selected an option, cannot cycle left.")
            print(f"Player selected: {self.player_choice}")

    def cycle_right(self, pin, pressed, duration):
        """
        Cycle through the options (rock, paper, scissors) when right button is pressed.
        """
        if pressed:
            # Only allow cycling if player hasn't locked in a selection
            if not self.player_selected:
                # Start at the first option if no choice yet
                if self.player_choice is None:
                    self.player_choice = self.options[0]
                else:
                    idx = self.options.index(self.player_choice)
                    self.player_choice = self.options[(idx + 1) % len(self.options)]
            else:
                print("Player has already selected an option, cannot cycle right.")
            print(f"Player selected: {self.player_choice}")

    def select_choice(self, pin, pressed, duration):
        """
        Lock in the player's selection.
        """
        if self.player_choice is not None:
            self.player_selected = True
            print(f"Player locked in choice: {self.player_choice}")
        else:
            print("No choice made to lock in.")

    def cancel_choice(self, pin, pressed, duration):
        """
        Cancel the player's selection.
        """
        if self.player_selected:
            self.player_choice = None
            self.player_selected = False
            print("Player cancelled their choice.")
        else:
            print("No choice to cancel.")

    def run(self):
        """
        Game loop for Rock Paper Scissors.
        """
        super().run() # Call the parent run method to clear buttons/leds.
        print("Starting Rock Paper Scissors Game")

        # Test if multiplayer is available
        # self.check_link()

        # Bot mode if no multiplayer is present
        # Select a random choice
        self.bot_choice = random.choice(self.options)
        print(f"Bot selected: {self.bot_choice}")

        while True:
            # Check if the player has made a choice
            if self.player_selected:
                print(f"Player's choice: {self.player_choice}")
                
                if self.determine_winner(self.player_choice, self.bot_choice) == "player":
                    print("Player wins!")
                    self.score += 1
                else:
                    print("Player lost!")
            else:
                print("Waiting for player to select an option...")
                time.sleep(1)
                # idle led blink?


        # Have a timeout for the player to make a choice

        # Multiplayer mode
        # Wait for the player to select an option
        # Send the player's choice to the peer
        # Wait for the peer to select an option
        # Receive the peer's choice

    def check_link(self):
        """
        Check if the UART link is available for multiplayer.
        """
        try:
            # Attempt to read from the UART
            if uart.any():
                return True
        except Exception as e:
            print(f"UART error: {e}")
        return False
    
    def determine_winner(self, player_choice, peer_choice):
        """
        Determine the winner based on player and peer choices.
        """
        if player_choice == peer_choice:
            print("It's a tie!")
            return None
        elif (player_choice == "rock" and peer_choice == "scissors") or \
             (player_choice == "paper" and peer_choice == "rock") or \
             (player_choice == "scissors" and peer_choice == "paper"):
            print("Player wins!")
            self.score += 1
            return "player"
        else:
            print("Peer wins!")
            return "peer"

    def send_choice(self, choice):
        """
        Send the player's choice to the peer over UART.
        """
        if uart:
            uart.write(choice.encode('utf-8'))
            print(f"Sent choice: {choice}")
        else:
            print("UART not available, cannot send choice.")

    def receive_choice(self):
        """
        Receive the peer's choice from UART.
        """
        if uart.any():
            choice = uart.read(1).decode('utf-8')
            print(f"Received choice: {choice}")
            return choice
        return None