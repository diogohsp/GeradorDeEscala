import random
from datetime import datetime, timedelta

def sortear_numeros(qtd_numeros, numeros_disponiveis):
    if len(numeros_disponiveis) < qtd_numeros:
        numeros_disponiveis.extend(numeros_gerais)
        random.shuffle(numeros_disponiveis)

    numeros_sorteados = []
    for _ in range(qtd_numeros):
        numero = numeros_disponiveis.pop()
        while numero in monitores_gerais:
            numero = numeros_disponiveis.pop()
        numeros_sorteados.append(numero)

    return numeros_sorteados

def sortear_monitor(qtd_numeros, monitores_disponiveis):
    monitores_sorteados = []
    while len(monitores_sorteados) < qtd_numeros:
        if len(monitores_disponiveis) < qtd_numeros:
            monitores_disponiveis.extend(monitores_gerais)
            random.shuffle(monitores_disponiveis)

        monitor_sorteado = monitores_disponiveis.pop()
        while monitor_sorteado in monitores_sorteados:
            monitor_sorteado = monitores_disponiveis.pop()

        monitores_sorteados.append(monitor_sorteado)

    return monitores_sorteados

data = datetime.now()
data_limite = datetime(2023, 9, 27)
numeros_gerais = list(range(1, 101))
monitores_gerais = [1, 6, 18, 24, 36, 37, 45, 48, 49, 53, 66, 74, 76, 77, 78, 87, 89, 100]
numeros_sorteados_geral = list(numeros_gerais)  # a lista geral possui todos os números no início
numeros_monitores_geral = list(monitores_gerais)
random.shuffle(numeros_sorteados_geral)
random.shuffle(numeros_monitores_geral)

#armazenar os monitores sorteados e disponíveis
monitores_sorteados = []
monitores_disponiveis = list(numeros_monitores_geral)
ciclos = 0

while data < data_limite:
    data = data + timedelta(days=1)
    quantidade = 3
    quantidade_monitores = 1
    numeros_sorteados = sortear_numeros(quantidade, numeros_sorteados_geral)
    monitores_sorteio_atual = sortear_monitor(quantidade_monitores, monitores_disponiveis)

    #atualização a lista de monitores sorteados
    monitores_sorteados.extend(monitores_sorteio_atual)

    print("Monitor:", monitores_sorteio_atual, "Atiradores:", numeros_sorteados, data.date())

    #verificação se existem números repetidos
    numeros_unicos = set(numeros_sorteados_geral)
    if len(numeros_unicos) != len(numeros_sorteados_geral):
        print("Há números repetidos na lista de números sorteados.")
    else:
        print("Não há números repetidos na lista de números sorteados.")

    #verificação se um ciclo completo foi concluído
    if len(monitores_disponiveis) == 0:
        monitores_disponiveis = list(numeros_monitores_geral)  # reiniciar lista de monitores disponíveis
        ciclos += 1

print("Lista de atiradores disponíveis:", list(set(numeros_sorteados_geral) - set(monitores_gerais)))
print("Lista de monitores disponíveis:", monitores_disponiveis)
