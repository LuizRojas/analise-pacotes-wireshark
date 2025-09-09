import sys, time
from socket import *

# Pega o host e a porta a partir dos argumentos
host = sys.argv[1]
port = int(sys.argv[2])
timeout_duration = 1  # em segundos

# Cria o socket UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Define o timeout
clientSocket.settimeout(timeout_duration)

print(f"Pinging {host}:{port}...")

# Envia 10 pings
for ptime in range(1, 11):
    data_str = f"Ping {ptime} {time.asctime()}"
    data_bytes = data_str.encode('utf-8')

    try:
        # Registra o tempo de envio
        RTTb = time.time()
        # Envia a mensagem de ping
        clientSocket.sendto(data_bytes, (host, port))
        # Espera pela resposta
        message, address = clientSocket.recvfrom(1024)
        # Registra o tempo de recebimento
        RTTa = time.time()
        
        print(f"Resposta de {address[0]}: {message.decode()}")
        print(f"RTT: {RTTa - RTTb:.6f} segundos")

    except timeout:
        print("Request timed out.")

print("Ping finalizado.")
clientSocket.close()