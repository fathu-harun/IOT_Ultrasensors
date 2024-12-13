import time
from machine import Pin, time_pulse_us

# Set the pin numbers (adjust these to your specific pin connections)
trigPin = Pin(14, Pin.OUT)  # Trigger pin
echoPin = Pin(13, Pin.IN)   # Echo pin
redPin = Pin(12, Pin.OUT)   # Red LED pin
greenPin = Pin(2, Pin.OUT)  # Green LED pin

# Function to get the distance from the ultrasonic sensor
def get_distance():
    # Send a 10ms pulse to trigger the sensor
    trigPin.value(1)  # Set the trigger pin high
    time.sleep_us(10)  # Wait for 10 microseconds
    trigPin.value(0)  # Set the trigger pin low

    # Measure the pulse duration (time taken for echo to return)
    pulse_time = time_pulse_us(echoPin, 1)  # Measure the pulse width in microseconds

    # Calculate distance in centimeters (speed of sound is ~343 m/s)
    distance = pulse_time * 0.0343 / 2  # distance = (time * speed) / 2 (divide by 2 for round trip)
    return distance

# Main program loop
while True:
    distance = get_distance()  # Get the distance from the sensor

    print(f"{distance:.2f} cm")  # Print the distance in centimeters

    if distance <= 10:  # If the object is very close (10 cm or less)
        redPin.value(1)   # Turn on the red LED
        greenPin.value(0)  # Turn off the green LED
    else:
        redPin.value(0)   # Turn off the red LED
        greenPin.value(1)  # Turn on the green LED

    time.sleep(0.05)  # Delay 50ms before the next reading

