
int sensor = A0; 
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); 
  pinMode(sensor, INPUT); 
}

void loop() {
  int data = analogRead(sensor); 
  // put your main code here, to run repeatedly:
  Serial.println(data); 
}
