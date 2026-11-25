from mapa import mapa_romenia, heuristica_bucareste

def custo_da_estrada(origem, destino):
    for vizinho, custo in mapa_romenia[origem]:
        if vizinho == destino:
            return custo
    return None

def custo_do_caminho(caminho):
    total = 0

    for i in range(len(caminho) - 1):
        total = total + custo_da_estrada(caminho[i], caminho[i + 1])

    return total

print('Distância da estrada entre Arad e Sibiu:',
      custo_da_estrada('Arad', 'Sibiu'), 'km')

print('Conexão direta entre Arad e Bucareste:',
      custo_da_estrada('Arad', 'Bucharest'),
      '(estrada inexistente)')

por_fagaras = ['Arad', 'Sibiu', 'Fagaras', 'Bucharest']

por_pitesti = ['Arad', 'Sibiu', 'Rimnicu Vilcea',
               'Pitesti', 'Bucharest']

print()
print('Primeira rota - passando por Fagaras:')
print(' -> '.join(por_fagaras))
print('Distância total:', custo_do_caminho(por_fagaras), 'km')

print()
print('Segunda rota - passando por Pitesti:')
print(' -> '.join(por_pitesti))
print('Distância total:', custo_do_caminho(por_pitesti), 'km')

def mostrar_g_h_f(caminho):
    print(f'{"Cidade":<15} {"g(n)":>5} {"h(n)":>5} {"f(n)":>5}')

    for i in range(len(caminho)):
        cidade = caminho[i]
        g = custo_do_caminho(caminho[:i + 1])
        h = heuristica_bucareste[cidade]
        f = g + h

        print(f'{cidade:<15} {g:>5} {h:>5} {f:>5}')

print()
print('Análise dos custos e estimativas da rota por Fagaras:')
mostrar_g_h_f(por_fagaras)

print()
print('Análise dos custos e estimativas da rota por Pitesti:')
mostrar_g_h_f(por_pitesti)
