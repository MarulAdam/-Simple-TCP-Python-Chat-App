import socket
import time
from modules import *

def secim1():
    host_ismi = "localhost"
    port = 7777

    internet_soketi = socket.socket()
    internet_soketi.bind((host_ismi,port))
    internet_soketi.listen(1)

    baglanti, adres = internet_soketi.accept()

    print(Mavi+str(adres)+"connection established.")

    while True:
        while True:
            try:
                gelen_veri = str(baglanti.recv(1024).decode())
                print(Mavi+"CLIENT :"+Eflatun+gelen_veri)
                break
            except ConnectionResetError:
                time.sleep(2)
                baglanti, adres = internet_soketi.accept()
                print(Mavi+str(adres)+"connection established.")
        if gelen_veri ==  "cikis":
            break
        else:
            mesaj = input(Mavi+"----::")
            print(Mavi+"Waiting for client...")
            baglanti.send(mesaj.encode())

    baglanti.close()

def secim2():
    host_ismi = "localhost"
    port = 7777

    internet_soketi = socket.socket()
    internet_soketi.bind((host_ismi,port))
    internet_soketi.listen(1)

    baglanti, adres = internet_soketi.accept()

    print(Mavi+str(adres)+"bağlantı sağlandı.")

    while True:
        while True:
            try:
                gelen_veri = str(baglanti.recv(1024).decode())
                print(Mavi+"CLIENT :"+Eflatun+gelen_veri)
                break
            except ConnectionResetError:
                time.sleep(2)
                baglanti, adres = internet_soketi.accept()
                print(Mavi+str(adres)+"bağlantı sağlandı.")
        if gelen_veri ==  "cikis":
            break
        else:
            mesaj = input(Mavi+"----::")
            print(Mavi+"Client bekleniyor...")
            baglanti.send(mesaj.encode())

    baglanti.close()

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
