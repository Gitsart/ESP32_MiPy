import machine
import network
import usocket as socket
import time
import esp

esp.osdebug(None)

led = machine.Pin(2,machine.Pin.OUT)

ip_address = '192.168.1.111'
subnet_mask = '255.255.255.0'
gateway = '192.168.1.1'
dns = '8.8.8.8'

espA_address = ('192.168.1.155', 1234)

station = network.WLAN(network.STA_IF)
station.active(True)
station.ifconfig((ip_address, subnet_mask, gateway, dns))
station.connect('Anode', 'anode@123')
print(station.ifconfig()[0])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(espA_address)

def blink_led():
    for _ in range(5):
        led.value(1)
        time.sleep(0.1)
        led.value(0)
        time.sleep(0.1)

def receive_data_from_espA():
    data, addr = sock.recvfrom(1024)
    return data.decode('utf-8')

while True:
    data_from_espA = receive_data_from_espA()
    if data_from_espA:
        priint(f"Received data: {data_from_espA}")
        blink_led()
