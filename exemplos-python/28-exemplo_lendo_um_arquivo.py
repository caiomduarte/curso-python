

import os

os.system("cls")

print("=== LENDO DADOS DE UM ARQUIVO ===\n")

input("Pressione a tecla <enter> para continuar...")

os.system("cls")

#Acessando o arquivo para ler os dados
with open("produtos.txt", "r", encoding="utf-8") as arquivo:
    print("=== Dados do arquivo ===\n")
    
    #Utilizando o print e o read para exibir os dados
    #print(arquivo.read()) 
    
    #Lendo Linha por Linha do arquivo
    for linha in arquivo:
        print(f"Conteúdo da Linha: {linha.strip()}") 
       

input("Pressione a tecla <enter> para encerrar...")