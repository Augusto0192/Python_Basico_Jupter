import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print('foi!? Foi!!')
host = 'localhost'
port = 5431
s.bind((host, port))
mensagem = "Servidor: Caterine Gibran"
while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print('serv: mensagem enviada Cat')
        s.sendto(dados + (mensagem.encode()), end)
