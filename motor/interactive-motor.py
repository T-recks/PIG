# load this file with `sudo python3 -i interactive-motor.py`
# then use `kit` to control motor, e.g. `kit.stepper1.onestep()`
import time
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

kit = MotorKit()
