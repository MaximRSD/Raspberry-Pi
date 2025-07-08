import RPi.GPIO as GPIO
import time

# GPIO ingangen van Arduino (LED selectie + snelheid)
led_select_pins = [17, 27, 22, 23]  # van Arduino pin 8–11
speed_pins = [20, 21]               # van Arduino pin 2 en 3 (LSB, MSB)

# GPIO pinnen van de LEDs op de Pi
led_pins = [5, 6, 13, 19]

GPIO.setmode(GPIO.BCM)

# Setup input pinnen
for pin in led_select_pins + speed_pins:
    GPIO.setup(pin, GPIO.IN)

# Setup output LEDs
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

print("Raspberry Pi gestart – wacht op selectie + snelheid...")

# Snelheidsopties (index = binaire waarde van speed_pins)
speed_table = [0.2, 0.4, 0.7, 1.0]  # in seconden (pas aan naar wens)

blink_state = False
last_toggle = time.time()
blink_delay = speed_table[2]  # default: medium

try:
    while True:
        # 1. Bepaal geselecteerde LED via led_select_pins
        selected_led = -1
        for i, pin in enumerate(led_select_pins):
            if GPIO.input(pin) == GPIO.HIGH:
                selected_led = i
                break

        # 2. Bepaal snelheid via speed_pins
        lsb = GPIO.input(speed_pins[0])
        msb = GPIO.input(speed_pins[1])
        speed_index = (msb << 1) | lsb  # 0–3
        blink_delay = speed_table[speed_index]

        # 3. Knipperlogica
        now = time.time()
        if now - last_toggle >= blink_delay:
            last_toggle = now
            blink_state = not blink_state

            # Reset alle LEDs
            for pin in led_pins:
                GPIO.output(pin, GPIO.LOW)

            if selected_led == -1:
                # Standaardmodus: LED 0 & 1 knipperen
                GPIO.output(led_pins[0], GPIO.HIGH if blink_state else GPIO.LOW)
                GPIO.output(led_pins[1], GPIO.HIGH if blink_state else GPIO.LOW)
            else:
                # Geselecteerde LED + volgende
                GPIO.output(led_pins[selected_led], GPIO.HIGH if blink_state else GPIO.LOW)
                second_led = (selected_led + 1) % 4
                GPIO.output(led_pins[second_led], GPIO.HIGH if blink_state else GPIO.LOW)

        time.sleep(0.01)

except KeyboardInterrupt:
    print("Afsluiten...")
    GPIO.cleanup()
