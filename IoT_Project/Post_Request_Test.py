import network
import time
import urequests

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

def make_post_request():
    url = "https://iot-group-9-backend.onrender.com/api/sensor/data/receive"  # Example URL
    data = {
      "arduino_ip": "192.168.1.10",
      "slot_id": 1,
      "occupied": True
    }
 
    response = urequests.post(url, json=data)  # Send a GET request
    
    print("Response status code:", response.status_code)  # Print status code
    print("Response text:", response.text)  # Print the response content
    
    response.close()  # Close the response to free up resources

# Call the function to connect to Wi-Fi
connect_wifi()
time.sleep(1)

print("Now trying to connect to server...")
time.sleep(1)

# Make the GET request
make_post_request()


