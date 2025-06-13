import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Pin
led1 = 17
led2 = 27
button1 = 22
button2 = 23

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

led1_aan = False
led2_aan = False
tijd_led1 = time.time()
tijd_led2 = time.time()

try:
    while True:
        nu = time.time()
        knop1 = GPIO.input(button1) == GPIO.HIGH
        knop2 = GPIO.input(button2) == GPIO.HIGH

        if knop1:
            # LED1 knippert (1s/1s), LED2 blijft UIT
            if nu - tijd_led1 > 1.0:
                led1_aan = not led1_aan
                tijd_led1 = nu
                GPIO.output(led1, led1_aan)
            GPIO.output(led2, False)

        elif knop2:
            # LED2 knippert (0.7s/0.7s), LED1 blijft UIT
            if nu - tijd_led2 > 0.7:
                led2_aan = not led2_aan
                tijd_led2 = nu
                GPIO.output(led2, led2_aan)
            GPIO.output(led1, False)

        else:
            # Geen knoppen: LED1 knippert met 1.3s/0.7s
            interval1 = 1.3 if led1_aan else 0.7
            if nu - tijd_led1 > interval1:
                led1_aan = not led1_aan
                tijd_led1 = nu
                GPIO.output(led1, led1_aan)
                GPIO.output(led2, not led1_aan)

        time.sleep(0.01)

finally:
    GPIO.cleanup()
