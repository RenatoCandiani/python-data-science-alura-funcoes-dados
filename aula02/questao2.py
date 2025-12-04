# Questão 2:
# Criar uma função que receba um número e gere sua tabuada de 0 a 10.

num = int(input("Digite um número para ver sua tabuada: "))

def tabuada (numero: int):
    print(f"Tabuada do {numero}: ")
    for i in range(11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

tabuada(num)