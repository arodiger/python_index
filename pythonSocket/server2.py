import socket
import threading

HEADER = 64
PORT = 5050
# SERVER = "192.168.1.125"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECTED!"

#instantiate a socket for tcp(AF_INET) and data stream(SOCK_STREAM) communication
#associate the socket class to a specific ip:port, tuple object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# handle_client function will first read in header.  header contains the length of the 
# message string that is being sent.  once length of string is aquired now read in the 
# message.  both header and message are encoded with utf-8.  print out message.
# now send back a header with the length of the return message, and then send 
# the return message.  if you receive DISCONNECT_MESSAGE, then disconnect.
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected. ")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)   #read in the header info, 64 bits
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)  #now read msg from client
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            # return encoded message from server to client 
            msg_outgoing = "Msg received..."
            msg_outgoing = msg_outgoing.encode(FORMAT)        
            msg_outgoing_length = len(msg_outgoing)
            send_length = str(msg_outgoing_length).encode(FORMAT)
            #store msg length in header and pad remainder 64 bits with blanks
            send_length += b' ' * (HEADER - len(send_length))
            conn.send(send_length)
            conn.send(msg_outgoing)
            # conn.send("Msg received".encode(FORMAT))    #send msg back to client

    conn.close()

# start function, server will begin to listen for client's requests to connect to a 
# specific port.  accept the client's request.  Now create/instantiate a thread for the  
# client's connection and call the handle_client function. start the thread.  
# log the active count of clients.
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        client_communication_socket, addr = server.accept()
        thread = threading.Thread(target=handle_client, args =(client_communication_socket, addr)) 
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("[STARTING] server is starting...")
start()

