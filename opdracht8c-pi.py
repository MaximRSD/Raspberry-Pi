import RPi.GPIO as GPIO
import time

LED1 = 17
LED2 = 27
BUTTON = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN)

# Starttoestand: alleen LED1 aan
led1_on = True
GPIO.output(LED1, GPIO.HIGH)
GPIO.output(LED2, GPIO.LOW)

# Voor edge-detectie
last_button_state = GPIO.input(BUTTON)
debounce_time = 0.05  # 50 ms

try:
    while True:
        current_state = GPIO.input(BUTTON)

        # Detecteer overgang van HIGH naar LOW (druk)
        if last_button_state == GPIO.HIGH and current_state == GPIO.LOW:
            # Toggle toestand
            led1_on = not led1_on

            GPIO.output(LED1, GPIO.HIGH if led1_on else GPIO.LOW)
            GPIO.output(LED2, GPIO.LOW if led1_on else GPIO.HIGH)

            print("Druk gedetecteerd → LEDs gewisseld")
            time.sleep(debounce_time)  # debounce

        last_button_state = current_state
        time.sleep(0.01)  # poll-snelheid

except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO opgeruimd, programma gestopt")
