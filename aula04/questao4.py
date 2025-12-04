# Crie uma função que combine duas listas em tuplas contendo os dois valores e sua soma; trate erros e sinalize listas de tamanhos diferentes.

def soma_listas(lista1, lista2):
    try:
        if len(lista1) == len(lista2):
            dados = [(lista1[i], lista2[i], lista1[i]+lista2[i]) for i in range(len(lista1))]
        else:
            raise IndexError('A quantidade de elementos em cada lista é diferente.')
    except Exception as e:
        print(type(e), f'Erro: {e}')
    else:
        return dados  