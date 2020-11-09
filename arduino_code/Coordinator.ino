String message = "";

void setup() {
  Serial.begin(9600);
  Serial.println("Program Started");
}

void loop() {

  while(Serial.available()){
    message = Serial.readString();
    Serial.print(message);
    delay(100);
    message = "";
  }
}
