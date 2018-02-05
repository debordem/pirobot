# Let's import the modules we will need!
import RPi.GPIO as GPIO
import time

AIA = 25
AIB = 8

# Next we setup the pins for use!
GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom
GPIO.setwarnings(False) # Warnings to false to stop noise

GPIO.setup(AIA, GPIO.OUT)  # pin 25 connected to pin A-IA
GPIO.setup(AIB, GPIO.OUT)  # pin 8 connected to pin A-IB

print('Starting motor sequence!')

while True:
  try:
    # Makes the motor spin one way for 3 seconds
    GPIO.output(AIA, True)
    GPIO.output(AIB, False)
    time.sleep(3)
    # Spins the other way for a further 3 seconds
    GPIO.output(AIA, False)
    GPIO.output(AIB, True)
    time.sleep(3)
  except(KeyboardInterrupt):
    # If a keyboard interrupt is detected then it exits cleanly!
    print('Finishing up!')
    GPIO.output(AIA, False)
    GPIO.output(AIB, False)
    quit()
