import socket
import threading

HEADER = 64
PORT = 8000
SERVER = socket.gethostbyname(socket.gethostname())
SERVER = '192.168.29.229'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(ADDR)
server.bind(ADDR)


def handle_client(conn, addr):
    print("connetions " + str(addr))

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        try:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(str(addr) + msg)

        except:
            pass
    conn.twclose()


def start():
    server.listen()
    print("server address " + str(SERVER))
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print("connections = " + str(threading.activeCount() - 1))


print("starting server")
start()
