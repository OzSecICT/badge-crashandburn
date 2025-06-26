"""
LED configuration.

This script sets up each of the available LEDs on the badge.
"""

from machine import Pin, PWM, Timer
import time

import pinout

class LED:
    def __init__(self, pin, is_pwm=False, brightness=10):
        self.pin = pin
        self.is_pwm = is_pwm
        self.timer = None
        self.brightness = int(brightness * 655.35)  # Convert 0-100 to 0-65535 for PWM
        self._timer_period = None
        self._timer_mode = None
        self._timer_callback = None

        if is_pwm:
            self.pwm = PWM(Pin(pin))
            self.pwm.freq(1000)  # Set PWM frequency to 1kHz
        else:
            self.gpio = Pin(pin, Pin.OUT)

    def on(self, fade=False):
        if self.timer is not None:
            self.stop_timer()
        if self.is_pwm:
            if fade: # TODO: Change this to a timer based approach.
                # Ramp up brightness
                # Set duty to 0, then gradually increase to self.brightness
                self.pwm.duty_u16(0)
                step = self.brightness // 10  # Adjust step size as needed
                for duty in range(0, self.brightness + 1, step):
                    self.pwm.duty_u16(duty)
                    time.sleep_ms(50)
            else:
                self.pwm.duty_u16(self.brightness)
        else:
            self.gpio.value(1)

    def off(self, fade=False):
        if self.timer is not None:
            self.stop_timer()
        if self.is_pwm:
            if fade: # TODO: Change this to a timer based approach.
                # Ramp down brightness
                # Set duty to self.brightness, then gradually decrease to 0
                self.pwm.duty_u16(self.brightness)
                step = self.brightness // 10  # Adjust step size as needed
                for duty in range(self.brightness, -1, -step):
                    self.pwm.duty_u16(duty)
                    time.sleep_ms(50)
            else:
                self.pwm.duty_u16(0)
        else:
            self.gpio.value(0)

    def blink(self, times, duration_ms=500):
        paused = False
        # if odd number, add one more blink to return the led to its original state.
        if times % 2 != 0:
            times += 1
        if self.timer is not None:
            self.pause_timer()
            paused = True

        self.clear()
        for _ in range(times):
            self.on()
            time.sleep_ms(duration_ms // 2)
            self.off()
            time.sleep_ms(duration_ms // 2)

        # resume timer
        if paused:
            self.start_timer()


    def set_brightness(self, brightness):
        if self.is_pwm:
            if 0 <= brightness <= 100:
                # Convert 0-100 to 0-65535
                self.brightness = int(brightness * 655.35)
                self.pwm.duty_u16(self.brightness)
            else:
                raise ValueError("Brightness must be between 0 and 100")
        else:
            raise ValueError("Cannot set brightness on non-PWM LED")
        
    def toggle(self, timer=None, fade=False):
        if self.is_pwm:
            if self.pwm.duty_u16() == 0:
                self.on(fade=fade)
            else:
                self.off(fade=fade)
        else:
            if self.gpio.value() == 0:
                self.on()
            else:
                self.off()

    def fade(self, timer=None):
        if self.is_pwm:
            if self.pwm.duty_u16() == 0:
                self.on(fade=True)
            else:
                self.off(fade=True)
        else:
            if self.gpio.value() == 0:
                self.on()
            else:
                self.off()
        
    def flash(self, duration_ms):
        # Setup a timer to flash the led
        if self.timer is not None:
            self.stop_timer()
        self.timer = Timer(-1)
        # Store timer values for later use
        self._timer_period = duration_ms
        self._timer_mode = Timer.PERIODIC
        self._timer_callback = self.fade
        # Start timer
        self.start_timer()

    def stop_timer(self):
        if self.timer is not None:
            self.timer.deinit()
            self.timer = None
            self._timer_period = None
            self._timer_mode = None
            self._timer_callback = None

    def pause_timer(self):
        if self.timer is not None:
            self.timer.deinit()
            self.timer = None
    
    def start_timer(self):
        if self.timer is None and self._timer_period is not None and self._timer_mode is not None and self._timer_callback is not None:
            self.timer = Timer(-1)
            self.timer.init(period=self._timer_period,
                            mode=self._timer_mode,
                            callback=self._timer_callback)
        
    def clear(self):
        if self.timer is not None:
            self.stop_timer()
        self.off()

def get_all_leds():
    leds = []
    for obj in globals().values():
        if isinstance(obj, LED):
            leds.append(obj)
    return leds

def clear():
    """
    Turn off all LEDs defined as LED instances in the global scope.
    """
    print("Clearing all LEDs...")
    for led in get_all_leds():
        led.clear()

print("Initializing LEDs...")

# Standard LED definitions
# Scoreboard
# Scorebaord and badge are not PWM, due to limitations in PWM channels and pins
# If they were PWM, they would mirror the other pins on the same pwm channel.
score_eights = LED(pinout.pin_score_eights)
score_fours = LED(pinout.pin_score_fours)
score_twos = LED(pinout.pin_score_twos)
score_ones = LED(pinout.pin_score_ones)

# Badge LED
badge_complete = LED(pinout.pin_badge_complete)
badge_bonus = LED(pinout.pin_badge_bonus)

# Game LED definitions
kode_complete = LED(pinout.pin_kode_complete, is_pwm=True)

simon_complete = LED(pinout.pin_simon_complete, is_pwm=True)
simon_bonus = LED(pinout.pin_simon_bonus, is_pwm=True)
simon_left = LED(pinout.pin_simon_left, is_pwm=True)
simon_right = LED(pinout.pin_simon_right, is_pwm=True)
simon_up = LED(pinout.pin_simon_up, is_pwm=True)
simon_down = LED(pinout.pin_simon_down, is_pwm=True)

hilo_complete = LED(pinout.pin_hilo_complete, is_pwm=True)
hilo_lo = LED(pinout.pin_hilo_lo, is_pwm=True)
hilo_hi = LED(pinout.pin_hilo_hi, is_pwm=True)

dtmf_complete = LED(pinout.pin_dtmf_complete, is_pwm=True)
dtmf_bonus = LED(pinout.pin_dtmf_bonus, is_pwm=True)

rps_complete = LED(pinout.pin_rps_complete, is_pwm=True)
rps_bonus = LED(pinout.pin_rps_bonus, is_pwm=True)
rps_rock = LED(pinout.pin_rps_rock, is_pwm=True)
rps_scissors = LED(pinout.pin_rps_scissors, is_pwm=True)
rps_paper = LED(pinout.pin_rps_paper, is_pwm=True)

# PWM-controlled LED definitions
# led2 = LED(1, is_pwm=True)
