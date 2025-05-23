import RPi.GPIO as GPIO
import time

# Zet GPIO-modus en maak pin 17 klaar voor gebruik als output (LED)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

try:
    # a) LED knippert 5 keer: 1 seconde aan, 1 seconde uit
    print("a) 1 seconde aan / 1 seconde uit")
    for i in range(5):
        GPIO.output(17, True)
        time.sleep(1)
        GPIO.output(17, False)
        time.sleep(1)

    # b) LED knippert 5 keer: 1 seconde aan, 2 seconden uit
    print("b) 1 seconde aan / 2 seconden uit")
    for i in range(5):
        GPIO.output(17, True)
        time.sleep(1)
        GPIO.output(17, False)
        time.sleep(2)

    # c) LED knippert snel 20 keer: 0.1 seconde aan en uit
    print("c) 0.1 seconde aan / 0.1 seconde uit")
    for i in range(20):
        GPIO.output(17, True)
        time.sleep(0.1)
        GPIO.output(17, False)
        time.sleep(0.1)

    # d) LED knippert heel snel 20 keer: 0.005 seconde aan en uit
    print("d) snel knipperen: 0.005 seconde aan/uit")
    for i in range(20):
        GPIO.output(17, True)
        time.sleep(0.005)
        GPIO.output(17, False)
        time.sleep(0.005)

finally:
    # Zorgt ervoor dat de GPIO-pinnen netjes worden opgeruimd na afloop
    GPIO.cleanup()
    print("Klaar, pinnen opgeruimd!")
