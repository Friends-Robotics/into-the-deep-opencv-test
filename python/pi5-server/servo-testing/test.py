from adafruit_servokit import ServoKit
import time

# Setup PCA9685 with 16 channels (default address 0x40)
kit = ServoKit(channels=16)

# Use channel 0 for your servo (can change if needed)
SERVO_CHANNEL = 0

def move_servo(angle):
    # Clamp angle to 0–180 just in case
    angle = max(0, min(180, angle))
    kit.servo[SERVO_CHANNEL].angle = angle
    print(f"Moved to {angle}°")
    time.sleep(0.5)

try:
    while True:
        val = input("Enter angle (0–180) or 'q' to quit: ")
        if val.lower() == 'q':
            break
        try:
            angle = int(val)
            move_servo(angle)
        except ValueError:
            print("Invalid input. Please enter a number or 'q'.")
finally:
    kit.servo[SERVO_CHANNEL].angle = None  # release servo
    print("Exiting. Servo released.")

