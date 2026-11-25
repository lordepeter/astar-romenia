
from fase4_expandir import expandir, mostrar_fronteira
from mapa import heuristica_bucareste

inicio = 'Arad'
fronteira = [(heuristica_bucareste[inicio], 0, inicio, [inicio])]
explorados = set()

print()
print('--- Desafio da Fase 4: seis rodadas ---')

for rodada in range(1, 7):

    fronteira.sort(key=lambda no: no[0])
    no = fronteira.pop(0)

    cidade = no[2]
    explorados.add(cidade)

    print(f'Rodada {rodada}: expandindo {cidade} '
          f'(f={no[0]}, g={no[1]})')

    fronteira = fronteira + expandir(no, explorados)

    mostrar_fronteira(fronteira)
    print('Cidades já processadas:', sorted(explorados))
    print()
