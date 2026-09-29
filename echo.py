"""
Echo game for Raspberry Pi
"""

from datetime import datetime
import subprocess
import time
from RPi import GPIO

PIN = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(PIN) == 0:  # Button was pressed
        FILE_NAME = str(datetime.now()) + ".wav"
        record_command = [
            "arecord",
            "-D", "sysdefault:CARD=3",
            "-f", "S16_LE",
            "-r", "48000",
            "-c", "1",
            "-d", "4",
            FILE_NAME
        ]
        try:
            subprocess.run(record_command)
            time.sleep(0.3)
            subprocess.run(["aplay", "-D", "plughw:2,0", FILE_NAME])
        except Exception as e:
            print(f"Error: {e}")

        # Wait for button release
        while GPIO.input(PIN) == 0:
            time.sleep(0.01)
        time.sleep(0.3)

    time.sleep(0.1)
