import this
ano = 0
meses = 0
dias = 0

def coletarAno():
    print('Informe quantos anos: ')
    this.ano = float(input())
   #metodo para coletar algo

def coletarMeses():
    print('Informe quantos meses: ')
    this.meses = float(input())


def coletarDias():
    print('Informe quantos dias: ')
    this.dias = float(input())

def Dia(ano,meses,dias):
    return this.ano * 365 + this.meses * 30 + this.dias * 1

def mostrarResultado():
    coletarAno()
    coletarMeses()
    coletarDias()

    print("Sua idade em dias é :" + str(Dia(this.ano, this.meses, this.dias)))