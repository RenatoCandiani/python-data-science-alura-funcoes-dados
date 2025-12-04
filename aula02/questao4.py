# Questão 4:
# Usar lambda + map() para gerar uma lista com os quadrados dos números de 1 a 10.

numeros = list(range(1, 11))

quadrado = lambda x: x ** 2

lista_quadrados = list(map(quadrado, numeros))
print(lista_quadrados)