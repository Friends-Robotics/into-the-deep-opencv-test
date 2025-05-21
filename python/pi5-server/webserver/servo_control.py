from adafruit_servokit import ServoKit
import time

# Setup PCA9685 with 16 channels
kit = ServoKit(channels=16)
SERVO_CHANNEL = 0

def move_servo(angle):
    angle = max(0, min(180, angle))
    kit.servo[SERVO_CHANNEL].angle = angle
    time.sleep(0.5)
    return angle

def release_servo():
    kit.servo[SERVO_CHANNEL].angle = None

