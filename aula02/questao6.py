# Questão 6:
# Criar função que receba 4 notas e retorne:
# - maior nota
# - menor nota
# - média
# - situação (Aprovado(a) ou Reprovado(a))

notas = []

for i in range(1,5):
    nota = float(input(f"Digite a {i}ª nota: "))
    notas.append(nota)

def cadastro(lista):
    maior = max(lista)
    menor = min(lista)
    media = sum(lista) / len(lista)

    if media >= 6:
        situacao = "Aprovado(a)"
    else:
        situacao = "Reprovado(a)"

    return(media, maior, menor, situacao)
    
media, maior, menor, situacao = cadastro(notas)

print(f"O(a) aluno(a) está {situacao} com média {media:.2f}, maior nota {maior} e menor nota {menor}.")

