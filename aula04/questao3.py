# Crie uma função que converta todos os itens de uma lista para float, trate erros e sempre exiba "Fim da execução da função".

def converte_lista(lista):
    try:
        nova_lista = [float(elemento) for elemento in lista]
    except Exception as e:
        print(type(e), f"Erro: {e}")
    else:
        return nova_lista
    finally:
        print("Fim da execução da função")
