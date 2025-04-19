# Component Bill of Materials

This is the current planned/work in progress bill of materials.

https://jlcpcb.com/partdetail/Waveshare-1_8inch_LCDModule/C359940 - round
https://jlcpcb.com/partdetail/C42370667 / https://www.waveshare.com/1.28inch-touch-lcd.htm - new, round with touch

https://jlcpcb.com/partdetail/Hs-HS96L03W2C03/C5248080 - small square
https://jlcpcb.com/partdetail/Newvisio-N087_2832TSWYG02H14/C2890610 - small rectangle

## TODO
Update 1k resistors to 0402 like the Crystal
Update footprint of controller buttons, currently using the reset/boot buttons.
Add jtag header
add uart header
add gpio headers


## USB Connector
USB-C Connector: [C2988369](https://jlcpcb.com/partdetail/gswitch-GT_USB7010ASV/C2988369)
ESD Protection: [C2827654](https://jlcpcb.com/partdetail/TechPublic-USBLC62SC6/C2827654)
USB-C 5.1k resistors x2: [C27834](https://jlcpcb.com/partdetail/26648-0402WGF5101TCE/C25905)

## Charge Controller
Controller: C478383
Capacitor 1uF: C52923
Resistors 2k x2: C17604
Fuse: C261957
Power Switch: C431541
AA Connectors x2: C2979179
Charge LED Yellow: C2296

## Voltage Regulator
Regulator: C15578
Capcitor 1uF: C1525
Capcitor 100uF: C15008
LED resistor 1k: C17513
LED green: C2297

## RP Crystal
Crystal: C20625731 $0.1980
Resistor 1k: C17513 $0.0017
Capacitor 15pF 2x: C1644 $0.0045

## RP Flash
Chip: C97521 $0.3375
Capacitor 100nF: C1525 $0.0010
Resistor 0ohm: C17168 $0.0005


## RP2350
Chip: C42415655 $1.1760
Resistor 27ohm x2: C138021 $0.0006
Reset and boot switches: C318884 $0.0146
resistor 33ohm: C25105 $0.0005
resistor 1k x2: C17513 $0.0017
capacitor 100nF x11: C307331 $0.0052
capacitor 4.7uF x4: C23733 $0.0050
Inductor: C42411119 $0.1967



ESP32-S3-WROOM-1-N8R8: $3.92
RP2350 and friends: $1.82
CH32V003F4U6: $0.1863