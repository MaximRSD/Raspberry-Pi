import RPi.GPIO as GPIO
import time

# GPIO pinnen voor de motor
IN1 = 27
IN2 = 17
IN3 = 18
IN4 = 24

# GPIO pinnen voor de knoppen
BUTTON1 = 22
BUTTON2 = 23

GPIO.setmode(GPIO.BCM)

motor_pins = [IN1, IN2, IN3, IN4]
for pin in motor_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

GPIO.setup(BUTTON1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# 8-stap sequentie voor de motor
sequence = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]

def step_motor(seq, delay=0.002):
    for step in seq:
        for pin, val in zip(motor_pins, step):
            GPIO.output(pin, val)
        time.sleep(delay)

def rotate(steps, direction="cw", speed=0.002):
    seq = sequence if direction == "cw" else sequence[::-1]
    for _ in range(steps):
        step_motor(seq, speed)

try:
    print("[START] Motorcontroller actief. Druk op knoppen om te testen.")
    while True:
        btn1 = GPIO.input(BUTTON1)
        btn2 = GPIO.input(BUTTON2)

        if btn1 and not btn2:
            print("[BTN1] Ingedrukt - Draait LINKSOM (5s per rondje)")
            rotate(8, direction="ccw", speed=0.0025)

        elif btn2 and not btn1:
            print("[BTN2] Ingedrukt - Draait RECHTSOM (12s per rondje)")
            rotate(8, direction="cw", speed=0.0055)

        elif btn1 and btn2:
            print("[BEIDE KNOPPEN] Speciaal gedrag: heen - wacht - terug")
            rotate(128, direction="cw", speed=0.0025)
            print("Wacht 2 seconden...")
            time.sleep(2)
            rotate(128, direction="ccw", speed=0.0025)

        else:
            time.sleep(0.05)

except KeyboardInterrupt:
    print("\n[STOP] Programma onderbroken")

finally:
    GPIO.cleanup()
    print("[CLEANUP] GPIO opgeruimd.")
