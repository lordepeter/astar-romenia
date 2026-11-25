
# -*- coding: utf-8 -*-
# fase5_busca.py — Fase 5: implementação da busca A*.
# Rode com: python fase5_busca.py

# ----- PASSO 1: importar os dados -----
from mapa import mapa_romenia, heuristica_bucareste


# ----- PASSO 2: implementar a busca A* -----
def busca_a_estrela(inicio, objetivo):
    """Retorna o melhor caminho e seu custo, ou None e infinito."""

    fronteira = [(heuristica_bucareste[inicio], 0, inicio, [inicio])]
    explorados = set()

    while fronteira:

        # Seleciona o nó com menor custo estimado
        fronteira.sort(key=lambda no: no[0])
        f_atual, g_atual, cidade_atual, caminho = fronteira.pop(0)

        # Verifica se o objetivo foi alcançado
        if cidade_atual == objetivo:
            return caminho, g_atual

        # Ignora cidades que já foram exploradas
        if cidade_atual in explorados:
            continue

        explorados.add(cidade_atual)

        # Gera novos nós a partir dos vizinhos
        for vizinho, custo_estrada in mapa_romenia[cidade_atual]:

            if vizinho not in explorados:

                novo_g = g_atual + custo_estrada
                novo_f = novo_g + heuristica_bucareste[vizinho]

                fronteira.append(
                    (novo_f, novo_g, vizinho, caminho + [vizinho])
                )

    return None, float('inf')


# ----- PASSO 3: executar a busca e apresentar o resultado -----
caminho, custo = busca_a_estrela('Arad', 'Bucharest')

print('Rota de menor custo encontrada pelo A*:', ' -> '.join(caminho))
print('Distância real total do percurso:', custo, 'km')
print('Quantidade de estradas percorridas:', len(caminho) - 1)
