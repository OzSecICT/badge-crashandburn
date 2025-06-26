"""
Pinout configuration

Defines pins for prototyping and production. Prototype versions used a Pico 2
which does not have enough GPIO available for all games.

Prototype_1: Missing I2C, SAO GPIO, Simon, and DTMF games
Prototype_2: Missing I2C, SAO GPIO, HiLo and RPS game.
Production: All pins available.
"""
from machine import Pin

pinout_type = "prototype_1"

print(f"Using pinout type: {pinout_type}")


if pinout_type == "prototype_1":
    # UART and I2C
    pin_uart0_tx = 0
    pin_uart0_rx = 1
    pin_i2c0_sda = 25
    pin_i2c0_scl = 25

    # SAO
    pin_sao_gpio2 = 25
    pin_sao_gpio1 = 25

    # Controller inputs
    pin_button_a = 2
    pin_button_b = 3
    pin_button_select = 4
    pin_button_start = 5
    pin_dpad_right = 7
    pin_dpad_down = 6
    pin_dpad_up = 8
    pin_dpad_left = 9

    # Scoreboard
    pin_score_eights = 10
    pin_score_fours = 11
    pin_score_twos = 12
    pin_score_ones = 13

    # Badge/Raffle LEDs
    pin_badge_complete = 25
    pin_badge_bonus = 14

    # Game LEDs
    pin_kode_complete = 15

    pin_simon_complete = 25
    pin_simon_bonus = 25
    pin_simon_left = 25
    pin_simon_right = 25
    pin_simon_up = 25
    pin_simon_down = 25

    pin_hilo_complete = 26
    pin_hilo_lo = 27
    pin_hilo_hi = 28

    pin_dtmf_bonus = 25
    pin_dtmf_complete = 25
    pin_dtmf_mic = 25 # 26 ADC0

    pin_rps_tx = 16
    pin_rps_rx = 17
    pin_rps_rock = 18
    pin_rps_scissors = 19
    pin_rps_paper = 20
    pin_rps_complete = 21
    pin_rps_bonus = 22

if pinout_type == "prototype_2":
    # UART and I2C
    pin_uart0_tx = 0
    pin_uart0_rx = 1
    pin_i2c0_sda = 25
    pin_i2c0_scl = 25

    # SAO
    pin_sao_gpio2 = 25
    pin_sao_gpio1 = 25

    # Controller inputs
    pin_button_a = 2
    pin_button_b = 3
    pin_button_select = 4
    pin_button_start = 5
    pin_dpad_right = 7
    pin_dpad_down = 6
    pin_dpad_up = 8
    pin_dpad_left = 9

    # Scoreboard
    pin_score_eights = 10
    pin_score_fours = 11
    pin_score_twos = 12
    pin_score_ones = 13

    # Badge/Raffle LEDs
    pin_badge_complete = 25
    pin_badge_bonus = 14

    # Game LEDs
    pin_kode_complete = 15

    pin_simon_complete = 16
    pin_simon_bonus = 17
    pin_simon_left = 18
    pin_simon_right = 19
    pin_simon_up = 20
    pin_simon_down = 21

    pin_hilo_complete = 25
    pin_hilo_lo = 25
    pin_hilo_hi = 25

    pin_dtmf_bonus = 22
    pin_dtmf_complete = 27
    pin_dtmf_mic = 26 # 26 ADC0

    pin_rps_tx = 25
    pin_rps_rx = 25
    pin_rps_rock = 25
    pin_rps_scissors = 25
    pin_rps_paper = 25
    pin_rps_complete = 25
    pin_rps_bonus = 25

if pinout_type == "production":
    # UART and I2C
    pin_uart0_tx = 0
    pin_uart0_rx = 1
    pin_i2c0_sda = 32
    pin_i2c0_scl = 33

    # SAO
    pin_sao_gpio2 = 28
    pin_sao_gpio1 = 29

    # Controller inputs
    pin_button_a = 16
    pin_button_b = 17
    pin_button_select = 18
    pin_button_start = 19
    pin_dpad_right = 20
    pin_dpad_down = 21
    pin_dpad_up = 22
    pin_dpad_left = 23

    # Scoreboard
    pin_score_eights = 36
    pin_score_fours = 37
    pin_score_twos = 38
    pin_score_ones = 39

    # Badge/Raffle LEDs
    pin_badge_complete = 34
    pin_badge_bonus = 35

    # Game LEDs
    pin_simon_complete = 2
    pin_simon_bonus = 3
    pin_simon_left = 4
    pin_simon_up = 5
    pin_simon_down = 6
    pin_simon_right = 7

    pin_kode_complete = 24

    pin_hilo_complete = 25
    pin_hilo_lo = 26
    pin_hilo_hi = 27

    pin_dtmf_bonus = 30
    pin_dtmf_complete = 31
    pin_dtmf_mic = 40

    pin_rps_tx = 41
    pin_rps_rx = 42
    pin_rps_rock = 43
    pin_rps_scissors = 44
    pin_rps_paper = 45
    pin_rps_complete = 46
    pin_rps_bonus = 47