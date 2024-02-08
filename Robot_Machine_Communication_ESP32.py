import network
import usocket as socket
from machine import Pin
import time
import esp

esp.osdebug(None)

# Set up LED pin
led = Pin(2, Pin.OUT, value=0)  # GPIO2 is the built-in LED on most ESP32 boards
buzz = Pin(4, Pin.OUT, value=0)
button = Pin(12, Pin.IN, Pin.PULL_UP)  # Push button on GPIO12 with pull-up resistor

def blink():
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)

# Create an access point (AP)
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid="ESP-Server", password="ServerPass")

# Print the AP IP address
print("AP IP Address:", ap.ifconfig()[0])

# Define HTML content for the LED control webpage
led_control_html = const("""
<!DOCTYPE html>
<html>
<head>
    <title>ESP32 AGV Control</title>
    <script>
        function updateStatus() {
            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    document.getElementById("status").innerHTML = this.responseText;
                }
            };
            xhttp.open("GET", "/status", true);
            xhttp.send();
        }
    </script>
</head>
<body onload="setInterval(updateStatus, 5000)">
    <h1>ESP32 AGV Control</h1>
    <form>
        LED: 
        <button type="submit" name="action" value="on">Call AGV</button>
        <button type="submit" name="action" value="off">Release AGV</button>
    </form>
    <p id="status">Status: </p>
</body>
</html>
""")

# Define HTML content for the AGV finished webpage
agv_finished_html = const("""
<!DOCTYPE html>
<html>
<head>
    <title>AGV Finished</title>
</head>
<body>
    <h1>AGV Finished</h1>
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
        client.send(led_control_html)
        client.close()
        blink()
    
    # Check if request contains "GET /?action=on"
    elif request.find(b"GET /?action=on") != -1:
        led.on()  # Corrected: Turn LED ON
        client.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
        client.send(led_control_html)
        client.close()
    
    # Check if request contains "GET /?action=off"
    elif request.find(b"GET /?action=off") != -1:
        led.off()  # Corrected: Turn LED OFF
        client.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
        client.send(led_control_html)
        client.close()
    
    # Check if request contains "GET /status"
    elif request.find(b"GET /status") != -1:
        if button.value() == 0:  # Button is pressed
            client.send("DONE")
        else:
            client.send("Waiting")
        client.close()
    
    # Check if request contains "GET /agv_finished"
    elif request.find(b"GET /agv_finished") != -1:
        client.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
        client.send(agv_finished_html)
        client.close()

# Set up a socket server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 80))
server.listen(1)

# Main loop to handle client requests
while True:
    client, addr = server.accept()
    handle_request(client)
server.close