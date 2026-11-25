# -*- coding: utf-8 -*-
# fase1_explorar.py — Fase 1: navegar nos dados, sem nenhuma busca ainda.
# Rode com: python fase1_explorar.py

# ----- PASSO 1: trazer os dados do arquivo mapa.py -----
from mapa import mapa_romenia, heuristica_bucareste

# ----- PASSO 2: quantas cidades existem? -----
print('Total de cidades cadastradas:', len(mapa_romenia))
print('Total de cidades com heurística:', len(heuristica_bucareste))

# ----- PASSO 3: olhar o valor guardado em uma chave -----
vizinhos_arad = mapa_romenia['Arad']
print()
print('Conexões rodoviárias disponíveis em Arad:', vizinhos_arad)
print('Estrutura que armazena os vizinhos:', type(vizinhos_arad))
print('Estrutura utilizada para armazenar o mapa:', type(mapa_romenia))

# ----- PASSO 4: pegar uma tupla e as partes dela -----
primeira = vizinhos_arad[0]
print()
print('Primeira conexão registrada:', primeira)
print('Cidade de destino da conexão:', primeira[0])
print('Distância até a cidade vizinha:', primeira[1], 'km')

# ----- PASSO 5: percorrer a lista com for e desempacotar -----
print()
print('Rotas diretas partindo de Arad:')

for vizinho, custo in mapa_romenia['Arad']:
    print(f'De Arad até {vizinho}: {custo} km')

# ----- PASSO 6: percorrer o mapa inteiro -----
print()
print('Quantidade de conexões por cidade:')

for cidade in mapa_romenia:
    quantidade = len(mapa_romenia[cidade])
    print(f'{cidade:<15} possui {quantidade} conexão(ões)')

# ----- PASSO 7: consultar a heurística -----
print()
print('Distância estimada de Arad até Bucareste:',
      heuristica_bucareste['Arad'], 'km')

print('Comparação entre distância real e estimativa restante:')

for vizinho, custo in mapa_romenia['Arad']:
    h = heuristica_bucareste[vizinho]
    print(f'{vizinho:<10} | Estrada: {custo:>3} km | Heurística: {h:>3} km')
