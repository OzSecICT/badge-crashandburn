"""
Button configuration.

This script manages button configurations and is imported when needed.
Uses software debouncing (no timers required).
"""
from machine import Pin
import time

import pinout


class DebouncedInput:
    """Micropython Debounced GPIO Input Class - Software Debouncing"""

    def __init__(self, pin_num, callback, pin_pull=None, pin_logic_pressed=True, debounce_ms=100):
        self.pin_num = pin_num
        self.pin_pull = pin_pull
        self.pin_logic_pressed = pin_logic_pressed
        self.debounce_ms = debounce_ms
        self.callback = callback

        # Track state for debouncing
        self.last_change_time = 0
        self.last_state = None
        self.current_state = False

        # Track press/release timing
        self.last_press_ms = 0
        self.last_release_ms = 0

        self.pin = Pin(self.pin_num, Pin.IN, self.pin_pull)
        self.pin.irq(self._irq_handler, Pin.IRQ_FALLING | Pin.IRQ_RISING)

        # Initialize last_state
        self.last_state = (self.pin.value() == self.pin_logic_pressed)

    def _irq_handler(self, pin):
        """Handle pin state changes with debouncing"""
        now = time.ticks_ms()

        # Read current pin state
        pin_value = self.pin.value()
        is_pressed = (pin_value == self.pin_logic_pressed)

        # Check if enough time has passed since last change
        if time.ticks_diff(now, self.last_change_time) < self.debounce_ms:
            # Too soon - ignore this change (debounce)
            return

        # Check if state actually changed
        if is_pressed == self.last_state:
            # No real change - ignore
            return

        # Valid state change detected
        self.last_change_time = now
        self.last_state = is_pressed

        # Calculate timing information
        if is_pressed:
            # Button pressed
            self.last_press_ms = now
            if self.last_release_ms == 0:
                ms_since_last_press = 0
            else:
                ms_since_last_press = time.ticks_diff(
                    now, self.last_release_ms)

            if self.callback is not None:
                self.callback(self.pin_num, True, ms_since_last_press)
        else:
            # Button released
            self.last_release_ms = now
            ms_duration_of_press = time.ticks_diff(now, self.last_press_ms)

            if self.callback is not None:
                self.callback(self.pin_num, False, ms_duration_of_press)


def clear():
    """Clear all button callbacks"""
    start.callback = None
    select.callback = None
    a.callback = None
    b.callback = None
    left.callback = None
    up.callback = None
    down.callback = None
    right.callback = None


print("Initializing buttons...")
start = DebouncedInput(pinout.pin_button_start, None,
                       Pin.PULL_DOWN, False, 100)
print("Start button initialized")
select = DebouncedInput(pinout.pin_button_select, None,
                        Pin.PULL_DOWN, False, 100)
print("Select button initialized")
a = DebouncedInput(pinout.pin_button_a, None, Pin.PULL_DOWN, False, 100)
print("A button initialized")
b = DebouncedInput(pinout.pin_button_b, None, Pin.PULL_DOWN, False, 100)
print("B button initialized")
left = DebouncedInput(pinout.pin_dpad_left, None, Pin.PULL_UP, False, 100)
print("Left button initialized")
up = DebouncedInput(pinout.pin_dpad_up, None, Pin.PULL_UP, False, 100)
print("Up button initialized")
down = DebouncedInput(pinout.pin_dpad_down, None, Pin.PULL_UP, False, 100)
print("Down button initialized")
right = DebouncedInput(pinout.pin_dpad_right, None, Pin.PULL_UP, False, 100)
print("Right button initialized")
print("Buttons initialized successfully.")
