# Questão 9:
# Criar 3 funções:
# - gasto_hotel
# - gasto_gasolina
# - gasto_passeio
# Simular viagem de 3 dias para Salvador considerando ida e volta.

dias = int(input("Quantas diárias? "))
cidade = input("Qual a cidade? [Salvador, Fortaleza, Natal ou Aracaju]: ")
distancias = [850, 800, 300, 550]
passeio = [200, 400, 250, 300]
km_l = 14
gasolina = 5

def gasto_hotel(dias):
    return 150 * dias

def gasto_gasolina(cidade):
    if cidade == "Salvador":
        return (2 * distancias[0] * gasolina) / km_l 
    elif cidade == "Fortaleza":
        return (2 * distancias[1] * gasolina) / km_l 
    elif cidade == "Natal":
        return (2 * distancias[2] * gasolina) / km_l 
    elif cidade == "Aracaju":
        return (2 * distancias[3] * gasolina) / km_l 

def gasto_passeio(cidade, dias):
    if cidade=="Salvador":
        return passeio[0] * dias
    elif cidade=="Fortaleza":
        return passeio[1] * dias
    elif cidade=="Natal":
        return passeio[2] * dias 
    elif cidade=="Aracaju":
        return passeio[3] * dias 

gastos = gasto_hotel(dias) + gasto_gasolina(cidade) + gasto_passeio(cidade, dias)
print(f"Com base nos gastos definidos, uma viagem de {dias} dias para {cidade} saindo de Recife custaria {round(gastos, 2)} reais")