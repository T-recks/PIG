# Load file with `sudo python3 -i i-dc.py`
# Interactively change speed and direction  by setting kit.motor1.throttle

from adafruit_motor import MotorKit
kit = MotorKit()

# Default throttle (not movement)
kit.motor1.throttle = 0

