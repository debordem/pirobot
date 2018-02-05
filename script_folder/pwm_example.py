#PWM Example from
# https://raspberrypikid.wordpress.com/2014/02/03/pwm-dimming-of-an-led-with-raspberry-pi/

# And a good tutorial here
#https://circuitdigest.com/microcontroller-projects/raspberry-pi-pwm-tutorial

import RPi.GPIO as GPIO
import time

RED = 22

GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom

GPIO.setup(RED, GPIO.OUT) #set pin 21 to output

led = GPIO.PWM(RED,100)       # create object led for PWM on port RED at 100 Hertz

led.start(0)                  # start  led on 0 percent duty cycle (off)

interval = 0.02

try:
    while True:
        for i in range (101):       # 101 because it stops when it finishes 100
            led.ChangeDutyCycle(i)

            time.sleep(interval)         #These last three lines are going to loop and increase the power from 1% to 100% gradually

        for i in range(100,-1,-1):      # from 100 to zero in steps of -1
            led.ChangeDutyCycle(100-i)

            time.sleep(interval)         #These three lines loop and decrease the power from 100%-1% gradually

except KeyboardInterrupt:
    led.stop()
    GPIO.cleanup()
