# Import RPi.GPIO and time library
import RPi.GPIO as GPIO
import time

# Set the mode to BOARD
GPIO.setmode(GPIO.BOARD)

# Define the pins used for stepper motor
stepPins = [31, 33, 35, 37]

# Set the GPIO pins as output
for pin in stepPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

# Define a function to make a single step
def singleStep(stepPinSequence):
    for pin in range(4):
        GPIO.output(stepPins[pin], stepPinSequence[pin])

# Define sequences for one full cycle
sequence = [[1,0,0,1],
            [0,0,0,1],
            [0,0,1,1],
            [0,0,1,0],
            [0,1,1,0],
            [0,1,0,0],
            [1,1,0,0],
            [1,0,0,0]]

# Function to rotate the motor
def rotateMotor(direction, delay, steps):
    for _ in range(steps):
        for stepPinSequence in sequence[::direction]:
            singleStep(stepPinSequence)
            time.sleep(delay)

try:
    while True:
        delay = float(input("Enter delay between steps (in milliseconds): ")) / 1000.0
        steps = int(input("How many steps?: "))
        direction = int(input("Enter direction (1 for clockwise, -1 for anticlockwise): "))
        rotateMotor(direction, delay, steps)

except KeyboardInterrupt:
    print("Program terminated by user")

finally:
    GPIO.cleanup()
