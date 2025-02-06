# OzSec 2025 Badge: CRASHANDBURN
This is the git repo for the code and supporting documents for the OzSec 2025 badge, codename CRASHANDBURN.

This badge will be built in MicroPython on an RP2040 or RP2350, and support multiple minigames.

This repo is currently a work in progress as we start planning how to lay out the badge firmware.

## Contributing
You will need a few things to help develop the badge firmware:
- Visual Studio Code
- VS Code Extensions: Python, Pylance
- Python 3.12+
- mpremote 1.24+

Install Python, and then install `mpremote`. Install VS Code, and clone this repository. Open the repo in VS Code and install the recommended extensions.

Currently the badge firmware is developed with a Raspberry Pi Pico 2 on a breadboard. If you want to see the code, obtain one and follow these steps to get it setup:
- Plugin drive while holding BOOTSEL and use the flash script or VS Code Task to flash firmware. 
    - In VS Code, hit Ctrl+Shift+P or Cmd+Shift+B and choose `Tasks: Run Task` followed by `Flash MicroPython Firmware`.
- After you make changes to the code, hit Ctrl+Shift+B or Cmd+Shift+B to automatically upload the code and reset the device.
