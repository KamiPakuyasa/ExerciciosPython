import this
total = 0
branco = 0
nulos = 0
validos = 0

def coletarTotal():
    print('Informe o total de eleitores: ')
    this.total = float(input())
   #metodo para coletar algo

def coletarValidos():
    print('Informe quantos votos validos: ')
    this.validos = float(input())

def coletarBrancos():
    print('Informe quantos votos brancos: ')
    this.branco = float(input())

def coletarNulos():
    print('Informe quantos votos nulos: ')
    this.nulos = float(input())

def PorcentagemValidos(total,validos):
    return (this.validos / this.total)* 100

def PorcentagemBranco(total,branco):
    return (this.branco/ this.total) * 100

def PorcentagemNulos(total,nulos):
    return (this.nulos / this.total) * 100

def mostrarResultado():
    coletarTotal()
    coletarValidos()
    coletarBrancos()
    coletarNulos()

    print("A porcentagem de votos validos é :" + str(PorcentagemValidos(this.total,this.validos)) +"\nA porcentagem de votos brancos é :" + str(PorcentagemBranco(this.total,this.branco))
    + "\nA porcentagem de votos nulos é:" + str(PorcentagemNulos(this.total,this.nulos)))
