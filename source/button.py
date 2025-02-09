"""
Button configuration.

This script manages button configurations and is imported when needed.

TODO: These pin numbers are placeholders, define actual pins.
"""

from machine import Pin

start = Pin(0, Pin.IN, Pin.PULL_UP)
select = Pin(1, Pin.IN, Pin.PULL_UP)
a = Pin(2, Pin.IN, Pin.PULL_UP)
b = Pin(3, Pin.IN, Pin.PULL_UP)
left = Pin(4, Pin.IN, Pin.PULL_UP)
up = Pin(5, Pin.IN, Pin.PULL_UP)
down = Pin(6, Pin.IN, Pin.PULL_UP)
right = Pin(7, Pin.IN, Pin.PULL_UP)