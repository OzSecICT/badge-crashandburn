"""
LED configuration.

This script sets up each of the available LEDs on the badge.
"""

from machine import Pin, PWM

class LED:
    def __init__(self, pin, is_pwm=False):
        self.pin = pin
        self.is_pwm = is_pwm
        if is_pwm:
            self.pwm = PWM(Pin(pin))
            self.pwm.freq(1000)  # Set PWM frequency to 1kHz
        else:
            self.gpio = Pin(pin, Pin.OUT)

    def on(self):
        if self.is_pwm:
            self.pwm.duty_u16(65535)  # Full brightness
        else:
            self.gpio.value(1)

    def off(self):
        if self.is_pwm:
            self.pwm.duty_u16(0)
        else:
            self.gpio.value(0)

    def set_brightness(self, brightness):
        if self.is_pwm:
            if 0 <= brightness <= 100:
                # Convert 0-100 to 0-65535
                duty = int(brightness * 655.35)
                self.pwm.duty_u16(duty)
            else:
                raise ValueError("Brightness must be between 0 and 100")
        else:
            raise ValueError("Cannot set brightness on non-PWM LED")

# Standard LED definitions
badge_complete = LED(25)
game_select = LED(8)

# PWM-controlled LED definitions
# led2 = LED(1, is_pwm=True)
