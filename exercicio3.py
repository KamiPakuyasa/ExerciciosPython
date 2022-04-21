import this

this.num1 = 0
this.num2 = 0


def coletarA():
    print('Informe a base: ')
    this.num1 = float(input())
   #metodo para coletar algo

def coletarB():
    print('Informe a altura: ')
    this.num2 = float(input())
   #metodo para coletar algo

def multiplicar(num1,num2):
    return this.num1 * this.num2

def mostrarResultado():
    coletarA()
    coletarB()

    print("A area do retangulo é::" + str(multiplicar(this.num1, this.num2)))