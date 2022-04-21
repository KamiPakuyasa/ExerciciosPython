import this
valorA = 10
valorB = 20
valorC = 0

def coletarA():
    print('Informe o valor A: ')
    this.valorA = float(input())
   #metodo para coletar algo

def coletarB():
    print('Informe o valor B: ')
    this.valorB = float(input())

def trocar():
    this.valorC = this.valorA
    this.valorA = this.valorB
    this.valorB = this.valorC

def mostrarResultado():
    coletarA()
    coletarB()
    trocar()
    print("Resultado final de A:" + str(this.valorA) + "\nResultado final de B:" + str(this.valorB))