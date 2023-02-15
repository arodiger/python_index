import socket

HEADER = 64
PORT = 5050
# SERVER = "192.168.1.125"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECTED!"

#setup a socket class to handle connection to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#create a socket connection to server
client.connect(ADDR)        


def send(msg):
    #first encode msg to be sent.
    message = msg.encode(FORMAT)        
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    #store msg length in header and pad remainder 64 bits with blanks
    send_length += b' ' * (HEADER - len(send_length))
    #send header
    client.send(send_length)
    #send msg
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hello World!") 
input()                     #used to hold this client up, to test other clients added
send("Hello #2")
input()
send("Hello #3")
input()
send(DISCONNECT_MESSAGE)

