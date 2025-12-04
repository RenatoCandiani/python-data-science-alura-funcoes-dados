# Desenvolva divide_colunas para dividir pressão por temperatura, validando tamanhos iguais e ausência de zeros.

def divide_colunas(lista_1: list, lista_2: list) -> list:
   
  try:
    if len(lista_1) != len(lista_2): # Verificando se as listas tem o mesmo tamanho, se não lança uma exceção
      raise ValueError("As listas precisam ter o mesmo tamanho")

    resultado = [round(a / b, 2) for a, b in zip(lista_1, lista_2)] 
  except ValueError as e:
    print(e)
  except ZeroDivisionError as e:
    print(f"{e}: A 2ª lista não pode possuir um valor igual a 0")
  else:
    return resultado
  
pressoes = [60, 120, 140, 160, 180]
temperaturas = [0, 25, 30, 35, 40]

divide_colunas(pressoes, temperaturas)

pressoes = [100, 120, 140, 160]
temperaturas = [20, 25, 30, 35, 40]

divide_colunas(pressoes, temperaturas)