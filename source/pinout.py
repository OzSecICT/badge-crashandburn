# Pinout options
from machine import Pin

pinout_type = "prototype"

if pinout_type == "prototype":
    pin_sda = Pin(0, Pin.IN, Pin.PULL_UP)  # I2C SDA
    pin_scl = Pin(1, Pin.IN, Pin.PULL_UP)  # I2C SCL

else:
    pin_sda = Pin(2, Pin.IN, Pin.PULL_UP)  # I2C SDA
    pin_scl = Pin(3, Pin.IN, Pin.PULL_UP)  # I2C SCL