/*
  SparkFun Inventor’s Kit
  Circuit 3B-Distance Sensor

  Control the color of an RGB LED using an ultrasonic distance sensor.

  This sketch was written by SparkFun Electronics, with lots of help from the Arduino community.
  This code is completely free for any use.

  View circuit diagram and instructions at: https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40
  Download drawings and code at: https://github.com/sparkfun/SIK-Guide-Code
*/

//Set 1
const int trigPin = 14;           //connects to the trigger pin on the distance sensor
const int echoPin = 13;           //connencts to the echo pin on the distance sensor
const int redPin = 12;             //pin to control the red LED inside the RGB LED
const int greenPin = 2;             //pin to control the red LED inside the RGB LED

// //Set 2
// const int trigPin = 25;           //connects to the trigger pin on the distance sensor
// const int echoPin = 19;           //connencts to the echo pin on the distance sensor
// const int redPin = 18;             //pin to control the red LED inside the RGB LED
// const int greenPin = 15;             //pin to control the red LED inside the RGB LED

// //Set 3
// const int trigPin = 33;           //connects to the trigger pin on the distance sensor
// const int echoPin = 32;           //connencts to the echo pin on the distance sensor
// const int redPin = 27;             //pin to control the red LED inside the RGB LED
// const int greenPin = 26;             //pin to control the red LED inside the RGB LED

// //Set fail
// const int trigPin = 39;           //connects to the trigger pin on the distance sensor
// const int echoPin = 36;           //connencts to the echo pin on the distance sensor
// const int redPin = 35;             //pin to control the red LED inside the RGB LED
// const int greenPin = 34;             //pin to control the red LED inside the RGB LED

// //Set 4
// const int trigPin = 23;           //connects to the trigger pin on the distance sensor
// const int echoPin = 22;           //connencts to the echo pin on the distance sensor
// const int redPin = 21;             //pin to control the red LED inside the RGB LED
// const int greenPin = 1;             //pin to control the red LED inside the RGB LED

// //Set fail
// const int trigPin = 17;           //connects to the trigger pin on the distance sensor
// const int echoPin = 16;           //connencts to the echo pin on the distance sensor
// const int redPin = 5;             //pin to control the red LED inside the RGB LED
// const int greenPin = 4;             //pin to control the red LED inside the RGB LED

float distance = 0;               //stores the distance measured by the distance sensor

void setup()
{
  // Serial.begin (9600);        //set up a serial connection with the computer
  pinMode(trigPin, OUTPUT);   //the trigger pin will output pulses of electricity
  pinMode(echoPin, INPUT);    //the echo pin will measure the duration of pulses coming back from the distance sensor

  //set the RGB LED pins to output
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
}

void loop() {
  distance = getDistance();   //variable to store the distance measured by the sensor

  Serial.print(distance);     //print the distance that was measured
  Serial.println(" in");      //print units after the distance

  if (distance <= 0.1) {       //if the object is close, hence, it is taken

    //make the RGB LED red
    digitalWrite(redPin, HIGH);
    digitalWrite(greenPin, LOW);
  }

  else {
    digitalWrite(redPin, LOW);
    digitalWrite(greenPin, HIGH);
  }

  delay(50);      //delay 50ms between each reading
}

//------------------FUNCTIONS-------------------------------

//RETURNS THE DISTANCE MEASURED BY THE HC-SR04 DISTANCE SENSOR
float getDistance()
{
  float echoTime;                   //variable to store the time it takes for a ping to bounce off an object
  float calculatedDistance;         //variable to store the distance calculated from the echo time

  //send out an ultrasonic pulse that's 10ms long
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  echoTime = pulseIn(echoPin, HIGH);      //use the pulsein command to see how long it takes for the
                                          //pulse to bounce back to the sensor

  calculatedDistance = echoTime / 1000 / 1000 * 148.0 ;  //calculate the distance of the object that reflected the pulse (half the bounce time multiplied by the speed of sound)

  return calculatedDistance;              //send back the distance that was calculated
}
