from GPIO.Sensors import Sensors
from Server import Server
from exceptions.AddressInUse import AddressInUse

us = Sensors()
us.start()

try:
    server = Server("0.0.0.0", 20002)
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
except AddressInUse:
    us.stop()
    exit(1)
