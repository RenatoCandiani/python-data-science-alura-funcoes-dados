# Crie um programa que solicite o nome do usuário. Em seguida, o programa deve gerar um token que seja um número par e esteja entre 1000 e 9998 (inclusive). Finalmente, exiba a seguinte mensagem, preenchendo as lacuna: "Olá, [nome], o seu token de acesso é [token]! Seja bem-vindo(a)!"

from random import randrange

nome = input("Digite seu nome: ")
token = randrange(1000, 9998, 2)

print(f"Olá, {nome}, o seu token de acesso é o token {token}! Seja bem-vindo(a)!")