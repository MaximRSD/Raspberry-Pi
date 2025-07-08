#include <IRremote.h>

const int irPin = 12;
IRrecv irrecv(irPin);
decode_results results;

// LED select pinnen (naar Pi): 8–11
const int ledPins[] = {8, 9, 10, 11};

// Snelheid bits (naar Pi): 2 = LSB, 3 = MSB
const int speedPins[] = {2, 3};

int selectedLed = -1;      // -1 = standaardmodus
int speedLevel = 2;        // 0 (snel) tot 3 (traag)

void setup() {
  Serial.begin(9600);
  irrecv.enableIRIn();

  // Output pinnen voor LED selectie
  for (int i = 0; i < 4; i++) {
    pinMode(ledPins[i], OUTPUT);
    digitalWrite(ledPins[i], LOW);
  }

  // Output pinnen voor snelheid bits
  for (int i = 0; i < 2; i++) {
    pinMode(speedPins[i], OUTPUT);
    digitalWrite(speedPins[i], LOW);
  }

  Serial.println("Arduino gestart – wacht op IR signaal.");
}

void updateOutputs() {
  for (int i = 0; i < 4; i++) {
    // Zet HIGH als i == selectedLed OF i == volgende LED (met wrap-around)
    bool isSecondLed = (selectedLed != -1) && (i == (selectedLed) % 4);
    bool isSelectedLed = (i == selectedLed);
    bool isDefault = (selectedLed == -1); // alle LEDs aan in default

    digitalWrite(ledPins[i], (isSelectedLed || isSecondLed || isDefault) ? HIGH : LOW);
  }

  // Snelheid bits
  digitalWrite(speedPins[0], bitRead(speedLevel, 0)); // LSB
  digitalWrite(speedPins[1], bitRead(speedLevel, 1)); // MSB
}


void loop() {
  if (irrecv.decode(&results)) {
    unsigned long code = results.value;
    Serial.print("Ontvangen code: ");
    Serial.println(code, HEX);

    switch (code) {
      case 0x9716BE3F: selectedLed = 0; Serial.println("LED 1 geselecteerd"); break;
      case 0x3D9AE3F7: selectedLed = 1; Serial.println("LED 2 geselecteerd"); break;
      case 0x6182021B: selectedLed = 2; Serial.println("LED 3 geselecteerd"); break;
      case 0x8C22657B: selectedLed = 3; Serial.println("LED 4 geselecteerd"); break;

      case 0xF076C13B:  // "-" knop
        speedLevel = max(0, speedLevel - 1);
        Serial.print("Sneller → Niveau: ");
        Serial.println(speedLevel);
        break;

      case 0xA3C8EDDB:  // "+" knop
        speedLevel = min(3, speedLevel + 1);
        Serial.print("Trager → Niveau: ");
        Serial.println(speedLevel);
        break;
    }

    updateOutputs(); // Zet outputs voor Pi
    irrecv.resume();
  }
}
