"""
CRASHANDBURN Main.py

This is the main script for the CRASHANDBURN badge firmware. 

By default this script will blink LED's, and wait for input to
select a different game/mode.


"""

from machine import Timer

import button
import led
import games.left_right
import games.light

class GameSelector:
    def __init__(self):
        self.games = [
            {"led": led.game_select_one, "module": games.left_right},
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
        self.games[self.current_index]["module"].run()

def idle_blink():
    """
    Blinks LED's, this is the default mode.
    """
    tim = Timer()
    game_selector = GameSelector()

    def blink(timer):
        print(f"Blinking LED for game at index {game_selector.current_index}")
        game_selector.games[game_selector.current_index]["led"].toggle()

    tim.init(freq=2, mode=Timer.PERIODIC, callback=blink)

    def select_game(pin):
        print("Select button pressed")
        tim.deinit()
        game_selector.next_game()
        idle_blink()

    def start_game(pin):
        print("Start button pressed")
        tim.deinit()
        game_selector.run_current_game()
        idle_blink()

    button.select.irq(trigger=button.Pin.IRQ_FALLING, handler=select_game)
    button.start.irq(trigger=button.Pin.IRQ_FALLING, handler=start_game)

if __name__ == "__main__":
    print("Starting idle blink mode")
    idle_blink()
