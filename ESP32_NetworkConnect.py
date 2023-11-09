import network

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)  # Create a station interface object
    if not wlan.isconnected():  # Check if it's already connected
        print('Connecting to WiFi...')
        wlan.active(True)  # Activate the interface
        wlan.connect(ssid, password)  # Connect to the WiFi network

        while not wlan.isconnected():
            pass

    print('Connected to WiFi')
    print('Network config:', wlan.ifconfig())

# Replace 'your_SSID' and 'your_password' with your actual WiFi credentials
connect_to_wifi('ssid', 'passwd')
