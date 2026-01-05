"""
LED configuration.

This script sets up each of the available LEDs on the badge.
"""

from machine import Pin, PWM, Timer
import time

import pinout


class LEDTimerManager:
    """Singleton timer manager for all LED flashing/fading"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.timer = None  # Lazy initialization
            cls._instance.leds = []
            cls._instance.running = False
        return cls._instance

    def add_led(self, led, period_ms, callback):
        """Add an LED to the managed list"""
        # Remove if already exists
        self.remove_led(led)

        # Add with its settings
        self.leds.append({
            'led': led,
            'period': period_ms,
            'callback': callback,
            'last_toggle': time.ticks_ms()
        })

        # Start timer if not running
        if not self.running:
            self.start()

    def remove_led(self, led):
        """Remove an LED from the managed list"""
        self.leds = [item for item in self.leds if item['led'] != led]

        # Stop timer if no LEDs left
        if not self.leds and self.running:
            self.stop()

    def start(self):
        """Start the timer"""
        if not self.running:
            # Lazy initialization - create timer only when first needed
            if self.timer is None:
                self.timer = Timer(1)  # Use hardware timer 0
            self.timer.init(mode=Timer.PERIODIC, period=50,
                            callback=self._update)
            self.running = True

    def stop(self):
        """Stop the timer"""
        if self.running:
            self.timer.deinit()
            self.running = False

    def _update(self, timer):
        """Update all managed LEDs"""
        now = time.ticks_ms()
        for item in self.leds:
            if time.ticks_diff(now, item['last_toggle']) >= item['period']:
                item['callback'](None)  # Call the LED's callback
                item['last_toggle'] = now


class LED:
    def __init__(self, pin, is_pwm=False, brightness=10):
        self.pin = pin
        self.is_pwm = is_pwm
        self.timer_manager = LEDTimerManager()
        self.is_managed = False  # Track if this LED is being managed by timer
        # Convert 0-100 to 0-65535 for PWM
        self.brightness = int(brightness * 655.35)

        if is_pwm:
            self.pwm = PWM(Pin(pin))
            self.pwm.freq(1000)  # Set PWM frequency to 1kHz
        else:
            self.gpio = Pin(pin, Pin.OUT)

    def on(self, fade=False):
        self.stop_flash()  # Stop any flashing
        if self.is_pwm:
            if fade:
                # Ramp up brightness
                self.pwm.duty_u16(0)
                step = self.brightness // 10
                for duty in range(0, self.brightness + 1, step):
                    self.pwm.duty_u16(duty)
                    time.sleep_ms(50)
            else:
                self.pwm.duty_u16(self.brightness)
        else:
            self.gpio.value(1)

    def off(self, fade=False):
        self.stop_flash()  # Stop any flashing
        if self.is_pwm:
            if fade:
                # Ramp down brightness
                self.pwm.duty_u16(self.brightness)
                step = self.brightness // 10
                for duty in range(self.brightness, -1, -step):
                    self.pwm.duty_u16(duty)
                    time.sleep_ms(50)
            else:
                self.pwm.duty_u16(0)
        else:
            self.gpio.value(0)

    def blink(self, times, duration_ms=500):
        """Blocking blink - doesn't use timers"""
        was_managed = self.is_managed
        if was_managed:
            self.stop_flash()

        # if odd number, add one more blink to return the led to its original state
        if times % 2 != 0:
            times += 1

        for _ in range(times):
            self.on()
            time.sleep_ms(duration_ms // 2)
            self.off()
            time.sleep_ms(duration_ms // 2)

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

    def toggle_fade(self):
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

    def fade(self, timer=None):
        """Toggle with fade effect"""
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

    def flash(self, duration_ms=500):
        """Start flashing the LED using the shared timer manager"""
        self.timer_manager.add_led(self, duration_ms, self.fade)
        self.is_managed = True

    def stop_flash(self):
        """Stop flashing this LED"""
        if self.is_managed:
            self.timer_manager.remove_led(self)
            self.is_managed = False

    def clear(self):
        """Turn off and stop any flashing"""
        self.stop_flash()
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
score_eights = LED(pinout.pin_score_eights)
score_fours = LED(pinout.pin_score_fours)
score_twos = LED(pinout.pin_score_twos)
score_ones = LED(pinout.pin_score_ones)

# Badge LED
badge_complete = LED(pinout.pin_badge_complete, is_pwm=True)
badge_bonus = LED(pinout.pin_badge_bonus, is_pwm=True)

# Game LED definitions
kode_complete = LED(pinout.pin_kode_complete, is_pwm=True)

simon_complete = LED(pinout.pin_simon_complete, is_pwm=True)
simon_left = LED(pinout.pin_simon_left)
simon_right = LED(pinout.pin_simon_right)
simon_up = LED(pinout.pin_simon_up)
simon_down = LED(pinout.pin_simon_down)

hilo_complete = LED(pinout.pin_hilo_complete, is_pwm=True)
hilo_lo = LED(pinout.pin_hilo_lo)
hilo_hi = LED(pinout.pin_hilo_hi)

dtmf_complete = LED(pinout.pin_dtmf_complete, is_pwm=True)
dtmf_bonus = LED(pinout.pin_dtmf_bonus, is_pwm=True)

rps_complete = LED(pinout.pin_rps_complete, is_pwm=True)
rps_rock = LED(pinout.pin_rps_rock)
rps_scissors = LED(pinout.pin_rps_scissors)
rps_paper = LED(pinout.pin_rps_paper)
