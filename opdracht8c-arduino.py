int led1 = 12;
int led2 = 13;
int inputPin1 = 2;     // GPIO17 Pi → LED1
int inputPin2 = 3;     // GPIO27 Pi → LED2

int buttonPin = 4;     // Knop op Arduino
int outputPin3 = 5;    // Knopstatus naar Pi (bijv. GPIO22)

void setup() {
  pinMode(inputPin1, INPUT);
  pinMode(inputPin2, INPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);

  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(outputPin3, OUTPUT);

  Serial.begin(9600);
  Serial.println("Start: Arduino is signaal-doorgever.");
}

void loop() {
  // Geef GPIO-signalen van Pi door naar de LEDs
  digitalWrite(led1, digitalRead(inputPin1));
  digitalWrite(led2, digitalRead(inputPin2));

  // Lees knopstatus en stuur die naar de Pi
  int buttonState = digitalRead(buttonPin);
  digitalWrite(outputPin3, buttonState);

  // Debug (optioneel)
  if (buttonState == LOW) {
    Serial.println("Knop is INGEDRUKT");
  } else {
    Serial.println("Knop is NIET ingedrukt");
  }

  delay(100);
}
