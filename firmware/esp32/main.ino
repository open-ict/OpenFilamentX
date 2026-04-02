#include <Arduino.h>

float temperatureC = 210.0;
float filamentDiameter = 1.75;
float extrusionSpeed = 8.0;

void setup() {
  Serial.begin(115200);
}

void loop() {
  // Replace this section with real sensor reads.
  Serial.print("temperature=");
  Serial.print(temperatureC);
  Serial.print(",diameter=");
  Serial.print(filamentDiameter);
  Serial.print(",speed=");
  Serial.println(extrusionSpeed);
  delay(1000);
}
