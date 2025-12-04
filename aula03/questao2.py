# Crie uma lista contendo apenas o terceiro item de cada tupla fornecida.
lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

lista = []
for tupla in lista_de_tuplas:
    lista.append(tupla[2])
print(lista)