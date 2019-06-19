#!/usr/bin/env python3

import socket
import time
import sys
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((HOST, PORT))
cards=[]
bmap = { 
         'K' : 10,
         'Q' : 10,
         "J" : 10,
         '10': 10,
         '9' : 9,
         '8' : 8,
         '7' : 7,
         '6' : 6,
         '5' : 5,
         '4' : 4, 
         '3' : 3, 
         '2' : 2,
         'A' : 1
       }
cardsValor=[]
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
        data=s.recv(12)
        if data !=b'':
            print(data.decode("utf-8"))
            break
    if data !=b'Sua vez':
       time.sleep(5)
       sys.exit(0)
        

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
        cardsValor.clear()
        end = cards[0].find(' ') 
        cardsValor.append(cards[0][:end])
        end = cards[1].find(' ') 
        cardsValor.append(cards[1][:end])
        end = cards[2].find(' ') 
        cardsValor.append(cards[2][:end]) 
        if(bmap[cardsValor[0]] + bmap[cardsValor[1]]+ bmap[cardsValor[2]]==21):
            print('Venci')
            s.send(b'Venci')
            s.close()
            time.sleep(5)
            sys.exit(0)
        else:
            s.send(b'Continua')
input('Press Enter to exit') 
bmap[cardsValor[0]] + bmap[cardsValor[1]]+ bmap[cardsValor[2]]==21