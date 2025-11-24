
#1 passo - importar a biblioteca os
import os

#2 passo - Utilizar a os para limpar a tela
os.system("cls")

#3 passo - Realizar as entradas
#TEXTO = STRING = STR
nome  = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))


#4 passo - Verificar a idade do usuário
if idade >=18:
    possui_carteira = input("Possui carteira de motorista? \n (1-Sim | 2-Não):")

    if possui_carteira == "1":
        print("Pode dirigir!")
    else:
        print("Não pode dirigir!")
else:
    print("Menor de idade")