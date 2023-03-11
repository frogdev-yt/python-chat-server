import socket
import threading

host = input("Ip address to connect to: ")
port = 4567
messages = []

s = socket.socket()
s.connect((host,port))
e = s.recv(1024)
print(e.decode())
connectedtoserver = True

x = threading.Thread(target=)

def listentohost(c):
    global connectedtoserver
    while connectedtoserver:
        try:
            msgrecv = c.recv(1024)


while connectedtoserver:
    try:
        msg = input("Message: ")
        s.send(msg.encode())

    except KeyboardInterrupt:
        print("keyboard interruptered!")
        connectedtoserver = False

    except TimeoutError:
        print("disconnected from server, timed out")
        connectedtoserver = False

    except ConnectionAbortedError:
        print("disconnected from server, server closed the connection")
        connectedtoserver = False