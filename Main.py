import network
import time

# Wi-Fi credentials
SSID = "607 University Ave"
PASSWORD = "Bluetruck629"

# Create Wi-Fi interface and turn it on
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

print("Connecting to Wi-Fi...")

# Try to connect if not already connected
if not wlan.isconnected():
    wlan.connect(SSID, PASSWORD)

    # Wait until connection is successful
    while not wlan.isconnected():
        time.sleep(1)
        print("Connecting...")

# Check result
if wlan.isconnected():
    print("Connected successfully")
    print("IP address:", wlan.ifconfig()[0])  # device network address
else:
    print("Connection failed")

print("Done")

import time
import machine
import ubinascii
from umqtt.robust import MQTTClient

# Device/user name
NAME = "trevor"

# MQTT broker address
MQTT_BROKER = "broker.hivemq.com"

# Topics for receiving commands and sending status updates
COMMAND_TOPIC = f"wyohack/{NAME}/led/command"
STATUS_TOPIC  = f"wyohack/{NAME}/led/status"