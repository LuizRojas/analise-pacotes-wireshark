# Análise de pacotes com Wireshark

## Etapa 1

Consulta

- IP origem/destino [192.168.1.133/8.8.8.8]
- Porta origem/destino [50137/53]
- Protocolo da camada de transporte utilizado [UDP]
- Tamanho do pacote UDP (carga útil + cabeçalho) [35 bytes + 20 bytes = 55 bytes]
- Valor da consulta [i.scdn.co]
- Tipo de RR consultado (A, MX, NS, CNAME, AAAA) [AAAA]

![Consulta da etapa 1](/images/etapa1/consulta/consulta_etapa1.png "Consulta da etapa 1")
![Tipo de RR Consultado](/images/etapa1/consulta/consulta_etapa1_tipo_rr.png "Tipo de RR Consultado")

Resposta

- IP origem/destino [8.8.8.8/192.168.1.133]
- Porta origem/destino [53/50137]
- Protocolo da camada de transporte utilizado [UDP]
- Tamanho do pacote UDP (carga útil + cabeçalho) [159 bytes + 20 bytes = 199 bytes]
- Resposta da consulta [scdnco.spotify.map.fastly.net possui o endereço IPv6 2a04:4e42:4f::760]
- Tipo de RR respondido (A, MX, NS, CNAME, AAAA) [AAAA]

![Resposta da etapa 1](/images/etapa1/resposta/resposta_etapa1.png "RR respondido")
![Tipo de RR Respondido](/images/etapa1/resposta/resposta_etapa1_tipo_rr.png "Tipo de RR Respondido")

## Etapa 2 (Sockets UDP e TCP)

### UDP

(Pacotes enviados)

- IP origem/destino [127.0.0.1/127.0.0.1]
- Porta origem/destino [54496/12000]
- Protocolo da camada de transporte utilizado [UDP]
- Tamanho do pacote UDP/TCP (Carga útil + cabeçalho) [13 bytes + 20 bytes = 33 bytes]

(Pacotes recebidos)

- IP origem/destino [127.0.0.1/127.0.0.1]
- Porta origem/destino [12000/54496]
- Protocolo da camada de transporte utilizado [UDP]
- Tamanho do pacote UDP/TCP (Carga útil + cabeçalho) [13 bytes + 20 bytes = 33 bytes]

### TCP

Estrutura

![Estrutura](/images/etapa2/tcp/cliente-servidor-tcp.png "Estrutura")

(Pacotes enviados)

- IP origem/destino [127.0.0.1/127.0.0.1]
- Porta origem/destino [4808/12000]
- Protocolo da camada de transporte utilizado [TCP]
- Tamanho do pacote UDP/TCP (Carga útil + cabeçalho) [25 bytes + 20 bytes = 45 bytes]

![Consulta TCP Etapa 2](/images/etapa2/tcp/consulta.png "Consulta TCP")

(Pacotes recebidos)

- IP origem/destino [12000]
- Porta origem/destino [4808]
- Protocolo da camada de transporte utilizado [TCP]
- Tamanho do pacote UDP/TCP (Carga útil + cabeçalho) [25 bytes + 20 bytes = 45 bytes]

![Resposta TCP Etapa 2](/images/etapa2/tcp/resposta.png "Resposta TCP")

## Etapa 3 (Socket UDP Pinger)

Estrutura

![Estrutura](/images/etapa3/cliente-servidor-udp-pinger.png "Estrutura")

(Pacote enviado)

- IP origem/destino [127.0.0.1/127.0.0.1]
- Porta origem/destino [53229/12000]
- Protocolo da camada de transporte utilizado [UDP]
- Tamanho do pacote UDP/TCP (Carga útil + cabeçalho) [39 bytes + 20 bytes = 59 bytes]

![Ping](/images/etapa3/ping01.png "Ping")

(Pacote recebido)

- IP origem/destino [127.0.0.1/127.0.0.1]
- Porta origem/destino [12000/53229]
- Protocolo da camada de transporte utilizado [UDP]
- Tamanho do pacote UDP/TCP (Carga útil + cabeçalho) [14 bytes + 20 bytes = 34 bytes]

![Pong](/images/etapa3/pong01.png "Pong")
