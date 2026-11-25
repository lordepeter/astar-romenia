
from fase3_fronteira import fronteira, proximo
from mapa import mapa_romenia, heuristica_bucareste

# Desafio 1: expandir Sibiu manualmente

f_atual, g_atual, cidade_atual, caminho = proximo

for vizinho, custo_estrada in mapa_romenia[cidade_atual]:
    novo_g = g_atual + custo_estrada
    novo_h = heuristica_bucareste[vizinho]
    novo_f = novo_g + novo_h
    novo_caminho = caminho + [vizinho]

    fronteira.append((novo_f, novo_g, vizinho, novo_caminho))

fronteira.sort(key=lambda no: no[0])

print()
print('--- Desafios da Fase 3 ---')
print('Fronteira após a expansão de Sibiu:')

for item in fronteira:
    print(' ', item)


# Desafio 2: ordenar pelo custo real (g)

fronteira.sort(key=lambda no: no[1])

print()
print('Fronteira organizada pelo custo real acumulado:')

for item in fronteira:
    print(' ', item)

print('Cidade prioritária considerando apenas g:', fronteira[0][2])
