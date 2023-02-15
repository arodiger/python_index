import socket
import threading

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 55555
ADDRESS = (SERVER,PORT)

killallthreads = False
lock = threading.Lock()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

nickname = input("Choose a nickname: ")         #cli ask and assign nickname

def receive():
    global killallthreads, lock
    while True and not killallthreads:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                if nickname not in message:
                    print(message)                  #clo print message from server
        except:
            if not killallthreads:
                print("An error occurred inside receive!")         #error so close connection and thread 
            lock.acquire()
            killallthreads = True
            lock.release()
            client.close()
            break


def write(): 
    global killallthreads, lock
    while True and not killallthreads:
        try:
            cli_message = input("")
            message = f'{nickname}: {cli_message}'   #endless loop of awaiting cli
            client.send(message.encode('ascii'))    #print cli
            if cli_message == "EXIT":
                raise
        except:
            print(f'{nickname}: is exiting')
            lock.acquire()
            killallthreads = True
            lock.release()
            client.close()
            break


processing_thread = threading.Thread(target=receive)    #thread to receive msg from server
processing_thread.start()

write_thread = threading.Thread(target=write)           #thread to send msg to server
write_thread.start()
