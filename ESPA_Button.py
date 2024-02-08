import machine
import network
import usocket as socket
import time
import esp

esp.osdebug(None)

button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

ip_address = '192.168.1.155'
subnet_mask = '255.255.255.0'
gateway = '192.168.1.1'
dns = '8.8.8.8'

espB_address = ('192.168.1.111', 1234)


station = network.WLAN(network.STA_IF)
station.active(True)
station.ifconfig((ip_address, subnet_mask, gateway, dns))
station.connect('Anode', 'anode@123')
print(sta.ifconfig()[0])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(espB_address)

def send_data_to_espB(data):
    sock.sendto(data.encode('utf-8'), espB_address)
    
while True:
    if button.value == 0:
        send_data_to_espB("Button Pressed")
        time.sleep(2)