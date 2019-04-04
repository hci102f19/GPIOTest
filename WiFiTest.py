from Server import Server
from WiFi import WiFi

# device = WiFi("wlan0", "AAU-1x")
device = WiFi("wlan0", "AAU-1x")
device.start()

server = Server("0.0.0.0", 20001)
server.message_loop.emits(device)

server.start()
