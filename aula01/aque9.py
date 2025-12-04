# Calcule a raiz quadrada de cada número na lista:
# numeros = [2, 8, 15, 23, 91, 112, 256]
#
# Identifique e informe quais números originais têm raízes quadradas
# que resultam em um número inteiro, listando seus respectivos valores de raiz.

from math import sqrt

numeros = [2, 8, 15, 23, 91, 112, 256]

raizes_inteiras = []

for numero in numeros:
    raizes_inteiras.append(sqrt(numero))

for i in range(len(raizes_inteiras)):
    if raizes_inteiras[i] / 1 == raizes_inteiras[i]:
        print(f"O número {numeros[i]} tem raiz quadrada inteira: {raizes_inteiras[i]}")