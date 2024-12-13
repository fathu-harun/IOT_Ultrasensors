


# This file is executed on every boot (including wake-boot from deepsleep)

#import esp

#esp.osdebug(None)

#import webrepl

#webrepl.start()

import network
import time
import urequests
from machine import Pin, time_pulse_us

# Set the pin numbers (adjust these to your specific pin connections)
trigPin = Pin(33, Pin.OUT)  # Trigger pin
echoPin = Pin(32, Pin.IN)   # Echo pin
redPin = Pin(27, Pin.OUT)   # Red LED pin
greenPin = Pin(26, Pin.OUT)  # Green LED pin

# Set the pin numbers (adjust these to your specific pin connections)
trigPin2 = Pin(14, Pin.OUT)  # Trigger pin
echoPin2 = Pin(13, Pin.IN)   # Echo pin
redPin2 = Pin(12, Pin.OUT)   # Red LED pin
greenPin2 = Pin(2, Pin.OUT)  # Green LED pin

def connect_wifi():
  ssid = ""  # Replace with your Wi-Fi SSID
  password = ""  # Replace with your Wi-Fi password
  
  # Create a WLAN object (Wi-Fi interface)
  wlan = network.WLAN(network.STA_IF)  
  wlan.active(True)  # Activate the Wi-Fi interface
  wlan.connect(ssid, password)  # Connect to the Wi-Fi network

  # Wait for connection
  print("Connecting to WiFi...", end="")
  while not wlan.isconnected():
    print(".", end="")  # Wait for the Wi-Fi to connect
    time.sleep(1)  # Wait for the Wi-Fi to connect
  
  print("\nConnected to Wi-Fi")
  print("IP Address:", wlan.ifconfig()[0])  # Print the IP address of the ESP32




def get_distance():
    # Send a 10ms pulse to trigger the sensor
    trigPin.value(1)  # Set the trigger pin high
    trigPin.value(0)  # Set the trigger pin low

    # Measure the pulse duration (time taken for echo to return)
    pulse_time = time_pulse_us(echoPin, 1)  # Measure the pulse width in microseconds

    # Calculate distance in centimeters (speed of sound is ~343 m/s)
    distance = pulse_time * 0.0343 / 2  # distance = (time * speed) / 2 (divide by 2 for round trip)
    return distance


def turn_on_green_light():
  greenPin.value(1)  # Turn on the green LED
  
def turn_off_green_light():
  greenPin.value(0)  # Turn off the green LED

def turn_on_red_light():
  redPin.value(1)  # Turn on the red LED
  
def turn_off_red_light():
  redPin.value(0)  # Turn off the red LED
  
def get_sensor_data():
  distance = get_distance()  # Get the distance from the sensor

  print(f"{distance:.2f} cm")  # Print the distance in centimeters

  if distance <= 10:  # If the object is very close (10 cm or less)
    turn_on_red_light()
    turn_off_green_light()
    data = "occupied"
  else:
    turn_off_red_light()
    turn_on_green_light()
    data = "available"
  
  print(data)
  return data

# Function to get the distance from the ultrasonic sensor
def get_distance2():
    # Send a 10ms pulse to trigger the sensor
    trigPin2.value(1)  # Set the trigger pin high
    trigPin2.value(0)  # Set the trigger pin low

    # Measure the pulse duration (time taken for echo to return)
    pulse_time = time_pulse_us(echoPin2, 1)  # Measure the pulse width in microseconds

    # Calculate distance in centimeters (speed of sound is ~343 m/s)
    distance = pulse_time * 0.0343 / 2  # distance = (time * speed) / 2 (divide by 2 for round trip)
    return distance
    
def turn_on_green_light2():
  greenPin2.value(1)  # Turn on the green LED
  
def turn_off_green_light2():
  greenPin2.value(0)  # Turn off the green LED

def turn_on_red_light2():
  redPin2.value(1)  # Turn on the red LED
  
def turn_off_red_light2():
  redPin2.value(0)  # Turn off the red LED

def get_sensor_data2():

  distance2 = get_distance2()  # Get the distance from the sensor
  print(f"{distance2:.2f} cm")  # Print the distance in centimeters

  if distance2 <= 10:  # If the object is very close (10 cm or less)
    turn_on_red_light2()
    turn_off_green_light2()
    data = "occupied"
  else:
    turn_off_red_light2()
    turn_on_green_light2()
    data = "available"
  
  print(data)
  return data

def send_data(data, data2):
  # ThingsBoard REST API endpoint and device token
  THINGSBOARD_URL = "http://tb.relentlessadmin.org:8080/api/v1/"  # Replace with your ThingsBoard server if self-hosted
  DEVICE_TOKEN = ""                      # Replace with your device token
  URL = THINGSBOARD_URL + DEVICE_TOKEN + "/telemetry"
  try:
    payload = {3:data, 4:data2}
    response = urequests.post(URL, json=payload)
    print("Data sent:", payload)
    print("Response:", response.status_code, response.text)
    response.close()
  except Exception as e:
    print("Failed to send data:", e)

connect_wifi()

while True:
    try:
        data = get_sensor_data()
        time.sleep(0.1)  # Prevent interference
        data2 = get_sensor_data2()
        send_data(data, data2)
        time.sleep(1)
    except Exception as e:
        print("Error:", e)






