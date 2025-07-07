import RPi.GPIO as GPIO
import time

buttonPin = 24          # Knop
outputToArduino = 4     # Stuur knopstatus naar Arduino pin 4
leds = [22, 23]         # LEDs op de Pi
fromArduino = [17, 27]  # Signaal van Arduino (pin 2 en 3)

GPIO.setmode(GPIO.BCM)

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(outputToArduino, GPIO.OUT)

GPIO.setup(fromArduino[0], GPIO.IN)
GPIO.setup(fromArduino[1], GPIO.IN)
GPIO.setup(leds[0], GPIO.OUT)
GPIO.setup(leds[1], GPIO.OUT)

try:
    while True:
        # Lees knopstatus en stuur die naar Arduino
        btn_state = GPIO.input(buttonPin)
        GPIO.output(outputToArduino, btn_state)

        # Lees Arduino signalen en stuur naar LEDs
        GPIO.output(leds[0], GPIO.input(fromArduino[0]))
        GPIO.output(leds[1], GPIO.input(fromArduino[1]))

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO opgeruimd")
