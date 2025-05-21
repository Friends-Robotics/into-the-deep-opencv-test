from gpiozero import Servo
from time import sleep

# Create a Servo object on pin 18
servo = Servo(18)

# Sweep the servo
try:
    while True:
        servo.min()  # Move to 0 degrees
        sleep(1)
        servo.max()  # Move to 180 degrees
        sleep(1)
except KeyboardInterrupt:
    pass

