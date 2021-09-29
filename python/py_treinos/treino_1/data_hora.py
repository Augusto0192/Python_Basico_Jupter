from datetime import date, time, datetime, timedelta
def data():
    data_atual = date.today()
    print(data_atual.strftime('%d - %m - %Y %A %B' ))


def tempo():
    horario = time(hour=15, minute=18, second=45)
    print(horario.strftime('%H:%M:%S'))
    print

def data_hora():
    agora = datetime.now()
    tupla = ('segunda', 'Teça', 'quarta', 'quinta', 'sexta', 'sabádo', 'domingo')
    print(tupla[agora.weekday()])
    print(agora.strftime('%c' ))
    novadata= agora- timedelta(days= 365)
    print(novadata)


if __name__ == '__main__':
  #  tempo()
    data_hora()

