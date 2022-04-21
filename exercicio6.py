import this

this.salario = 0
this.percentual = 0
this.novoSalario = 0
this.total = 0

def coletar():
    print("Informe o salario mensal:")
    this.salario = (int(input()))
    print("Informe o percentual de reajuste:")
    this.percentual = (int(input()))
def calcular():
    coletar()
    this.percentual / 100
    this.novoSalario = (this.salario * this.percentual)
    this.total = this.salario + this.novoSalario
def mostrarResultado():
    calcular()
    print("O novo Salario é: " + str(this.total))