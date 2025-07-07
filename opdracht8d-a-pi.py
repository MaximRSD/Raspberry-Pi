import RPi.GPIO as GPIO

btnPin = 6
leds = [22, 23]
# 3 input, 4 output
ardPins = [17, 27]

GPIO.setmode(GPIO.BCM)

GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(leds[0], GPIO.OUT)
GPIO.setup(leds[1], GPIO.OUT)
GPIO.setup(ardPins[0], GPIO.IN)
GPIO.setup(ardPins[1], GPIO.OUT)

while True:
    GPIO.output(ardPins[1], GPIO.input(btnPin))

    if GPIO.input(ardPins[0]) == GPIO.HIGH:
        GPIO.output(leds[0], GPIO.HIGH)
        GPIO.output(leds[1], GPIO.LOW)
    else:
        GPIO.output(leds[1], GPIO.HIGH)
        GPIO.output(leds[0], GPIO.LOW)
