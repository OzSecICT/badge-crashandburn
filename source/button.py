"""
Button configuration.

This script manages button configurations and is imported when needed.
"""
from machine import Pin, Timer
import time

class DebouncedInput: # https://github.com/jmcclin2/updebouncein
    """Micropython Debounced GPIO Input Class"""
    def __init__(self, pin_num, callback, pin_pull=None, pin_logic_pressed=True, debounce_ms=100):
        self.pin_num = pin_num
        self.pin_pull = pin_pull
        self.pin_logic_pressed = pin_logic_pressed
        self.debounce_ms = debounce_ms
        self.callback = callback
        self.last_release_ms = 0
        self.last_press_ms = 0

        self.pin = Pin(self.pin_num, Pin.IN, self.pin_pull)
        self.pin.irq(self.__ButtonHandler, Pin.IRQ_FALLING | Pin.IRQ_RISING)
    
        self.db_timer = Timer(-1)
        self.expected_value = True

    def __ButtonDebounceTimerExpired(self, timer):
           
        current_value = False   
           
        if (self.pin.value() == self.pin_logic_pressed):
            current_value = True
        else:
            current_value = False
        
        if ((self.expected_value == True) and (current_value == True)):
            #print("Button pressed")
            self.expected_value = False
            self.last_press_ms = time.ticks_ms()
            if (self.last_release_ms == 0):
                ms_since_last_press = 0
            else:
                ms_since_last_press = time.ticks_diff(self.last_press_ms, self.last_release_ms) + 2*self.debounce_ms
            if(self.callback is not None): # Ensure callback is not None - ruff
                self.callback(self.pin_num, True, ms_since_last_press)
        elif ((self.expected_value == False) and (current_value == False)):
            #print("Button released")
            self.expected_value = True
            self.last_release_ms = time.ticks_ms()
            ms_duration_of_press = time.ticks_diff(self.last_release_ms, self.last_press_ms) + 2*self.debounce_ms
            if(self.callback is not None): # Ensure callback is not None - ruff
                self.callback(self.pin_num, False, ms_duration_of_press)
        #else:
            #print("Missed edge: expected:", self.expected_value, " actual:", current_value)
            
        # Re-enable pin interrupt
        self.pin.irq(self.__ButtonHandler, Pin.IRQ_FALLING | Pin.IRQ_RISING)

    def __ButtonHandler(self, pin):
        
        #print("IRQ with flags:", pin.irq().flags())
        self.db_timer.init(mode=Timer.ONE_SHOT, period=self.debounce_ms, callback=self.__ButtonDebounceTimerExpired)
        
        # Disable pin interrupt
        self.pin.irq(trigger=0)

def clear():
    start.callback = None
    select.callback = None
    a.callback = None
    b.callback = None
    left.callback = None
    up.callback = None
    down.callback = None
    right.callback = None

start = DebouncedInput(0, None, Pin.PULL_UP, False, 100)
select = DebouncedInput(1, None, Pin.PULL_UP, False, 100)
a = DebouncedInput(2, None, Pin.PULL_UP, False, 100)
b = DebouncedInput(3, None, Pin.PULL_UP, False, 100)
left = DebouncedInput(4, None, Pin.PULL_UP, False, 100)
up = DebouncedInput(5, None, Pin.PULL_UP, False, 100)
down = DebouncedInput(6, None, Pin.PULL_UP, False, 100)
right = DebouncedInput(7, None, Pin.PULL_UP, False, 100)