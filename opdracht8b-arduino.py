int inputPin1 = 2;  // Van Pi: LED1
int inputPin2 = 4;  // Van Pi: LED2
int led1 = 12;
int led2 = 13;

void setup() {
  pinMode(inputPin1, INPUT);
  pinMode(inputPin2, INPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
}

void loop() {
  digitalWrite(led1, digitalRead(inputPin1));
  digitalWrite(led2, digitalRead(inputPin2));
}
