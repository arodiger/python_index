import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECTED!"

client_list = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# CREATE A DICTIONARY OF ALL THE CONNECTED CLIENTS SO THAT I CAN BROADCAST A MESSAGE
# TO EACH CONNECTED CLIENT

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected. ")
    client_list.append({addr,conn})
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)   #read in the header info, 64 bits
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)  #now read msg from client
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            msg_outgoing = input("")
            # msg_outgoing = "Msg received..."
            msg_outgoing = msg_outgoing.encode(FORMAT)        
            msg_outgoing_length = len(msg_outgoing)
            send_length = str(msg_outgoing_length).encode(FORMAT)
            send_length += b' ' * (HEADER - len(send_length))
            conn.send(send_length)
            conn.send(msg_outgoing)
            if len(client_list) > 0:
                print(f"dictionary count: {client_list[0]}")
                popped_connection = client_list.pop()
                popped_connection[0].send(send_length)
                popped_connection[0].send(msg_outgoing)

    conn.close()

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

