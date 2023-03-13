# when receiving data, if the data is a signal looking for servers, send data back with the name of the server
# when a new user tries to connect, instead of straight up accepting the connection, create a new thread that accepts the connection so you can have multiple clients connected
# host has multiple functions in which it sends data to the clients:
# 1 for messages being sent to the specified client (or group)
# 1 for the client joining and being given the stored chat log
# 1 for the client being passed the names of other clients connected (for direct messages)
# if a message is sent to a client when they are not connected, the host will store this message and send it to them when they rejoin
# (when a new client joins, the server checks to see if it has messages stored for this client)

import socket
import threading
import datetime

messages = [{}] # also write chat log to file
# storedusers = [{"name":john,"hardwareid":"1232_AFS12","username":"johnthegreatest27","password":"password"}] also written to file
connectedclients = []

def listentoclient(c: socket.socket,a: tuple): # that is how you type variables in python :D
    global serveropen
    global sendmessage
    global connectedclients
    connectedclients.append(c)
    connectedtoclient = True
    c.send(welcomemsg.encode())
    c.settimeout(1)

    # check for new messages
    while connectedtoclient and serveropen:
        try:
            msg = c.recv(1024) # 2 different messages received from client on different wavelengths, one for message, and one for general ping / showing its there. If the ping one fails, close connection. if the msg one fails, just check again
            time = datetime.datetime.now().strftime("%H:%M")
            print(a[0] + " at " + time + ": " + msg.decode())
            messages.append({"time":time,"sender":a,"msg":msg.decode()}) # change sender to username of a, or displayname of a, or userid of a
            sendmessage(str({"time":time,"sender":a,"msg":msg.decode()}).encode()) # figure out how to send message data (dictionary) in form of string
        except TimeoutError:
            try:
                #print("checking for new message from client")
                pass
            except KeyboardInterrupt:
                print("keyboard interrupted while checking for new messages, terminating connection to client")
                c.close()
                connectedtoclient = False
        except ConnectionResetError:
            print("the user that was associated with this connection (" + a[0] + ") closed their client!")
            connectedtoclient = False
        

def sendmessage(m):
    for i in connectedclients:
        i:socket.socket; i.send(m)

host = "localhost"
port = 4567
#welcomemsg = input("What would you like your welcome message for new users joining the server to be? ")
welcomemsg = "WELCOME TO THE PARTY"

s = socket.socket()
s.bind((host,port))
s.listen()
s.settimeout(1)
serveropen = True

# check for new connections
while serveropen:
    try:
        # user has connected, this is where a new thread should be opened to handle this connection
        # this client should also be added to a list of connected clients, and have an id assigned to them, and a client chosen name
        (conn,addr) = s.accept()
        print("connection found")
        print("from " + addr[0])
        x = threading.Thread(target=listentoclient,args=(conn,addr))
        x.start()
        
    except TimeoutError:
        try:
            #print("scanning for connections")
            pass
        except KeyboardInterrupt:
            print("Process terminated due to keyboard interrupt")
            s.close()
            serveropen = False