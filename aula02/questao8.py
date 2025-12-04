# Questão 8:
# Criar função calcula_pontos que receba listas de gols marcados e sofridos.
# Calcular:
# - pontuação total (3 vitória, 1 empate, 0 derrota)
# - aproveitamento (%) em relação ao máximo possível

gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]

def calcula_pontos(gols_marcados, gols_sofridos):
    pontos = 0

    for i in range(len(gols_marcados)):
        if gols_marcados[i] > gols_sofridos[i]:
            pontos += 3  # Vitória
        elif gols_marcados[i] == gols_sofridos[i]:
            pontos += 1  # Empate
    aprov = 100 * pontos / (len(gols_marcados) * 3)
    return pontos, aprov

pontos, aprov = calcula_pontos(gols_marcados, gols_sofridos)
print(f'Pontuação total: {pontos} pontos')
print(f'Aproveitamento: {aprov:.2f}%')