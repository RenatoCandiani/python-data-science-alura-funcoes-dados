# Selecione 3 frutas aleatórias e únicas da lista fornecida abaixo
# e exiba a seleção.
#
# frutas = ["maçã", "banana", "uva", "pêra", 
#           "manga", "coco", "melancia", "mamão",
#           "laranja", "abacaxi", "kiwi", "ameixa"]

from random import choices

frutas = ["maçã", "banana", "uva", "pêra","manga", "coco", "melancia", "mamão", "laranja", "abacaxi", "kiwi", "ameixa"]

salada = choices(frutas, k=3)

print(f"As frutas selecionadas para a salada surpresa são: {salada[0]}, {salada[1]} e {salada[2]}")