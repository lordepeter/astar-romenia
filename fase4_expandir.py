
# -*- coding: utf-8 -*-
# fase4_expandir.py — Fase 4: função de expansão e cidades exploradas.
# Rode com: python fase4_expandir.py

# ----- PASSO 1: importar os dados -----
from mapa import mapa_romenia, heuristica_bucareste


# ----- PASSO 2: mostrar a fronteira de forma resumida -----
def mostrar_fronteira(fronteira):
    """Exibe as cidades da fronteira e seus custos estimados."""
    partes = []

    for f, g, cidade, caminho in fronteira:
        partes.append(f'{cidade}(f={f})')

    print('   Nós disponíveis para expansão:', ', '.join(partes))


# ----- PASSO 3: criar uma função para expandir um nó -----
def expandir(no, explorados):
    """Gera os nós filhos, ignorando cidades já exploradas."""
    f_atual, g_atual, cidade_atual, caminho = no
    filhos = []

    for vizinho, custo_estrada in mapa_romenia[cidade_atual]:

        if vizinho in explorados:
            continue

        novo_g = g_atual + custo_estrada
        novo_f = novo_g + heuristica_bucareste[vizinho]

        filhos.append((novo_f, novo_g, vizinho, caminho + [vizinho]))

    return filhos


# ----- PASSO 4: preparar a fronteira e os explorados -----
inicio = 'Arad'

fronteira = [(heuristica_bucareste[inicio], 0, inicio, [inicio])]
explorados = set()


# ----- PASSO 5: realizar três rodadas de expansão -----
for rodada in [1, 2, 3]:

    fronteira.sort(key=lambda no: no[0])
    no = fronteira.pop(0)

    cidade = no[2]
    explorados.add(cidade)

    print(f'Rodada {rodada}: expandindo {cidade} '
          f'(Custo estimado: {no[0]} km | Custo real: {no[1]} km)')

    fronteira = fronteira + expandir(no, explorados)

    mostrar_fronteira(fronteira)

    print('   Cidades já processadas:', sorted(explorados))
    print()
