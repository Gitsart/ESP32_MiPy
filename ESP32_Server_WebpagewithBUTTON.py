import network
import usocket as socket
from machine import Pin

# Set up LED pin
led = Pin(2, Pin.OUT, value=1)  # GPIO2 is the built-in LED on most ESP32 boards

# Create an access point (AP)
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid="ESP-Server", password="ServerPass")

# Print the AP IP address
print("AP IP Address:", ap.ifconfig()[0])

# Define HTML content for the webpage
html = const("""
<!DOCTYPE html>
<html>
<head>
    <title>ESP32 LED Control</title>
</head>
<body>
    <h1>ESP32 LED Control</h1>
    <form>
        LED: 
        <button type="submit" name="action" value="on">Turn On</button>
        <button type="submit" name="action" value="off">Turn Off</button>
    </form>
</body>
</html>
""")

# Create a function to handle client requests
def handle_request(client):
    request = client.recv(1024)
    print(request)
    
    # Check if request contains "GET / "
    if request.find(b"GET / ") != -1:
        client.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
        client.send(html)
        client.close()
    
    # Check if request contains "GET /?action=on"
    elif request.find(b"GET /?action=on") != -1:
        led.off()
        client.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
        client.send(html)
        client.close()
    
    # Check if request contains "GET /?action=off"
    elif request.find(b"GET /?action=off") != -1:
        led.on()
        client.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
        client.send(html)
        client.close()

# Set up a socket server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 80))
server.listen(1)

# Main loop to handle client requests
while True:
    client, addr = server.accept()
    handle_request(client)
