import network
import machine
import time

led = machine.Pin(2, machine.Pin.OUT)

def blink():
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect('Vaishak M', '03101997')

while sta.isconnected() == True:
    print("Connected to Network")
    blink()
    
