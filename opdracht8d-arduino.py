const int piOutputPins[] = {2, 3};  // naar GPIO17 en GPIO27
const int buttonInputPin = 4;       // signaal van Raspberry Pi

unsigned long lastTime = 0;
bool ledState = false;

void setup() {
  Serial.begin(9600);

  pinMode(piOutputPins[0], OUTPUT);  // LED1
  pinMode(piOutputPins[1], OUTPUT);  // LED2
  pinMode(buttonInputPin, INPUT);    // signaal van knop (via Pi)

  // Start met beide LEDs uit
  digitalWrite(piOutputPins[0], LOW);
  digitalWrite(piOutputPins[1], LOW);
}

void loop() {
  int buttonState = digitalRead(buttonInputPin);

  if (buttonState == LOW) {
    // Knop is ingedrukt → knipperen
    unsigned long currentTime = millis();
    if (currentTime - lastTime >= 1000) {
      lastTime = currentTime;
      ledState = !ledState;

      digitalWrite(piOutputPins[0], ledState ? HIGH : LOW);
      digitalWrite(piOutputPins[1], ledState ? LOW : HIGH);

      Serial.println("Knipperen...");
    }
  } else {
    // Knop niet ingedrukt → beide uit
    digitalWrite(piOutputPins[0], LOW);
    digitalWrite(piOutputPins[1], LOW);
  }
}
