# UART comms for RPS
from machine import Pin, UART
import time

# Hardware Configuration (adjust pins if needed)
BUTTON_PIN = 0  # GP0 for button input
LED_PIN = 1     # GP1 for LED output
UART_TX_PIN = 4  # GP4 for UART TX
UART_RX_PIN = 5  # GP5 for UART RX

# Initialize hardware
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_DOWN)
led = Pin(LED_PIN, Pin.OUT)
uart = UART(0, baudrate=9600, tx=Pin(UART_TX_PIN), rx=Pin(UART_RX_PIN))

# Debounce variables
last_button_state = 0
debounce_delay = 50  # ms
last_debounce_time = 0

while True:
    current_time = time.ticks_ms()
    button_state = button.value()
    
    # Button press detection with debounce
    if button_state != last_button_state and current_time - last_debounce_time > debounce_delay:
        last_debounce_time = current_time
        last_button_state = button_state
        
        # Send button state to peer
        uart.write(b'1' if button_state else b'0')
    
    # Check for incoming data
    if uart.any():
        data = uart.read(1)
        if data == b'1':
            led.on()
        elif data == b'0':
            led.off()
    
    time.sleep_ms(10)
