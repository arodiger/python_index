import socket

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "DISCONNECT_MESSAGE"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)        

def send(msg):
    msg_incomming = ""
    while True and msg_incomming != DISCONNECT_MESSAGE:
        message = msg.encode(FORMAT)        
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        client.send(send_length)
        client.send(message)
        msg_length_incomming = client.recv(HEADER).decode(FORMAT) 
        if msg_length_incomming:
            msg_length_incomming = int(msg_length_incomming)
            msg_incomming = client.recv(msg_length_incomming).decode(FORMAT)  
            print(f"[SERVER RESPONSE] {msg_incomming}")


send("Client Begin: ") 

