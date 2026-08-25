import RPi.GPIO as GPIO
import time
import os

butPressed = True

recordBool = False#True if a record is in progress
pin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)#sets Pi's internal resistors to pull-up

while True:
    butPressed = GPIO.input(pin)#checks if a button is pressed
    if butPressed == False:#if a button is pressed
        os.system("aplay -D plughw:CARD=2 test.wav")
    time.sleep(0.1)
