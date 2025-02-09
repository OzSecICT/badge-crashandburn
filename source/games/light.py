"""
Light Game

Press the A button and light up the game_select_one LED.
Press the B button and light up the game_select_two LED.
"""

import button
import led

def run():
    while True:
        if button.select.value():
            return
        
        if not button.a.value():
            led.game_select_one.on()
        else:
            led.game_select_one.off()
        
        if not button.b.value():
            led.game_select_two.on()
        else:
            led.game_select_two.off()


if __name__ == '__main__':
    run()