def escrever(nome, txt):
    arquivo = open(nome, 'a')
    arquivo.writelines(txt)
    arquivo.close()



def media_nota(nome_arquivo):
    arquivo= open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)
    lista_media=[]
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        media = lambda notas: sum([int(i) for i in notas])/4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

    
def copia(nome):
    import shutil
    shutil.copy(nome, 'C:/Users/SAMSUNG/Documents/')

if __name__ =='__main__':

    '''
    lista_media = media_nota('Notas.txt')
    print(lista_media)
    '''
    copia('Notas.txt')