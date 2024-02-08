import machine
import network
import time

led_pin = 2

led = machine.Pin(led_pin, machine.Pin.OUT)

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect('ESP32Server' , '12345678')

while not sta.isconnected():
    pass

print("connected to server")

while True:
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)
    