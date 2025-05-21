from adafruit_servokit import ServoKit
import time

# Setup PCA9685 with 16 channels
kit = ServoKit(channels=16)

def move_servo(channel, angle):
    angle = max(0, min(180, angle))
    kit.servo[channel].angle = angle
    return angle

def release_servo():
    for i in range(16):
        kit.servo[i].angle = None

