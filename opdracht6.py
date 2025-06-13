import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Pinnen instellen
servo_pin = 27
button1 = 22
button2 = 23

# Zet pin
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Start PWM op 50Hz (voor servo)
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)

# Functie om servo te draaien van start naar eindhoek in gegeven tijd
def draai_servo(start, end, duur):
    stappen = 50
    delay = duur / stappen
    for i in range(stappen + 1):
        hoek = start + (end - start) * (i / stappen)
        duty = 2 + (hoek / 180) * 10
        pwm.ChangeDutyCycle(duty)
        time.sleep(delay)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        # Lees knoppen
        b1 = GPIO.input(button1) == GPIO.HIGH
        b2 = GPIO.input(button2) == GPIO.HIGH

        # Als knop 1 ingedrukt is: servo op 1s heen en terug
        if b1 and not b2:
            draai_servo(0, 120, 1.0)
            draai_servo(120, 0, 1.0)

        # Als knop 2 ingedrukt is: servo op 0.5s heen en terug
        elif b2 and not b1:
            draai_servo(0, 120, 0.5)
            draai_servo(120, 0, 0.5)

        # Als beide knoppen ingedrukt zijn: servo heen in 1s, wacht 2s, terug in 1s
        elif b1 and b2:
            draai_servo(0, 120, 1.0)
            time.sleep(2.0)
            draai_servo(120, 0, 1.0)

        else:
            time.sleep(0.01)

except KeyboardInterrupt:
    pass

# Stop
finally:
    pwm.stop()
    GPIO.cleanup()
