import this

this.valor = 0
this.num1 = 0


def coletar():
    print('Informe o numero: ')
    this.num1 = float(input())
   #metodo para coletar algo

def subtrair():
        return this.num1 - 1

def mostrarResultado():
    coletar()
    subtrair()
    print("Seu antecessor é:" + str(subtrair()))