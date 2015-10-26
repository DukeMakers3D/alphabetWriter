const int ledPin = 8;

void setup(){
pinMode(ledPin, OUTPUT);
Serial.begin(9600);
}

void loop(){
Serial.println(Serial.available());
if (Serial.available()) {
  //String readMes = Serial.read();
  
  int blinkNum = Serial.read() - 48;
  if(blinkNum > 0)
  {
    //Serial.print(blinkNum);
    light(blinkNum);
    blinkNum = -1;
  }
  }
delay(500);
}

void light(int n){
for (int i = 0; i < n; i++) {
digitalWrite(ledPin, HIGH);
delay(100);
digitalWrite(ledPin, LOW);
delay(100);
}
}
