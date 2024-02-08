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
    while not ap.isconnected():
        pass
    print('Client connected')
    blink_ap_led()
