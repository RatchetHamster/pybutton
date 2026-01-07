import subprocess
from gpiozero import Button

button = Button(23)
button.wait_for_press()
subprocess.call(['sudo reboot -h now'], shell=True)
