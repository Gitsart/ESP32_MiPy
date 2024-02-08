import network
import time

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect('Anode_Guest_389D', '0123456789')
while sta.isconnected() == True:
    print("Connected")
    print(sta.ifconfig()[0])
