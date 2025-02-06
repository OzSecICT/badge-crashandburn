#!/bin/bash

FIRMWARE="firmware/RPI_PICO2-20241129-v1.24.1.uf2"
URL="https://micropython.org/resources/firmware/RPI_PICO-20240118-v1.22.0.uf2"

# Check if firmware exists, download if not
if [ ! -f "$FIRMWARE" ]; then
    echo "Firmware not found."
    exit 1
fi

echo "Put your device into bootloader mode (hold BOOTSEL and plug in USB)."
read -p "Press Enter to continue when ready..."

# Find the RP2040's mounted drive
MOUNT_POINT=$(mount | grep "RP2350" | awk '{print $1}' | cut -d' ' -f1)
if [ -z "$MOUNT_POINT" ]; then
    echo "Error: Device not found. Make sure it's in bootloader mode."
    exit 1
fi

# Copy firmware to RP2040
echo "Flashing MicroPython..."
cp "$FIRMWARE" "$MOUNT_POINT" && sync
echo "Done! Device should reboot into MicroPython."
