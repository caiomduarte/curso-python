
import os

os.system("cls")

print("Exemplos de tratamento de exceções")

try:

    comando = "print('teste'"

    exec(comando)

    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    resultado  = numero1 / numero2
    print(f"O resultado da divisão é {resultado}")

except ValueError as erro:
    print(f"Aconteceu o erro {erro}")
    print("Você digitou um valor ínvalido")    


