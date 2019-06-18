#!/usr/bin/env python3

import socket
import time
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((HOST, PORT))
cards=[]

while True:
 try:
      data=s.recv(13)
 except :
     break
 cards.append(data.decode("utf-8"))
  
 if len(cards)==3:
      break
print('Sua Mao e ')
print(cards)
data=''

while True: 
    data =b''
    while True:
        data=s.recv(10)
        if data !=b'':
            print(data)
            break
    #if data !=b'Sua vez':
    #    print(data)
    #    break
    if data ==b'Sua vez':
        for i in cards :
            s.send(i.encode("utf-8"))
            time.sleep(0.2)
        
        while True:
            pergunta=s.recv(1500)
            if  pergunta !=b'':
                break
        escolha=input(pergunta.decode("utf-8")) 
        s.sendall(escolha.encode("utf-8"))
        opcao=b''
        if escolha=='1':
            while True:
                opcao=s.recv(1500)
                if  opcao !=b'':
                    break
            escolha=input(opcao.decode("utf-8"))
            s.send(escolha.encode("utf-8"))
            escolha=''
            cards.clear()
            data=b''
            while True:
                
                data=s.recv(13)
                if(data!=b''):
                    cards.append(data.decode("utf-8"))
                if len(cards)==3:
                    break
            print(cards)
            data=b''
        if escolha=='2':
            while True:
                opcao=s.recv(1500)
                if  opcao !=b'':
                    break
            escolha=input(opcao.decode("utf-8"))
            s.send(escolha.encode("utf-8"))
            escolha=''
            cards.clear()
            data=b''
            while True:
                
                data=s.recv(13)
                if(data!=b''):
                    cards.append(data.decode("utf-8"))
                if len(cards)==3:
                    break
            print(cards)
            data=b''
        if escolha=='3':
            data=b''
            escolha=''
            time.sleep(1)
input('Press Enter to exit') 
bmap[cardsValor[0]] + bmap[cardsValor[1]]+ bmap[cardsValor[2]]==21