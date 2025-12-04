# Avalie listas de respostas, valide alternativas e lance erro para opção inválida; se válido, calcule e retorne as notas.

gabarito = ['D', 'A', 'B', 'C', 'A']
def corretor(testes: list):
  pontuacoes = []
  try:
    for teste in testes:
      nota = 0 
      for i in range(len(teste)):
        if teste[i] not in ['A', 'B', 'C', 'D']:
          raise ValueError(f'A alternativa {teste[i]} não é uma opção de alternativa válida')
        elif teste[i] == gabarito[i]: 
          nota += 1
      pontuacoes.append(nota)
  except Exception as e:
    print(e)
  else:
    return pontuacoes 
  

testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
corretor(testes_sem_ex)

testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]
corretor(testes_com_ex)