import os # Biblioteca que integra os programas e recursos do Sistema Operacional

def ping_simples(ping):
    ip = ping
    os.system('ping -n 8 {}'.format(ip))

if __name__ == "__main__":
    print(ping_simples('www.google.com'))