@echo off
set SOURCE_DIR=source

echo =============================================
echo 🔍 Waiting for device to connect...

:loop
:: Check for device connection in a loop
:wait
mpremote connect usb: exec "print('Connected')" >nul 2>&1
if %errorlevel% neq 0 (
    timeout /t 2 >nul
    goto wait
)

echo ✅ Device detected!
echo 📤 Uploading files to device...

mpremote connect usb: fs mkdir /source 2>nul
mpremote connect usb: fs cp -r %SOURCE_DIR%\* :/source/
if %errorlevel% neq 0 (
    echo ❌ Upload failed! Check mpremote and device connection.
    goto loop
)

echo ✅ Upload successful!
echo 🔄 Resetting device...
mpremote connect usb: reset

echo ✅ Device reset. Waiting for a new device...
echo =============================================

goto loop
