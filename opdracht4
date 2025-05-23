import RPi.GPIO as GPIO
import time

# Zet GPIO-modus op BCM
GPIO.setmode(GPIO.BCM)

# Pin
led1 = 17
led2 = 27
button = 22

# Zet pinnen als uitgang
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        if GPIO.input(button) == GPIO.HIGH:
            #4c
            GPIO.output(led2, GPIO.LOW)
            GPIO.output(led1, GPIO.HIGH)
            time.sleep(1.3)
            GPIO.output(led1, GPIO.LOW)
            time.sleep(0.7)
        else:
            # LED2 aan als knop NIET wordt ingedrukt
            GPIO.output(led1, GPIO.LOW)
            GPIO.output(led2, GPIO.HIGH)
            time.sleep(0.1)

finally:
    GPIO.cleanup()
