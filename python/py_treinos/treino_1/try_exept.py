lista = [1, 10]

try:
    divisao = 10/0
    nunber = lista[2]
    x = a
except ZeroDivisionError:
    print("não da pra dividir Zero mano")
except IndexError:
    print('Não tem tantas opções na lista mano')
except BaseException as ex:
    print('erro desconhecido mano. Erro: {}'.format(ex))

else:
    print('a vida continua')

finally:
    print('sempre chega no finally')