import socket
import threading
import time

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65339     # Port to listen on (non-privileged ports are > 1023)


def client(conn,addr,startchat):
    with conn:
        print('Connected by', addr)
        i=0
        while i < len(startchat)-1:
            conn.sendall(bytes(startchat[i],'utf-8'))
            i+=1

        conn.sendall(bytes("9849846516189615",'utf-8'))
        while True:
            data = conn.recv(1024)
            if not data:
                i  = 0
                while i < len(clients):
                    if clients[i] == conn:
                        print("remove")
                        clients[i].remove()
                        break
                    i+=1
                break
            d = repr(addr)+":"+repr(data)
            post(d)


chat = []
clients = []

def stamp():
    t = time.localtime()

    return str(t.tm_hour) +":"+ str(t.tm_min) +":"

def post(msg):
    msg = stamp()+msg
    chat.append(msg+"\n")

    for cl in clients:
        try:
            cl[0].sendall(bytes(msg,'utf-8'))
        except:
            pass


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    try:
        s.listen()


        while True:
            conn, addr = s.accept()


            while True:
                name = conn.recv(1024)
                name = repr(name)
                print(name)
                if "9849846516189615" in name:
                    name = name[1:-17]
                    break

            login = name+" joined"
            post(login)

            clients.append((conn,addr))
            print('Connected by', addr)
            mythread = threading.Thread(target=client, args = (conn,name,chat),name = "Thread-{}".format(addr),)  # ...Instantiate a thread and pass a unique ID to it
            mythread.start()
    except (KeyboardInterrupt, SystemExit):
        s.close()
