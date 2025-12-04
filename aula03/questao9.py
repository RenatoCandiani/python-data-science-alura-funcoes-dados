# Crie um dicionário que conte quantas vezes cada Estado aparece na lista, usando dict comprehension.

estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG']

estados_unicos = list(set(estados))

lista_de_listas = []
for estado in estados_unicos:
    lista = [uf for uf in estados if uf == estado]
    lista_de_listas.append(lista)
print(lista_de_listas)

contagem_valores = {estados_unicos[i]: len(lista_de_listas[i]) for i in range(len(estados_unicos))}
print(contagem_valores)