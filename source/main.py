"""
CRASHANDBURN Main.py

This is the main script for the CRASHANDBURN badge firmware. 

By default this script will blink LED's, and wait for input to
select a different game/mode.


"""

from machine import Pin, Timer

# import button
import led
# import games.left_right

def idle_blink():
    """
    Blinks LED's, this is the default mode.
    """
    tim = Timer()
    # button = Pin("BUTTON", Pin.IN, Pin.PULL_UP)
    
    # def check_button(timer):
    #     if not button.value():
    #         timer.deinit()
    #         led.off()
    #         return
    
    def blink(led):
        led.toggle()
    # TODO: I don't think this is working.
    tim.init(freq=2, mode=Timer.PERIODIC, callback=blink(led))

if __name__ == "__main__":
    idle_blink()
