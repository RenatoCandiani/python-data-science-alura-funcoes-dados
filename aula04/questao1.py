# Peça dois números float, tente dividir o primeiro pelo segundo e mostre o tipo do erro caso a operação falhe.

try:
    num1 = float(input())
    num2 = float(input())
    divisao = num1 / num2
except Exception as e:
    print(type(e), f'Erro: {e}')