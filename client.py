import socket
import threading

host = ""
port = 4567
connectedtoserver = False
messages = []

def listentohost(e: socket.socket):
    global connectedtoserver
    while connectedtoserver:
        try:
            msgrecv = e.recv(1024)
            print(msgrecv.decode())
            #messages.append(msgrecv.decode())
        except TimeoutError:
            try:
                print("timeout rehehehe")
            except KeyboardInterrupt:
                print("Process terminated by keyboard interrupt")


s = socket.socket()
while connectedtoserver == False:
    try:
        host = input("Ip address to connect to: ") 
        s.connect((host,port))
        connectedtoserver = True
    except ConnectionRefusedError:
        print("Port is not open on this host or connection otherwise refused")
    except socket.gaierror:
        print("Could not find host")


x = threading.Thread(target=listentohost,args=(s))
x.start()

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