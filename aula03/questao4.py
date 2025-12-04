# Use list comprehension para coletar somente os valores associados a 'Apartamento' nas tuplas.

aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

lista = [tupla[1] for tupla in aluguel if tupla[0] == "Apartamento"]
print(lista)