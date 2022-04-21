import this #Ele demonstra que é a msm variavel

import exercicio1
import exercicio11
import exercicio12
import exercicio2
import exercicio3
import exercicio4
import exercicio5
import exercicio6
import exercicio7
import exercicio8
import exercicio9

this.opcao = 0#Crio a variável global
valorA = 0
valorB = 0
num1 = 0
num2 = 1


def mostrarMenu():
    print('Escolha uma das opções abaixo\n' +
          '\n1. Exercicio1' +
          '\n2. Exercicio2' +
          '\n3. Exercicio3' +
          '\n4. Exercicio4' +
          '\n5. Exercicio5' +
          '\n6. Exercicio6' +
          '\n7. Exercicio7' +
          '\n8. Exercicio8' +
          '\n9. Exercicio9' +
          '\n11. Exercicio11' +
          '\n11. Exercicio12' +
          '\n0. Sair')

    this.opcao = int(input()) #Coletar a digitaçaõ do usuário
def operacao():

    mostrarMenu()
    if this.opcao == 1:
        print(exercicio1.mostrarResultado())
    if this.opcao == 2:
        print(exercicio2.mostrarResultado())
    if this.opcao == 3:
        print(exercicio3.mostrarResultado())
    if this.opcao == 4:
        print(exercicio4.mostrarResultado())
    if this.opcao == 5:
        print(exercicio5.mostrarResultado())
    if this.opcao == 6:
        print(exercicio6.mostrarResultado())
    if this.opcao == 7:
        print(exercicio7.mostrarResultado())
    if this.opcao == 8:
        print(exercicio8.mostrarResultado())
    if this.opcao == 9:
        print(exercicio9.mostrarResultado())
    if this.opcao == 11:
        print(exercicio11.mostrarResultado())
    if this.opcao == 12:
        print(exercicio12.mostrarResultado())