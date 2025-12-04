# Crie uma função que detecte pontuação em palavras e lance ValueError no primeiro caso encontrado.
# criando a função que recebe a lista de palavras

def avalia_texto(texto: list):
    for palavra in texto:
        if ',' in palavra or '.' in palavra or '!' in palavra or '?' in palavra:
            raise ValueError(f'O texto apresenta pontuações na palavra "{palavra}".')
    return "Texto já tratado!"

# Testando no exemplo que não lança exceção
lista_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil',
                  'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial']

try:
  avaliacao = avalia_texto(lista_tratada)
except Exception as e:
  print(e)
else:
  print(avaliacao)

  # Testando no exemplo que lança exceção
lista_nao_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa,', 'versátil',
                  'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial!']

try:
  avaliacao = avalia_texto(lista_nao_tratada)
except Exception as e:
  print(e)
else:
  print(avaliacao)