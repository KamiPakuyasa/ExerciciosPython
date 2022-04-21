import this
this.valor = 0
this.salario = 0
this.total = 0

def coletarSalario():
    print('Informe o salario: ')
    this.salario = float(input())
    if this.salario >= 1500:
        this.valor = this.salario * 1.05
    else:
        this.valor = this.salario * 1.03

def mostrarResultado():
     coletarSalario()
     print("O valor novo salario é" + str(this.valor))