import json
import socket

bytesToSend = "HELO".encode('utf-8')

serverAddressPort = ("192.168.1.102", 20001)
# serverAddressPort = ("127.0.0.1", 20001)

bufferSize = 4096

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

while True:
    message, _ = UDPClientSocket.recvfrom(bufferSize)

    data = json.loads(message.decode('utf-8'))
    print(data)
