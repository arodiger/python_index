import socket
import threading

HEADER = 64
PORT = 5050
# SERVER = "192.168.1.125"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECTED!"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


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
            conn.send("Msg received".encode(FORMAT))    #send msg back to client

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()                    #accept connection from new client
        #create client thread for client connection and call handle_client function.
        thread = threading.Thread(target=handle_client, args =(conn, addr)) 
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("[STARTING] server is starting...")
start()

