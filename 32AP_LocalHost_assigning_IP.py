import network
import machine
import time

# Configure the ESP32 as an Access Point (AP)
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='ESP32-AP', password='123456789')

# Internal LED pin
led_ap = machine.Pin(2, machine.Pin.OUT)

# Function to blink the internal LED
def blink_ap_led():
    led_ap.on()
    time.sleep(1)
    led_ap.off()
    time.sleep(1)

# Main loop
while True:
    while ap.ifconfig()[0] == '0.0.0.0':  # Wait until AP gets an IP address
        pass
    print('AP IP Address:', ap.ifconfig()[0])  # Print AP's IP address
    while not ap.isconnected():
        pass
    print('Client connected')
    blink_ap_led()
