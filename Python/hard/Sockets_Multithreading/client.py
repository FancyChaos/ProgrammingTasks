import socket
import threading
import sys

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65339   # The port used by the server

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()



def post(msg):

    msg = msg.replace("b\\'","")
    msg = msg.replace("b'","")
    msg = msg.replace('b"',"")
    msg = msg.replace("\\''","")
    msg = msg.replace("\\'","")
    msg = msg.replace("\\\\r","")
    print(msg)
    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[K")
    print(msg)

def listen(socket):
    while True:
        data = s.recv(1024)
        data = repr(data)[2:]
        if "\n" in data:
            print("drin")
            split = data.split("\\n")
            print(split)
            for str in split:
                post(str)
        else:
            post(data)


def write(s):
    getch = _Getch()
    msg =""
    while True:
        msg += getch.__call__()
        print(msg)
        if "\r" in msg:
            s.sendall(bytes(msg,'utf-8'))
            sys.stdout.write("\033[F") #back to previous line
            sys.stdout.write("\033[K")
            msg = ""
        elif msg == "":
            print("buffer")
        else:
            sys.stdout.write("\033[F") #back to previous line
            sys.stdout.write("\033[K")
        if "\x7f" in msg:
            msg = msg[:-2]
            print(msg)
            sys.stdout.write("\033[F") #back to previous line
            sys.stdout.write("\033[K")
        if "\x03" in msg:
            sys.exit()



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    try:
        name = input("Username:")
        name = name + "9849846516189615"
        s.sendall(bytes(name,'utf-8'))
        data = bytes("",'utf-8')
        while True:
            data += s.recv(1024)
            if "9849846516189615" in str(data):
                d = str(repr(data))#[2:-17]
                if "\\n" in d:
                    split = d.split("\\n")
                    post("")
                    post("Vorherige Konversation:")
                    for str in split:
                        str = str.replace("b\\'","")
                        str = str.replace("b'","")
                        str = str.replace('b"',"")
                        str = str.replace("\\''","")
                        str = str.replace("\\'","")
                        str = str.replace("\\\\r","")
                        str = str.replace("\\n","")
                        if "9849846516189615" in str:
                            post("")
                            break
                        post(str)
                break


        mythread = threading.Thread(target=listen, args = (s,),name = "Thread",)  # ...Instantiate a thread and pass a unique ID to it
        mythread.start()

        write(s)
    except (KeyboardInterrupt, SystemExit):
        s.close()
