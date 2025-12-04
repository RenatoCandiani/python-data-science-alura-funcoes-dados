# Solicite o raio de um jardim circular ao usuário. Com o preço da grama
# a R$ 25,00 por metro quadrado, calcule e devolva o custo total
# para cobrir a área circular com grama. (Use pi para o cálculo da área: A = pi * r^2)

from math import pi, pow

raio = float(input("Digite o radio do jardim circular em m²: "))

area = pi*pow(raio,2)
valor = area*25

print(f"A área do jardim é de {area:.2f} m²")
print(f"O custo total para cobrir a área do jardim com grama é de R$ {valor:.2f}")