import RPi.GPIO as GPIO
import time

# Set up the GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# Set up PWM on GPIO pin 18 (50Hz for servos)
pwm = GPIO.PWM(18, 50)
pwm.start(0)  # Start PWM with a duty cycle of 0% (servo at 0 degrees)

# Function to move the servo to a given angle
def move_servo(angle):
    duty_cycle = (angle / 18) + 2  # Convert angle to duty cycle
    GPIO.output(18, True)
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)
    GPIO.output(18, False)
    pwm.ChangeDutyCycle(0)

# Sweep the servo from 0 to 180 degrees and back
try:
    while True:
        for angle in range(0, 181, 10):  # Move from 0 to 180 degrees in steps of 10
            move_servo(angle)
        for angle in range(180, -1, -10):  # Move from 180 back to 0
            move_servo(angle)
except KeyboardInterrupt:
    pwm.stop()  # Stop PWM
    GPIO.cleanup()  # Clean up GPIO settings

