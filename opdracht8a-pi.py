import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
SIGNAL_PIN = 17  # GPIO17, stuurt HIGH/LOW signaal naar Arduino

GPIO.setup(SIGNAL_PIN, GPIO.OUT)

try:
    while True:
        print("Signaal NAAR ARDUINO: AAN")
        GPIO.output(SIGNAL_PIN, GPIO.HIGH)
        time.sleep(1)
        print("Signaal NAAR ARDUINO: UIT")
        GPIO.output(SIGNAL_PIN, GPIO.LOW)
        time.sleep(1)

except KeyboardInterrupt:a
    GPIO.cleanup()
    print("GPIO opgeruimd")
