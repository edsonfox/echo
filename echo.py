"""
Echo game for Raspberry Pi
"""

import subprocess
import time

from RPi import GPIO

PIN = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)#sets Pi's internal resistors to pull-up

while True:
    if GPIO.input(PIN) == 0:  # Button was pressed
        result = subprocess.run(["aplay", "-D", "plughw:CARD=2", "test.wav"],
                                capture_output=True,
                                check=True)
    time.sleep(0.1)
