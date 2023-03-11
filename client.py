import socket

host = input("Ip address to connect to: ")
port = 4567

s = socket.socket()
s.connect((host,port))
e = s.recv(1024)
print(e.decode())
connectedtoserver = True

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