# UDPPingerServer.py (Versão para Python 3)
import random
from socket import *

# Cria um socket UDP
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Atribui a porta 12000
serverSocket.bind(('', 12000))

print("Servidor Pinger pronto para receber em Python 3.")

while True:
    rand = random.randint(0, 10)
    
    message, address = serverSocket.recvfrom(1024)
    
    # Decodifica a mensagem recebida para processá-la como texto
    message_str = message.decode('utf-8')
    
    # Simula perda de pacote
    if rand < 4:
        continue
            
    # Prepara e envia a resposta
    sequence_number = message_str.split()[1]
    response = f"Pong {sequence_number}"
    serverSocket.sendto(response.encode('utf-8'), address)