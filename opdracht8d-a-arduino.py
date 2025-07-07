int led1 = 12;
int led2 = 13;

// GPIO-uitgangen naar Pi (die stuurt ze naar de fysieke LEDs)
int outputPin1 = 2;  // LED1 → Pi GPIO17
int outputPin2 = 3;  // LED2 → Pi GPIO27

void setup() {
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);

  pinMode(outputPin1, OUTPUT);
  pinMode(outputPin2, OUTPUT);

  Serial.begin(9600);
  Serial.println("Start: Arduino knippert LEDs om en om.");
}

void loop() {
  // Stap 1: LED1 aan, LED2 uit
  digitalWrite(led1, HIGH);
  digitalWrite(led2, LOW);

  // Signaal naar Pi (die laat LEDs oplichten)
  digitalWrite(outputPin1, HIGH);
  digitalWrite(outputPin2, LOW);

  Serial.println("LED1 AAN, LED2 UIT");
  delay(1000);

  // Stap 2: LED1 uit, LED2 aan
  digitalWrite(led1, LOW);
  digitalWrite(led2, HIGH);

  digitalWrite(outputPin1, LOW);
  digitalWrite(outputPin2, HIGH);

  Serial.println("LED1 UIT, LED2 AAN");
  delay(1000);
}
