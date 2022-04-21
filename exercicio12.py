import this
this.numConta = 0
this.saldo = 0
this.debito = 0
this.credito = 0
this.saldoAtual = 0


def coletarNumeroConta():
    print('Informe o numero da conta: ')
    this.numConta = float(input())

def coletarSaldo():
     print('Informe o saldo: ')
     this.saldo = float(input())

def coletarDebito():
     print('Informe o debito: ')
     this.debito = float(input())

def coletarcredito():
     print('Informe o credito: ')
     this.credito = float(input())

def calcular():
    coletarNumeroConta()
    coletarcredito()
    coletarDebito()
    coletarSaldo()
    this.saldoAtual = this.saldo - this.debito + this.credito
    if this.saldoAtual >= 0:
        print("Saldo Positivo")
    else:
        print("Saldo Negativo")

def mostrarResultado():
    calcular()

    print("O saldo na sua conta é" + str(this.saldoAtual))