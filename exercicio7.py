import this
this.carro = 0

def coletarCarro():
    print('Informe o valor do carro: ')
    this.carro = float(input())

def Ajuste():
    coletarCarro()
    return float(this.carro + (this.carro * 1.73))


def mostrarResultado():
    print("O valor final do carro sera: " + str(Ajuste()))