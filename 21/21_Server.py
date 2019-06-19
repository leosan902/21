import random
import sys
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

cards=[]
pilha=[]
cardsValor=[]

clientes=[]

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

s =socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((HOST, PORT))
s.listen(5)
for i in range(2):
    conn, addr = s.accept()
    clientes.append(conn)
    cards.clear()
    cards.append(deck.pop())
    cards.append(deck.pop())
    cards.append(deck.pop())
    print("conexao "+ str(i+1))
    for i in cards :
         conn.send(i.encode('utf-8'))
         time.sleep(0.2)
cards.clear()
random.shuffle(clientes)
while True:
    for x in clientes:
        x.send(b'Sua vez')
        print("Vez de "+ str(x))
        data=b''
        while True:
          data=x.recv(12)
          cards.append(data.decode("utf-8"))
          if len(cards)==3:
              break
        print(cards)
        #print ("Sua mao e: %s , %s and %s. Pontuacao: %s "  % (cards[0],cards[1],cards[2], bmap[cardsValor[0]] + bmap[cardsValor[1]]+ bmap[cardsValor[2]]))
        if not pilha:
            x.sendall(b'1 - Pegar do Topo\n3 - Ficar com a mao\n') 
            while True:
                question=x.recv(13)
                if(question == b'1' or question == b'3'):
                    break
        else:
            x.sendall(b'1 - Pegar do Topo\n2 - Pegar da pilha %b\n3 - Ficar com a mao\n' % pilha[len(pilha)-1].encode('utf-8')) 
            while True:
                question=x.recv(13)
                if(question == b'1' or question == b'2' or question == b'3'):
                    break

        if question==b'1':
            topo=deck.pop()
            while True:
                try:
                    x.sendall(b'Escolha umas das opcoes para trocar de cartas pelo %b\n1- %b \n2- %b \n3- %b \n4-Nao trocar\n'  % (topo.encode('utf-8'),cards[0].encode('utf-8'),cards[1].encode('utf-8'),cards[2].encode('utf-8')))
                    while True:
                        troca=x.recv(13)
                     
                        if(question == b'1' or question == b'2' or question == b'3'or question == b'4'):
                            break
              
                    if troca==b'1':
                        pilha.append(cards[0])
                        cards[0]=topo
                        cardsValor.clear()
                        
                        for i in cards :
                             x.send(i.encode('utf-8'))
                             time.sleep(0.2)
                        cards.clear()
                        break
                    if troca==b'2':
                        pilha.append(cards[1])
                        cards[1]=topo
                        cardsValor.clear()
                        for i in cards :
                             x.send(i.encode('utf-8'))
                             time.sleep(0.2)
                        cards.clear()
                        break
                    if troca==b'3':
                        pilha.append(cards[2])
                        cards[2]=topo
                        cardsValor.clear()
                        for i in cards :
                             x.send(i.encode('utf-8'))
                             time.sleep(0.2)
                        cards.clear()
                        break
                    if troca==b'4':
                        pilha.append(topo)
                        for i in cards :
                             x.send(i.encode('utf-8'))
                             time.sleep(0.2)
                        
                        cards.clear()
                        break
                except Exception as e:
                    print(e)
          
        if question==b'2':
                
            while True:
                try:
                
                    x.sendall(b'Escolha umas das opcoes para trocar de cartas pelo %b\n1- %b\n2- %b\n3- %b\n4-Nao trocar\n'  % (pilha[len(pilha)-1].encode('utf-8'),cards[0].encode('utf-8'),cards[1].encode('utf-8'),cards[2].encode('utf-8')))
                    while True:
                        troca=x.recv(13)
                     
                        if(question == b'1' or question == b'2' or question == b'3'or question == b'4'):
                            break
                   
                    if troca==b'1':
                        temp=cards[0]
                        cards[0]=pilha[len(pilha)-1]
                        pilha.pop()
                        pilha.append(temp)
                        cardsValor.clear()
                        for i in cards :
                             x.send(i.encode('utf-8'))
                             time.sleep(0.2)
                        cards.clear()
                        break
                    if troca==b'2':
                        temp=cards[1]
                        cards[1]=pilha[len(pilha)-1]
                        pilha.pop()
                        pilha.append(temp)
                        cardsValor.clear()
                        for i in cards :
                             x.send(i.encode('utf-8'))
                             time.sleep(0.2)
                        cards.clear()
                        break
                    if troca==b'3':
                        temp=cards[2]
                        cards[2]=pilha[len(pilha)-1]
                        pilha.pop()
                        pilha.append(temp)
                        cardsValor.clear()
                        for i in cards :
                             x.send(i.encode('utf-8'))
                             time.sleep(0.2)
                        cards.clear()
                        break
                    if troca==b'4':
                        for i in cards :
                             x.send(i.encode('utf-8'))
                             time.sleep(0.2)
                        cards.clear()   
                        break
                                         
                except :
                    print("That's not a valid option!")
           
        if question==b'3':
            cards.clear()   
            break
          
        resutado = x.recv(100)
        if(resutado==b'Venci'):
            for x in clientes:
                try:
                    x.send(b'Voce Perdeu')
                    x.close()

                except:
                    pass
            time.sleep(5)
            sys.exit(0)
       

           
        

