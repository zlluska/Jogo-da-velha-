def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print('|'+'|'.join(linha)+'|')
        print()


def encontrar_caminho(tabuleiro, x, y, fim_x, fim_y, visitado, caminho_atual, melhor_caminho):
    n = len(tabuleiro)

    # Verifica se está fora do tabuleiro ou em posição inválida
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    if tabuleiro[x][y] == 'X' or visitado[x][y]:
        return
    if (x, y) in caminho_atual:
        return

    # Adiciona a posição atual no caminho
    caminho_atual.append((x, y))

    # Chegamos no destino!
    if x == fim_x and y == fim_y:
        if len(caminho_atual) < len(melhor_caminho[0]) or not melhor_caminho[0]:
            melhor_caminho[0] = list(caminho_atual)  # copia o caminho atual
        caminho_atual.pop()
        return

    # Marca como visitado
    visitado[x][y] = True

    # Tenta todas as 4 direções (cima, baixo, esquerda, direita)
    encontrar_caminho(tabuleiro, x+1, y, fim_x, fim_y, visitado, caminho_atual, melhor_caminho)
    encontrar_caminho(tabuleiro, x-1, y, fim_x, fim_y, visitado, caminho_atual, melhor_caminho)
    encontrar_caminho(tabuleiro, x, y+1, fim_x, fim_y, visitado, caminho_atual, melhor_caminho)
    encontrar_caminho(tabuleiro, x, y-1, fim_x, fim_y, visitado, caminho_atual, melhor_caminho)

    # Desmarca e faz backtrack
    visitado[x][y] = False
    caminho_atual.pop()


# ---------- Execução Principal ----------
tabuleiro = [
    [' ', ' ', 'X', ' '],
    ['X', ' ', 'X', ' '],
    [' ', ' ', ' ', ' '],
    [' ', 'X', 'X', ' ']
]

inicio = (0, 0)
fim = (3, 3)
n = len(tabuleiro)

visitado = [[False for _ in range(n)] for _ in range(n)]
melhor_caminho = [[]]

encontrar_caminho(tabuleiro, inicio[0], inicio[1], fim[0], fim[1], visitado, [], melhor_caminho)

# Marca o melhor caminho no tabuleiro
for x, y in melhor_caminho[0]:
    if (x, y) != inicio and (x, y) != fim:
        tabuleiro[x][y] = '*'

print("Melhor Caminho Encontrado:")
imprimir_tabuleiro(tabuleiro)
