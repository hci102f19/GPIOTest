from GPIOServer import GPIOServer
from WiFiServer import WiFiServer

gpio = GPIOServer("0.0.0.0", 20002, 'GPIO Service', 'GPIO.local')
wifi = WiFiServer("0.0.0.0", 20001, 'WiFi Service', 'WiFi.local')

try:
    gpio.start()
    wifi.start()

    run = True
    while run:
        text = input()

        if text == "stop":
            gpio.stop()
            wifi.stop()
            run = False
        if text == "list":
            print("WiFi:")
            wifi.list_clients()
            print("GPIO:")
            gpio.list_clients()
except KeyboardInterrupt:
    gpio.stop()
    wifi.stop()
    run = False