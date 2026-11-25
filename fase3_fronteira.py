
# -*- coding: utf-8 -*-
# fase3_fronteira.py — Fase 3: criação de nós e expansão manual.
# Rode com: python fase3_fronteira.py

# ----- PASSO 1: importar os dados -----
from mapa import mapa_romenia, heuristica_bucareste


# ----- PASSO 2: montar o nó inicial e a fronteira -----
# Estrutura do nó: (f, g, cidade, caminho)

inicio = 'Arad'
g = 0
h = heuristica_bucareste[inicio]
no_inicial = (g + h, g, inicio, [inicio])

fronteira = [no_inicial]

print('Nós disponíveis no início da busca:', fronteira)


# ----- PASSO 3: retirar o primeiro nó da fronteira -----
no = fronteira.pop(0)
f_atual, g_atual, cidade_atual, caminho = no

print()
print('Nó selecionado para processamento:', no)

print(' Custo estimado (f) =', f_atual,
      '| Custo percorrido (g) =', g_atual,
      '| Cidade atual =', cidade_atual,
      '| Rota percorrida =', caminho)

print('Nós restantes após a remoção:', fronteira)


# ----- PASSO 4: gerar os filhos do nó selecionado -----
for vizinho, custo_estrada in mapa_romenia[cidade_atual]:
    novo_g = g_atual + custo_estrada
    novo_h = heuristica_bucareste[vizinho]
    novo_f = novo_g + novo_h
    novo_caminho = caminho + [vizinho]

    fronteira.append((novo_f, novo_g, vizinho, novo_caminho))

print()
print('Novas possibilidades de caminho a partir de Arad:')
for item in fronteira:
    print(' ', item)


# ----- PASSO 5: ordenar a fronteira pelo custo estimado -----
fronteira.sort(key=lambda no: no[0])

print()
print('Nós organizados do menor para o maior custo estimado (f):')
for item in fronteira:
    print(' ', item)


# ----- PASSO 6: selecionar o próximo nó -----
proximo = fronteira.pop(0)

print()
print('Próxima cidade prioritária:', proximo[2],
      'com custo total estimado de', proximo[0], 'km')
