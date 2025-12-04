# Crie um programa que solicite o número total de participantes de um sorteio ao usuário. O programa deve, então, sortear e exibir um número inteiro aleatório entre 1 e o total de participantes.

from random import randint

total_participantes = int(input("Digite a quantidade total de participantes do sorteio: "))

print(f"O número sorteado foi: {randint(1, total_participantes)}")