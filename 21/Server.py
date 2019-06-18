import random
import socket
import time
deck=[]
numeros=['2','3','4','5','6','7','8','9','10',"J","Q","K","A"]
for word in numeros:
    deck.append(word+" de Paus")
    deck.append(word+" de Espadas")
    deck.append(word+" de Ouros")
    deck.append(word+" de Copas")

random.shuffle(deck)
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
cards=[]
cardsValor=[]
pilha=[]

#end = cards[0].find(' ') 
#cardsValor.append(cards[0][:end])
#end = cards[1].find(' ') 
#cardsValor.append(cards[1][:end])
#end = cards[2].find(' ') 
#cardsValor.append(cards[2][:end]) 
clientes=[]

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

s =socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((HOST, PORT))
s.listen(5)
for i in range(5):
    conn, addr = s.accept()
    clientes.append(conn)
    cards.clear()
    cards.append(deck.pop())
    cards.append(deck.pop())
    cards.append(deck.pop())
    print("conexao "+ str(i+1))
    for i in cards :
         conn.send(i.encode('utf-8'))
         time.sleep(0.1)

random.shuffle(clientes)
for i in clientes:
    i.send(b'Sua vez')
    
         
         
         
            