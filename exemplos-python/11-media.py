
import os

os.system("cls")

print("""
      
██████╗░░█████╗░██╗░░░░░███████╗████████╗██╗███╗░░░███╗
██╔══██╗██╔══██╗██║░░░░░██╔════╝╚══██╔══╝██║████╗░████║
██████╦╝██║░░██║██║░░░░░█████╗░░░░░██║░░░██║██╔████╔██║
██╔══██╗██║░░██║██║░░░░░██╔══╝░░░░░██║░░░██║██║╚██╔╝██║
██████╦╝╚█████╔╝███████╗███████╗░░░██║░░░██║██║░╚═╝░██║
╚═════╝░░╚════╝░╚══════╝╚══════╝░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝
      """)

nome = input("Digite o nome do aluno: ")
nota01 = float(input("Digite a primeira nota: "))
nota02 = float(input("Digite a segunda nota: "))
nota03 = float(input("Digite a terceira nota: "))

media = (nota01 + nota02 + nota03) / 3

#Mostrando a média
print(f"Sua média foi {round(media,2)}")

#Verificando se o aluno está aprovado
if media >=7:
    print("Aprovado")
elif media >=4:
    print("Recuperação")
else: 
    print("Reprovado")   

input("Pressione qualquer <Enter> para fecha o programa.")
