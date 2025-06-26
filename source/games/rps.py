"""
Rock Paper Scissors Game

Single and multiplayer game of Rock Paper Scissors using UART communication
over GPIO pins for multiplayer mode.
"""
from machine import UART
import random
import time

import button
import led
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
        self.score = 0
        self.options = ["ROCK", "PAPER", "SCISSORS"]
        self.uart = UART(0, baudrate=9600, \
                        tx=pinout.pin_rps_tx, \
                        rx=pinout.pin_rps_rx)

    def register_callbacks(self):
        button.left.callback = self.clicked_left  # type: ignore
        button.right.callback = self.clicked_right  # type: ignore
        button.up.callback = self.clicked_up # type: ignore
        button.a.callback = self.cancel_choice  # type: ignore
        button.b.callback = self.select_choice  # type: ignore
        button.select.callback = self.clicked_select  # type: ignore

    def select_choice(self, pin, pressed, duration):
        """
        Lock in the player's selection.
        """
        if pressed:
            if self.player_choice is not None:
                self.player_selected = True
                print(f"Player locked in choice: {self.player_choice}")
                if self.peer_selected:
                    self.determine_winner(self.player_choice, self.peer_choice)
                    self.reset()
            else:
                print("No choice made to lock in.")

    def reset(self):
        """
        Reset the game state for a new round.
        """
        self.player_choice = None
        self.player_selected = False
        self.peer_choice = None
        self.peer_selected = False
        led.rps_rock.clear()
        led.rps_paper.clear()
        led.rps_scissors.clear()
        print("Game state reset for a new round.")

        self.play_bot()  # Simulate bot choice for next round

    def clicked_up(self, pin, pressed, duration):
        """
        Handle the up button being pressed.
        """
        if pressed:
            print("Player selected ROCK")
            led.rps_rock.on()
            led.rps_paper.clear()
            led.rps_scissors.clear()
            self.player_choice = "ROCK"
    
    def clicked_left(self, pin, pressed, duration):
        """
        Handle the left button being pressed.
        """
        if pressed:
            print("Player selected SCISSORS")
            led.rps_scissors.on()
            led.rps_rock.clear()
            led.rps_paper.clear()
            self.player_choice = "SCISSORS"

    def clicked_right(self, pin, pressed, duration):
        """
        Handle the right button being pressed.
        """
        if pressed:
            print("Player selected PAPER")
            led.rps_paper.on()
            led.rps_rock.clear()
            led.rps_scissors.clear()
            self.player_choice = "PAPER"

    def cancel_choice(self, pin, pressed, duration):
        """
        Cancel the player's selection.
        """
        if pressed:
            if self.player_selected:
                self.player_choice = None
                self.player_selected = False
                print("Player cancelled their choice.")
            else:
                print("No choice to cancel.")
            
            led.rps_rock.clear()
            led.rps_paper.clear()
            led.rps_scissors.clear()

    def play_bot(self):
        """
        Simulate a bot playing the game by randomly selecting an option.
        This is for single-player mode.
        """
        if not self.player_selected:
            self.peer_choice = random.choice(self.options)
            self.peer_selected = True
            print(f"Bot selected: {self.peer_choice}")

    def run(self):
        """
        Game loop for Rock Paper Scissors.
        """
        super().run() # Call the parent run method to clear buttons/leds.
        print("Starting Rock Paper Scissors Game")
        led.rps_complete.flash(0.5)

        self.play_bot()

        # Test if multiplayer is available
        # self.check_link()

        print("Use DPAD to choose Scissors [<], Rock [^], or Paper [>].\nPress A to lock in selection.")


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
            if self.uart.any():
                return True
        except Exception as e:
            print(f"UART error: {e}")
        return False
    
    def determine_winner(self, player_choice, peer_choice):
        """
        Determine the winner based on player and peer choices.
        """
        if player_choice == peer_choice:
            print(f"It's a tie! Your score remains {self.score}.")
        elif (player_choice == "ROCK" and peer_choice == "SCISSORS") or \
             (player_choice == "PAPER" and peer_choice == "ROCK") or \
             (player_choice == "SCISSORS" and peer_choice == "PAPER"):
            self.score += 1
            print(f"Player wins! Score is now {self.score}")
        else:
            print(f"Peer wins! Your score remains {self.score}")

        self.peer_selected = False
        self.player_selected = False

    def send_choice(self, choice):
        """
        Send the player's choice to the peer over UART.
        """
        if self.uart:
            self.uart.write(choice.encode('utf-8'))
            print(f"Sent choice: {choice}")
        else:
            print("UART not available, cannot send choice.")

    def receive_choice(self):
        """
        Receive the peer's choice from UART.
        """
        if self.uart.any():
            choice = self.uart.read(1).decode('utf-8')
            print(f"Received choice: {choice}")
            return choice
        return None