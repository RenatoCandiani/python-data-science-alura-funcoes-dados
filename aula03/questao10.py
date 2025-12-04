# A partir de tuplas (Estado, colaboradores), gere um dicionário com listas por Estado e outro com a soma total por Estado.

funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]

estados_unicos = list(set([tupla[0] for tupla in funcionarios]))

lista_de_listas = []
for estado in estados_unicos:
    lista = [tupla[1] for tupla in funcionarios if tupla[0] == estado]
    lista_de_listas.append(lista)
print(lista_de_listas)

agrrupamento_por_estado = {estados_unicos[i]: lista_de_listas[i] for i in range(len(estados_unicos))}
print(agrrupamento_por_estado)

soma_por_estado = {estados_unicos[i]: sum(lista_de_listas[i]) for i in range(len(estados_unicos))}
print(soma_por_estado)