from machine import Pin, ADC, I2C
import ujson
import network
import utime as time
import urequests as requests
import DHT  # Example to read temperature and humidity

# Define pins
PIR_PIN = Pin(15, Pin.IN)  # PIR motion sensor pin
LED_PIN = Pin(19, Pin.OUT)  # LED pin
LDR_PIN = ADC(Pin(34))  # Pin for LDR
DHT_PIN = Pin(25)  # Pin for DHT sensor
DEVICE_ID = "test"  # Device ID
WIFI_SSID = "SAMSUNG FRIEND"  # WiFi SSID
WIFI_PASSWORD = "selaludihat"  # WiFi password
TOKEN = "YOUR_UBIDOTS_TOKEN"  # Ubidots token

# Instantiate DHT22 sensor
dht_sensor = DHT.DHT22(DHT_PIN)

def send_data(motion_detected, ldr_value, temperature, humidity):
    url = f"http://industrial.api.ubidots.com/api/v1.6/devices/{DEVICE_ID}"
    headers = {"Content-Type": "application/json", "X-Auth-Token": TOKEN}
    data = {
        "motion_detected": motion_detected,
        "ldr_value": ldr_value,
        "temperature": temperature,
        "humidity": humidity
    }
    response = requests.post(url, json=data, headers=headers)
    print("Response:", response.text)

# Connect to WiFi
wifi_client = network.WLAN(network.STA_IF)
wifi_client.active(True)
wifi_client.connect(WIFI_SSID, WIFI_PASSWORD)

while not wifi_client.isconnected():
    print("Connecting...")
    time.sleep(0.1)
print("WiFi Connected!")
print(wifi_client.ifconfig())

while True:
    try:
        # Read PIR sensor
        motion_detected = PIR_PIN.value()
        
        # Read LDR value
        ldr_value = LDR_PIN.read()
        
        # Read temperature and humidity values
        dht_sensor.measure()
        temperature = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
        
        # Control LED based on motion detection
        LED_PIN.value(motion_detected)  
        
        # Print sensor values
        print(f"Motion Detected: {motion_detected}")
        print(f"LDR Value: {ldr_value}")
        print(f"Temperature: {temperature}, Humidity: {humidity}")
        
        # Send data to Ubidots
        send_data(motion_detected, ldr_value, temperature, humidity)
        
    except Exception as e:
        print("Error:", e)

    time.sleep(5)  # Delay before the next reading