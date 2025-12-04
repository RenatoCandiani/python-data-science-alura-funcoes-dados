# Monte uma lista de tuplas onde cada tupla guarda o índice original e o nome correspondente.

lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

lista = []
for tupla in lista_de_tuplas:
    lista.append(tupla[0])

lista_de_tuplas = []
for i in range(len(lista)):
    lista_de_tuplas.append((i, lista[i]))
print(lista_de_tuplas)