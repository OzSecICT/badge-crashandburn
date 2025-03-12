"""
LED configuration.

This script sets up each of the available LEDs on the badge.
"""

from machine import Pin, PWM, Timer


class LED:
    def __init__(self, pin, is_pwm=False):
        self.pin = pin
        self.is_pwm = is_pwm
        self.timer = None
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
        
    def toggle(self, timer=None):
        if self.is_pwm:
            if self.pwm.duty_u16() == 0:
                self.on()
            else:
                self.off()
        else:
            if self.gpio.value() == 0:
                self.on()
            else:
                self.off()
        
    def flash(self, duration_ms):
        # Setup a timer to flash the led
        if self.timer is not None:
            self.timer.deinit() # Stop existing timer
        
        self.timer = Timer(-1)
        self.timer.init(period=duration_ms,
                        mode=Timer.PERIODIC,
                        callback=self.toggle)

    def clear(self):
        if self.timer is not None:
            self.timer.deinit()
            self.off()
            self.timer = None
        self.off()

def clear():
    """
    Turn off all LEDs.
    """
    # @todo Need to make this dynamic in some fashion.
    # Storing led's in a list?
    game_select_one.clear()
    game_select_two.clear()
    badge_complete.clear()
    pico_internal.clear()

# Standard LED definitions
game_select_one = LED(8)
game_select_two = LED(9)
game_select_three = LED(11)
badge_complete = LED(10)
pico_internal = LED(25)

# PWM-controlled LED definitions
# led2 = LED(1, is_pwm=True)
