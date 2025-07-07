import RPi.GPIO as GPIO
import time

LED1_PIN = 17  # 3 sec cyclus
LED2_PIN = 27  # 1 sec cyclus

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1_PIN, GPIO.OUT)
GPIO.setup(LED2_PIN, GPIO.OUT)

def toggle_led(state, pin):
    GPIO.output(pin, state)
    status = "ON" if state else "OFF"
    print(f"[{time.strftime('%H:%M:%S')}] LED on pin {pin} {status}")

try:
    led1_on = False
    led2_on = False
    counter = 0

    while True:
        # Elke 0.5 seconden
        if counter % 3 == 0:  # om de 1.5s → toggle LED1
            led1_on = not led1_on
            toggle_led(led1_on, LED1_PIN)

        # altijd toggle LED2 (elke 0.5s)
        led2_on = not led2_on
        toggle_led(led2_on, LED2_PIN)

        counter += 1
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO opgeruimd")
