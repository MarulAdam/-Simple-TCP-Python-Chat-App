import socket
import time
from modules import *

def secim1():
    host_ismi = "localhost"
    port = 7777

    internet_soketi = socket.socket()
    internet_soketi.connect((host_ismi,port))

    print(Mavi+"Connection established!! {}:{}".format(host_ismi, port))

    mesaj = input(Mavi+"----::")
    print(Mavi+"Waiting for server..")

    while mesaj != "cikis":
        internet_soketi.send(Eflatun+mesaj.encode())
        gelen_veri = internet_soketi.recv(1024).decode()

        print(Mavi+"SERVER : "+Eflatun+gelen_veri)

        mesaj = input(Mavi+"----::")
        print(Mavi+"Waiting for server..")

    internet_soketi.close()

def secim2():
    host_ismi = "localhost"
    port = 7777

    internet_soketi = socket.socket()
    internet_soketi.connect((host_ismi,port))

    print(Mavi+"Bağlantı sağlandı!! {}:{}".format(host_ismi, port))

    mesaj = input(Mavi+"----::")
    print(Mavi+"Server bekleniyor..")

    while mesaj != "cikis":
        internet_soketi.send(mesaj.encode())
        gelen_veri = internet_soketi.recv(1024).decode()

        print(Mavi+"SERVER : "+Eflatun+gelen_veri)

        mesaj = input(Mavi+"----::")
        print(Mavi+"Server bekleniyor..")
        
    internet_soketi.close()


banner = AcikYesil+"""
      ██████╗██╗  ██╗ █████╗ ████████╗     █████╗ ██████╗ ██████╗ 
     ██╔════╝██║  ██║██╔══██╗╚══██╔══╝    ██╔══██╗██╔══██╗██╔══██╗
     ██║     ███████║███████║   ██║       ███████║██████╔╝██████╔╝
     ██║     ██╔══██║██╔══██║   ██║       ██╔══██║██╔═══╝ ██╔═══╝ 
     ╚██████╗██║  ██║██║  ██║   ██║       ██║  ██║██║     ██║     
      ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═╝╚═╝     ╚═╝     
                                                                   
                                                                                    
                     [1]English          [2]Türkçe
"""
print(banner)

secim = input(Mavi+"Choise A Option ==>")

if secim == "1":
    secim1()
elif secim == "2":
    secim2()


