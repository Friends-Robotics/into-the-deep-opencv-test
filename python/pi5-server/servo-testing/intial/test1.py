import time
import board
import busio
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(board.SCL, board.SDA)
pca = PCA9685(i2c)
pca.frequency = 50

# Servo channel
servo = pca.channels[0]

try:
    while True:
        print("Moving to min position")
        servo.duty_cycle = 0x0666  # ~1ms pulse
        time.sleep(1)
        print("Moving to max position")
        servo.duty_cycle = 0x0CCC  # ~2ms pulse
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    pca.deinit()

