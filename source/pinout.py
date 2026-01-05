"""
Pinout configuration

Defines pins for prototyping and production. Prototype versions used a Pico 2
which does not have enough GPIO available for all games.

Prototype_1: Missing I2C, SAO GPIO, Simon, and DTMF games
Prototype_2: Missing I2C, SAO GPIO, HiLo and RPS game.
Production: All pins available.
"""
from machine import Pin

pinout_type = "production"

print(f"Using pinout type: {pinout_type}")


if pinout_type == "production":
    # Controller inputs
    pin_button_a = 12
    pin_button_b = 13
    pin_button_select = 14
    pin_button_start = 21
    pin_dpad_right = 47
    pin_dpad_down = 48
    pin_dpad_up = 38
    pin_dpad_left = 45

    # Scoreboard
    pin_score_eights = 15
    pin_score_fours = 7
    pin_score_twos = 6
    pin_score_ones = 5

    # Badge/Raffle LEDs
    pin_badge_complete = 2
    pin_badge_bonus = 4

    # Game LEDs
    pin_simon_complete = 46
    pin_simon_left = 11
    pin_simon_up = 3
    pin_simon_down = 10
    pin_simon_right = 9

    pin_kode_complete = 39

    pin_hilo_complete = 40
    pin_hilo_lo = 41
    pin_hilo_hi = 42

    pin_dtmf_bonus = 44
    pin_dtmf_complete = 43
    pin_dtmf_mic = 1

    pin_rps_rock = 16
    pin_rps_scissors = 18
    pin_rps_paper = 17
    pin_rps_complete = 8
