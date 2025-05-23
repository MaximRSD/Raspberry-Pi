import RPi.GPIO as GPIO
import time

# Zet de GPIO-modus op BCM (Broadcom-chip pin-nummering)
GPIO.setmode(GPIO.BCM)

# Stel GPIO-pinnen 17 en 27 in als uitgang
led1 = 17
led2 = 27
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)

try:
    # a. Beide LEDs tegelijk knipperen, 1 seconde aan, 1 seconde uit
    for i in range(5):
        GPIO.output(led1, GPIO.HIGH)
        GPIO.output(led2, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led1, GPIO.LOW)
        GPIO.output(led2, GPIO.LOW)
        time.sleep(1)

    # b. LEDs om en om laten knipperen
    for i in range(5):
        GPIO.output(led1, GPIO.HIGH)
        GPIO.output(led2, GPIO.LOW)
        time.sleep(1)
        GPIO.output(led1, GPIO.LOW)
        GPIO.output(led2, GPIO.HIGH)
        time.sleep(1)

    # c. LED 1 en LED 2 met verschillende tijden laten knipperen
    for i in range(5):
        GPIO.output(led1, GPIO.HIGH)
        time.sleep(1.3)
        GPIO.output(led1, GPIO.LOW)
        time.sleep(0.7)

        GPIO.output(led2, GPIO.HIGH)
        time.sleep(0.8)
        GPIO.output(led2, GPIO.LOW)
        time.sleep(1.7)

finally:
    # Ruim de GPIO-pinnen op na gebruik
    GPIO.cleanup()
