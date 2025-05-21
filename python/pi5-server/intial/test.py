import time
import board
import busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo

# I2C bus setup
i2c = busio.I2C(board.SCL, board.SDA)

# PCA9685 setup
pca = PCA9685(i2c)
pca.frequency = 50  # Standard servo frequency (50 Hz)

# Create a servo object on channel 0
servo0 = servo.Servo(pca.channels[0])

# Sweep servo from 0 to 180 and back
try:
    while True:
        for angle in range(0, 181, 5):  # 0 to 180 degrees
            servo0.angle = angle
            time.sleep(0.02)
            print(servo0.angle)
        for angle in range(180, -1, -5):  # 180 to 0 degrees
            servo0.angle = angle
            time.sleep(0.02)
            print(servo0.angle)
except KeyboardInterrupt:
    pass
finally:
    pca.deinit()

