#!/bin/bash

# Directory containing MicroPython scripts
SOURCE_DIR="./source"

# Function to upload files using mpremote
upload_files() {
    echo "============================================="
    echo "📤 Uploading files to device..."
    mpremote connect usb: fs mkdir /source 2>/dev/null
    mpremote connect usb: fs cp -r ${SOURCE_DIR}/* :/source/
    
    if [ $? -eq 0 ]; then
        echo "✅ Upload successful!"
    else
        echo "❌ Upload failed! Check mpremote and device connection."
        return
    fi

    echo "🔄 Resetting device..."
    mpremote connect usb: reset

    echo "✅ Device reset. Waiting for a new device..."
    echo "============================================="
}

# Loop to continuously upload files when a new device is connected
while true; do
    echo "🔍 Waiting for device to connect..."
    
    # Wait until device appears
    while ! mpremote connect usb: exec "print('Connected')" &>/dev/null; do
        sleep 2
    done
    
    echo "✅ device detected!"
    upload_files
done
