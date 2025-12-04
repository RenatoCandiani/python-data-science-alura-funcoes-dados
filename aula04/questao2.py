# Solicite um nome, tente buscar a chave no dicionário e trate KeyError mostrando "Nome não encontrado".

try:
    chave = input()
    valor = idades[chave]
except KeyError:
    print('Nome não encontrado')
else:
    print(valor)