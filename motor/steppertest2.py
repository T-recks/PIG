import time
from adafruit_motorkit import MotorKit

kit = MotorKit()

for i in range(20000):
        kit.stepper1.onestep()




