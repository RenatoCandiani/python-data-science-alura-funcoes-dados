# Questão 10:
# Receber uma frase e filtrar palavras com 5+ caracteres usando lambda + filter().
# Remover .,?! antes da filtragem.

frase = input("Digite uma frase: ")
frase = frase.replace(',',' ').replace('.',' ').replace('!',' ').replace('?',' ').split()

tamanho = list(filter(lambda x: len(x) >= 5, frase))
print(tamanho)