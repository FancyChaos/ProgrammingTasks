from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.scrollview import ScrollView

Config.set('graphics', 'width', '50')
Config.set('graphics', 'height', '300')


from functools import partial

import socket
import threading
import sys

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65339   # The port used by the server

username= ""

def post(msg):

    msg = msg.replace("b\\'","")
    msg = msg.replace("b'","")
    msg = msg.replace('b"',"")
    msg = msg.replace("\\''","")
    msg = msg.replace("\\'","")
    msg = msg.replace("\\\\r","")
    addChat(msg)

def listen(s):
    while True:
        data = s.recv(1024)
        data = repr(data)[2:]
        if "\n" in data:
            split = data.split("\\n")
            for stri in split:
                post(stri)
        else:
            post(data)


scroll = ScrollView()
textinput = TextInput(text='', multiline=False,size_hint= (.2, None), height= 30)
noinput = TextInput(text='', multiline=False, readonly= True ,size_hint= (1, None))
noinput.height=(len(noinput._lines)+1) * noinput.line_height
b = Button(text='send',size_hint= (.1, None), height= 30)

class Chat(App):
    def build(self):
        Window.size = (400, 300)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))

        name = username
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
                    for stri in split:
                        stri = stri.replace("b\\'","")
                        stri = stri.replace("b'","")
                        stri = stri.replace('b"',"")
                        stri = stri.replace("\\''","")
                        stri = stri.replace("\\'","")
                        stri = stri.replace("\\\\r","")
                        stri = stri.replace("\\n","")
                        if "9849846516189615" in stri:
                            post("")
                            break
                        post(stri)
                break


        mythread = threading.Thread(target=listen, args = (s,),name = "Thread",)  # ...Instantiate a thread and pass a unique ID to it
        mythread.start()





        layout = BoxLayout(orientation='vertical')
        layout2 = BoxLayout(orientation='horizontal',size_hint= (1, None), height= 30)
        b.bind(on_press=partial(self.click, s))

        textinput.bind(on_text_validate=partial(self.on_enter2, s))


        scroll.add_widget(noinput)

        layout.add_widget(scroll)
        layout.add_widget(layout2)
        layout2.add_widget(textinput)
        layout2.add_widget(b)
        return layout

    def on_start(self):
        textinput.focus = True

    def on_enter2(instance,s,value):
        s.sendall(bytes(textinput.text,'utf-8'))
        textinput.text = ""
        textinput.focus = True

    def click(instance,s,value):
        s.sendall(bytes(textinput.text,'utf-8'))
        textinput.text = ""
        textinput.focus = True

def addChat(stri):
    noinput.text+= stri +"\n"
    textinput.focus = True
    noinput.height=(len(noinput._lines)+1) * noinput.line_height
    scroll.scroll_y = 0

txtin = TextInput(text='Nickname', multiline=False,size_hint= (.2, None), height= 30)

class Name(App):

    def build(self):
        Window.size = (300, 50)

        layout1 = AnchorLayout(anchor_x='left', anchor_y='center')
        layout = BoxLayout(orientation="horizontal",size_hint= (1, None), height= 30)

        but = Button(text="join",size_hint= (.2, None), height= 30)
        global txtin
        layout.add_widget(txtin)
        layout.add_widget(but)

        but.bind(on_press=self.click2)

        txtin.bind(on_text_validate=self.on_en)

        layout1.add_widget(layout)

        return layout1

    def on_en(self,instance):
        global username
        username = txtin.text
        Chat().run()

    def click2(self,instance):
        global username
        username = txtin.text
        Chat().run()

    def on_start(self):
        txtin.focus = True


ch = Name()
ch.run()
username = ch.username
