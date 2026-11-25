
from fase2_caminhos import custo_do_caminho, mostrar_g_h_f

# Desafio 1: calcular o custo de um caminho alternativo

caminho_alternativo = [
    'Arad', 'Timisoara', 'Lugoj', 'Mehadia',
    'Drobeta', 'Craiova', 'Pitesti', 'Bucharest'
]

print()
print('--- Desafios da Fase 2 ---')

print('Rota alternativa:', ' -> '.join(caminho_alternativo))
print('Distância total da rota:', custo_do_caminho(caminho_alternativo), 'km')

# Desafio 2: analisar os valores de g, h e f

print()
print('Custos acumulados e estimados da rota alternativa:')
mostrar_g_h_f(caminho_alternativo)
