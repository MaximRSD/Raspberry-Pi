#include <IRremote.h>

const int irPin = 12;
IRrecv irrecv(irPin);
decode_results results;

// LED-pinnen
const int ledPins[] = {8, 9, 10, 11};

int selectedLed = -1;             // -1 = standaardmodus
int blinkDelay = 500;             // Snelheid (ms)
unsigned long lastToggle = 0;
bool ledState = false;

void setup() {
  irrecv.enableIRIn();
  Serial.begin(9600);

  for (int i = 0; i < 4; i++) {
    pinMode(ledPins[i], OUTPUT);
    digitalWrite(ledPins[i], LOW);
  }

  Serial.println("Arduino gestart – wacht op IR signaal.");
}

void loop() {
  // 📡 Lees IR-signaal
  if (irrecv.decode(&results)) {
    unsigned long code = results.value;
    Serial.print("IR ontvangen: ");
    Serial.println(code, HEX);

    // === LED-selectie op cijfers 1 t/m 4 ===
    if (code == 0x9716BE3F) {       // knop 1
      selectedLed = 0;
    } else if (code == 0x3D9AE3F7) { // knop 2
      selectedLed = 1;
    } else if (code == 0x6182021B) { // knop 3
      selectedLed = 2;
    } else if (code == 0x8C22657B) { // knop 4
      selectedLed = 3;

    // === Snelheid aanpassen via - en + knoppen ===
    } else if (code == 0xF076C13B) {  // "-" knop → sneller
      blinkDelay = max(100, blinkDelay - 100);
      Serial.print("Sneller → ");
      Serial.println(blinkDelay);
    } else if (code == 0xA3C8EDDB) {  // "+" knop → trager
      blinkDelay = min(2000, blinkDelay + 100);
      Serial.print("Trager → ");
      Serial.println(blinkDelay);

    //Reset naar standaardmodus
    } else if (code == 0xFF38C7) {   // OK knop
      selectedLed = -1;
      Serial.println("Reset naar standaardmodus");
    }

    irrecv.resume(); // Klaar voor volgende signaal
  }

  //Knipperlogica op basis van millis()
  unsigned long currentMillis = millis();
  if (currentMillis - lastToggle >= blinkDelay) {
    lastToggle = currentMillis;
    ledState = !ledState;

    //Reset alle LEDs
    for (int i = 0; i < 4; i++) {
      digitalWrite(ledPins[i], LOW);
    }

    if (selectedLed == -1) {
      //Standaardmodus: LED 0 en 1 knipperen
      digitalWrite(ledPins[0], ledState ? HIGH : LOW);
      digitalWrite(ledPins[1], ledState ? HIGH : LOW);
    } else {
      //Gekozen LED + naastgelegen LED knipperen
      digitalWrite(ledPins[selectedLed], ledState ? HIGH : LOW);
      int secondLed = (selectedLed + 1) % 4;
      digitalWrite(ledPins[secondLed], ledState ? HIGH : LOW);
    }
  }
}
