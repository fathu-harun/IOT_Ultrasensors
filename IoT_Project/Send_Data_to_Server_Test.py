import network
import time
import urequests
from machine import Pin, time_pulse_us

def connect_wifi():
    ssid = ""  # Replace with your Wi-Fi SSID
    password = ""  # Replace with your Wi-Fi password
    
    # Create a WLAN object (Wi-Fi interface)
    wlan = network.WLAN(network.STA_IF)  
    wlan.active(True)  # Activate the Wi-Fi interface
    wlan.connect(ssid, password)  # Connect to the Wi-Fi network

    # Wait for connection
    print("Connecting to Wi-Fi...")
    while not wlan.isconnected():
      time.sleep(1)  # Wait for the Wi-Fi to connect
    
    print("Connected to Wi-Fi")
    print("IP Address:", wlan.ifconfig()[0])  # Print the IP address of the ESP32
 
def make_get_request(url_get):
  response = urequests.get(url)  # Send a GET request
  print("Response status code:", response.status_code)  # Print status code
  response.close()  # Close the response to free up resources

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
    data = True
  else:
    turn_off_red_light()
    turn_on_green_light()
    data = False
  
  print(data)
  return data
  
def send_data(data, url):
  data = {
    "arduino_ip": "192.168.1.10",
    "slot_id": 1,
    "occupied": data
  }
  try:
    response = urequests.post(url, json=data)
    print("Response status code:", response.status_code)  # Print status code

    if response.status_code == 200:
      print("Data sent successfully!")
    else:
      print("Failed to send data:", response.status_code)
    response.close()
  except Exception as e:
    print("Error sending data:", e)



















# main() starts here

print("Connecting to hotspot...")
time.sleep(1)

connect_wifi()
time.sleep(1)

#print("Now trying to connect to server...")
#url_get = "https://iot-group-9-backend.onrender.com/api/test/db_state"
#make_get_request(url_get)
print("Entering loop...")
time.sleep(1)

while True:
  print("Running the ultrasensors...")
  time.sleep(5)

  distance = get_distance()  # Get the distance from the sensor
  
  print(f"{distance:.2f} cm")  # Print the distance in centimeters
  
  if distance <= 10:  # If the object is very close (10 cm or less)
    turn_on_red_light()
    turn_off_green_light()
    data = True
  else:
    turn_off_red_light()
    turn_on_green_light()
    data = False
  
  print("Now sending data over...")
    
  url_post = "https://iot-group-9-backend.onrender.com/api/sensor/data/receive"
    
  send_data(data, url_post)
