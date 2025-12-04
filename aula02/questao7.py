# Questão 7:
# Juntar duas listas (nomes e sobrenomes) formando nomes completos.
# Padronizar letras e usar map() para o mapeamento.

nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

nome_completo = map(lambda nome, sobrenome: f'{nome.title()} {sobrenome.title()}', nomes, sobrenomes)

for n in nome_completo:
    print(f"Nome completo: {n}")