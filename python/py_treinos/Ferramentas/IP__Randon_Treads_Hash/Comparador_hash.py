import hashlib
def comparador(arq1, arq2):
    arquivo1 = arq1
    arquivo2 = arq2

    hash1 = hashlib.new('ripemd160')
    hash1.update(open(arquivo1, 'rb').read())

    hash2 = hashlib.new('ripemd160')
    hash2.update(open(arquivo2, 'rb').read())

    if hash1.digest() != hash2.digest():
        print(f'O arquivo: {arquivo1} é diferente do arquivo: {arquivo2}')
    else:
        print(f'Arquivo: {arquivo1} é igual ao arquivo: {arquivo2}')

'''
def gerador(txt):
    resultado = hashlib.md5(txt.encode('utf-8'))
    return (resultado.hexdigest)


if __name__ == "__main__":

    resul = gerador("kakakaka")
    print(resul)

    comparador('a.txt','b.txt')
'''