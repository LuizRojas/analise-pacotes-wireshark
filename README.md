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

## Etapa 2

bla bla

## Sockets UDP e TCP

bla bla
