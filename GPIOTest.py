from GPIO.UltrasonicSensor import UltrasonicSensor
from Server import Server

us = UltrasonicSensor("TEST", 17, 4)
us.start()

server = Server("0.0.0.0", 20001)
server.message_loop.emits(us)

server.start()

while True:
    text = input()

    if text == "stop":
        server.stop()
    if text == "list":
        for idx, c in enumerate(server.clients):
            print("{}: {}".format(idx + 1, c))
