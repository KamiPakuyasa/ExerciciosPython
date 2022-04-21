import this
this.notaA = 0
this.notaB = 0
this.notaC = 0

def coletarA():
    print('Informe a primeira nota: ')
    this.notaA = float(input())

def coletarB():
     print('Informe a segunda nota: ')
     this.notaB = float(input())

def coletarC():
     print('Informe a terceira nota: ')
     this.notaC = float(input())

def Media():

    return float((this.notaA  + this.notaB + this.notaC) / 3)

def mostrarResultado():
    coletarA()
    coletarB()
    coletarC()
    print("Sua Media é :" + str(Media()))