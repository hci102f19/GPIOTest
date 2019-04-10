from GPIO.UltrasonicSensor import UltrasonicSensor
from Server import Server

us = UltrasonicSensor("TEST", 17, 4)
us.start()

server = Server("0.0.0.0", 20001)
server.message_loop.emits(us)

server.start()

try:
    run = True
    while run:
        text = input()

        if text == "stop":
            us.stop()
            server.stop()
            run = False
        if text == "list":
            for idx, c in enumerate(server.clients):
                print("{}: {}".format(idx + 1, c))
except KeyboardInterrupt:
    us.stop()
    server.stop()
    run = False
