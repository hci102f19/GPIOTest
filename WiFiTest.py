# from time import sleep
#
# from WiFi import WiFi
#
# device = WiFi("wlan0", "AAU-1x")
# device.start()
#
# try:
#     while True:
#         print(device.emit())
#         sleep(1)
# except KeyboardInterrupt:
#     device.stop()
#
#
# from GPIO.Sensors import Sensors
# from Server import Server
from Server import Server
from WiFi import WiFi

# device = WiFi("wlan0", "AAU-1x")
device = WiFi("wlan0")
device.start()

server = Server("0.0.0.0", 20001)
server.message_loop.emits(device)

server.start()
