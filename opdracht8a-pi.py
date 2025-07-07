import RPi.GPIO as GPIO
import time

LED1 = 17  # Naar Arduino inputPin1
LED2 = 27  # Naar Arduino inputPin2

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)

try:
    while True:
        print("LED1 aan, LED2 uit")
        GPIO.output(LED1, GPIO.HIGH)
        GPIO.output(LED2, GPIO.LOW)
        time.sleep(1)

        print("LED1 uit, LED2 aan")
        GPIO.output(LED1, GPIO.LOW)
        GPIO.output(LED2, GPIO.HIGH)
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO opgeruimd, programma gestopt")
