# Questão 5:
# Ler 5 notas, remover a maior e a menor, e calcular a média das 3 restantes.
# Retornar a média final.

notas =  []

for i in range(1, 6):
    nota = float(input(f"Digite a {i}° nota: "))
    notas.append(nota)

def media(lista):
    lista.remove(max(lista))
    lista.remove(min(lista))
    return sum(lista) / len(lista)

media = media(notas)
print(f"Nota da manobra: {round(media, 1)}")