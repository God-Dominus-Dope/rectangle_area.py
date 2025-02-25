from machine import Pin, ADC
import ujson
import network
import utime as time
import urequests as requests

# Define pins
PIR_PIN = Pin(15, Pin.IN)  # PIR motion sensor pin
LED_PIN = Pin(19, Pin.OUT)  # LED pin
LDR_PIN = ADC(Pin(34))  # Pin untuk LDR (gunakan pin ADC yang sesuai)
DEVICE_ID = "test"  # Ganti dengan DEVICE_ID Anda
WIFI_SSID = "SAMSUNG FRIEND"  # Ganti dengan SSID WiFi Anda
WIFI_PASSWORD = "selaludihat"  # Ganti dengan password WiFi Anda
TOKEN = "BBUS-ZRHsz0tEUxwjgNz7sPS3LizLJpFSxk"  # Ganti dengan token Anda di Ubidots

def send_data(motion_detected, ldr_value):
    url = "http://industrial.api.ubidots.com/api/v1.6/devices/" + DEVICE_ID
    headers = {"Content-Type": "application/json", "X-Auth-Token": TOKEN}
    data = {
        "motion_detected": motion_detected,
        "ldr_value": ldr_value
    }
    response = requests.post(url, json=data, headers=headers)
    print("Response:", response.text)

# Connect to WiFi
wifi_client = network.WLAN(network.STA_IF)
wifi_client.active(True)
print("Connecting device to WiFi")
wifi_client.connect(WIFI_SSID, WIFI_PASSWORD)

while not wifi_client.isconnected():
    print("Connecting...")
    time.sleep(0.1)
print("WiFi Connected!")
print(wifi_client.ifconfig())

while True:
    try:
        # Read PIR sensor value
        motion_detected = PIR_PIN.value()
        
        # Read LDR value
        ldr_value = LDR_PIN.read()  # Baca nilai dari LDR
        
        # Control LED based on motion detection
        LED_PIN.value(motion_detected)  # Turn LED on/off based on motion
        
        # Print the sensor values
        print("Motion Detected: {}".format(motion_detected))
        print("LDR Value: {}".format(ldr_value))
        
        # Send data to Ubidots
        send_data(motion_detected, ldr_value)
        
    except Exception as e:
        print("Error:", e)

    time.sleep(5)  # Delay before the next reading