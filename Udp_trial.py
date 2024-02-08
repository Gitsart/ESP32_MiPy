import network
import machine
import time
import socket

led = machine.Pin(2, machine.Pin.OUT)
button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

def blink():
    led.value(1)
    time.sleep(.5)
    led.value(0)
    time.sleep(.5)
    
ip_address = '192.168.1.100'
subnet_mask = '255.255.255.0'
gateway = '192.168.1.1'
dns = '8.8.8.8'

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.ifconfig((ip_address, subnet_mask, gateway, dns))
sta.connect('Anode_Guest_389D', '0123456789')

udp_target_ip = '192.168.1.105'  # IP address of ESP32_2
udp_target_port = 12345

while sta.isconnected() == True:
    print("Connected")
    time.sleep(.2)
    if button.value() == 0:
        print("Button pressed")
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.sendto(b'1', (udp_target_ip, udp_target_port))
        udp_socket.close()
        time.sleep(0.2)
        blink()
