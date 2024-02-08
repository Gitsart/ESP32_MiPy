import machine
import time

uart = machine.UART(2, baudrate=9600, tx=17, rx=16)
button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
led = machine.Pin(2, machine.Pin.OUT, value=0)

def send_data(data):
    uart.write(data)
def blink():
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)

while True:
    if button.value() == 0:
        send_data("Button pressed! Hello from ESP32...\n")
        time.sleep(2)

    if uart.any():
        try:
            received_data = uart.readline()
            decoded_data = received_data.decode("utf-8")
            print("Received Data from Arduino:", decoded_data)
            blink()
            blink()
        except UnicodeError:
            print("Error decoding data from Arduino:", received_data)
            print("Data as bytes:", received_data)
            blink()
            blink()
            
