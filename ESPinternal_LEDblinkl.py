import machine
import time
led_pin = 2
led = machine.Pin(led_pin, machine.Pin.OUT)

while True:
    led.value(1)
    time.sleep(.5)
    led.value(0)
    time.sleep(.5)
    
