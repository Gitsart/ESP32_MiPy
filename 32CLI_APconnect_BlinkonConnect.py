import network
import machine
import time

# Configure the ESP32 as a Station (Client)
station = network.WLAN(network.STA_IF)
station.active(True)

# Client LED pin
led_client = machine.Pin(2, machine.Pin.OUT)  # Assuming pin 2, change as needed

# Function to connect to the AP and handle LED
def connect_to_ap():
    station.connect('ESP32-AP', '123456789')  # Connect to the AP
    while not station.isconnected():
        pass
    led_client.on()
    print('Connected to AP')

# Function to handle disconnection and LED
def disconnect_from_ap():
    led_client.off()
    print('Disconnected from AP')
    station.disconnect()

# Connect to AP on startup
connect_to_ap()

# Monitor the connection status
while True:
    while station.isconnected():
        pass
    disconnect_from_ap()
