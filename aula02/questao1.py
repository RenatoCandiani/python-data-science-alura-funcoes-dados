# Questão 1:
# Ler a lista dada e calcular:
# - tamanho da lista
# - maior valor
# - menor valor
# - soma dos valores
# Exibir mensagem final com esses dados.

lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

tam = len(lista)
maior = max(lista)
min = min(lista)
soma = sum(lista)

print(f"Tamanho da lista: {tam}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {min}")
print(f"Soma dos valores: {soma}")