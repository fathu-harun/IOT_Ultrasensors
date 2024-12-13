// Define the GPIO pin for the LED
#define LED_PIN 12

void setup() {
  // Set each pin as an output and turn on the LEDs
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  for (int i=0; i < 40; i++){
    digitalWrite(i, HIGH);
  }
}