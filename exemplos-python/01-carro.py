#Utilizado para executar comandos no cmd
import os

#Limpando a Tela
os.system("cls")

nome_carro = input("Digite o nome o carro: ")
valor_carro = float(input("Digite o valor do carro: "))
consumo_por_litro = float(input("Digite o consumo por litro: "))

print("--------------------------------------------------")
print("| Carro: ", nome_carro)
print("| Valor: ", valor_carro)
print("| Consumo por litro: ", consumo_por_litro)