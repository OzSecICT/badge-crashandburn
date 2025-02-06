@echo off
set FIRMWARE=firmware/RPI_PICO2-20241129-v1.24.1.uf2
set URL=https://micropython.org/resources/firmware/RPI_PICO-20240118-v1.22.0.uf2

if not exist %FIRMWARE% (
    echo Firmware not found.
    exit /b
)

echo Put your Device into bootloader mode (hold BOOTSEL and plug in USB).
pause

:: Find RP2040 drive
for /f "delims=" %%D in ('wmic logicaldisk get caption^, volumename ^| findstr "RP2350"') do set DRIVE=%%D

if "%DRIVE%"=="" (
    echo Error: Device not found. Make sure it's in bootloader mode.
    exit /b
)

:: Copy firmware
echo Flashing MicroPython...
copy %FIRMWARE% %DRIVE%\
echo Done! Device should reboot into MicroPython.
