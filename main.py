#!/usr/bin/env python3

from gpiozero import Button
from signal import pause
import os
import logging
#Logger:
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') #Change level of logging output here

button = Button(23, pull_up=True, hold_time=2, hold_repeat=False)
logging.info("Button initiated")

def immediate_press():
    logging.debug("Immediate press detected")

def short_press():
    logging.debug("Short press detected")
    os.system("sudo reboot -h now")

def long_press():
    logging.debug("Long press detected")
    os.system("sudo shutdown -h now")

button.when_pressed = immediate_press
button.when_released = short_press  # fires only if not held
button.when_held = long_press
logging.info("Handles initalised...continuing to pause until trigger")
pause()



