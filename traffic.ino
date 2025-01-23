const int greenLED = 7;
const int redLED = 12;

void setup() {
  pinMode(greenLED, OUTPUT);
  pinMode(redLED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char signal = Serial.read();  // Read the signal from Python

    if (signal == 'G') {
      digitalWrite(greenLED, HIGH);
      digitalWrite(redLED, LOW);
    } else if (signal == 'R') {
      digitalWrite(greenLED, LOW);
      digitalWrite(redLED, HIGH);
    }
  }
}
