import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Criado!!!')
host = 'localhost'
porta = 5433
mensagem = 'Cliente: testando 123 testando!'

try:
    print(('cliente: ' + mensagem))
    s.sendto(mensagem.encode(), (host, 5431))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print(dados)
finally:
    print('cliente: Acabou!!!!!!!')
    s.close()