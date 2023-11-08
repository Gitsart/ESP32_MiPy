import machine
import network

led_pin = 2
led = machine.Pin(led_pin, machine.Pin.OUT)

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='ESP32Server', password='12345678')

while not ap.isconnected():
    pass
print('Server IP Address:', ap.ifconfig()[0])

led.value(1)

while True:
    pass

