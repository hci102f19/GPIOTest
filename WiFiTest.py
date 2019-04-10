from Server import Server
from WiFi import WiFi

device = WiFi("wlan0", "AAU-1x")
device.start()

server = Server("0.0.0.0", 20001)
server.message_loop.emits(device)

server.start()

try:
    run = True
    while run:
        text = input()

        if text == "stop":
            device.stop()
            server.stop()
            run = False
        if text == "list":
            for idx, c in enumerate(server.clients):
                print("{}: {}".format(idx + 1, c))
except KeyboardInterrupt:
    device.stop()
    server.stop()
    run = False
