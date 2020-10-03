import socket
import settings

ADDR = (settings.HOST, settings.PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(ADDR)