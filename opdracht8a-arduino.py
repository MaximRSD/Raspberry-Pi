int inputPin = 2;    // Van Raspberry Pi
int led1 = 12;
int led2 = 13;

void setup() {
  pinMode(inputPin, INPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
}

void loop() {
  int signal = digitalRead(inputPin);

  if (signal == HIGH) {
    digitalWrite(led1, HIGH);
    digitalWrite(led2, LOW);
    delay(500);
    digitalWrite(led1, LOW);
    digitalWrite(led2, HIGH);
    delay(500);
  } else {
    // Zet beide LED’s uit als Pi geen signaal geeft
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
  }
}
