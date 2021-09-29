import socket
import  sys

def tcp_cliente():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('Conecxão falhou \n')
        print(e)
        sys.exit()

    print("Sucesso!!!")

    hostAlvo = input('Host ou IP: ')
    portaAlvo = input('porta alvo: ')
    try:
        s.connect((hostAlvo, int(portaAlvo)))
        print("Cliente Conectado!!! \n")
        s.shutdown(5)

    except socket.error as e:
        print('Erro de conecxão \n' + hostAlvo)
        print('\n erro:{}'.format(e))
        sys.exit()


if __name__ == '__main__':
    tcp_cliente()
