# Construa um dicionário unindo meses como chaves e despesas como valores usando dict comprehension.
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]

dicionario = {meses[i]: despesa[i] for i in range(len(meses))}
print(dicionario)