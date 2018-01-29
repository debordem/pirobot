import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom

GPIO.setup(17, GPIO.OUT)  # set up pin 17
GPIO.setup(18, GPIO.OUT)  # set up pin 18

RED = 17
GREEN = 18

def flash(pin,sec):
    time.sleep(sec)
    GPIO.output(pin, 1)  # turn on pin 17
    time.sleep(sec)
    GPIO.output(pin, 0)  # turn on pin 17

for x in range(0, 3):
    print ("We're on time %d" % (x))
    flash(RED,0.5)
    flash(GREEN,0.5)
    #GPIO.output(17, 1)  # turn on pin 17
    #GPIO.output(18, 0)  # turn on pin 18
