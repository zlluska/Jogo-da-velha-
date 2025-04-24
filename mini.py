# Tabuleiro começa com 9 espaços vazios
tabuleiro = [" " for _ in range(9)]

# Mostra o tabuleiro formatado
def mostrar_tabuleiro():
    print()
    print(tabuleiro[0], "|", tabuleiro[1], "|", tabuleiro[2])
    print("--+---+--")
    print(tabuleiro[3], "|", tabuleiro[4], "|", tabuleiro[5])
    print("--+---+--")
    print(tabuleiro[6], "|", tabuleiro[7], "|", tabuleiro[8])
    print()

# Verifica se alguém venceu
def venceu(jogador):
    combinacoes = [
        [0,1,2], [3,4,5], [6,7,8],  # linhas
        [0,3,6], [1,4,7], [2,5,8],  # colunas
        [0,4,8], [2,4,6]            # diagonais
    ]
    for c in combinacoes:
        if tabuleiro[c[0]] == tabuleiro[c[1]] == tabuleiro[c[2]] == jogador:
            return True
    return False

# Verifica se deu empate
def empate():
    return " " not in tabuleiro

# Algoritmo de IA (Minimax)
def minimax(tab, profundidade, maximizando):
    if venceu("X"):
        return -10 + profundidade
    if venceu("O"):
        return 10 - profundidade
    if empate():
        return 0

    if maximizando:
        melhor = -1000
        for i in range(9):
            if tab[i] == " ":
                tab[i] = "O"
                valor = minimax(tab, profundidade + 1, False)
                tab[i] = " "
                melhor = max(melhor, valor)
        return melhor
    else:
        pior = 1000
        for i in range(9):
            if tab[i] == " ":
                tab[i] = "X"
                valor = minimax(tab, profundidade + 1, True)
                tab[i] = " "
                pior = min(pior, valor)
        return pior

# Escolhe a melhor jogada para o computador
def melhor_jogada():
    melhor_valor = -1000
    melhor_posicao = 0
    for i in range(9):
        if tabuleiro[i] == " ":
            tabuleiro[i] = "O"
            valor = minimax(tabuleiro, 0, False)
            tabuleiro[i] = " "
            if valor > melhor_valor:
                melhor_valor = valor
                melhor_posicao = i
    return melhor_posicao

# Função principal do jogo
def jogar():
    print("Bem-vindo ao Jogo da Velha!")
    print("Você é o 'X' e o computador é o 'O'")
    print("Use números de 0 a 8 para jogar:")
    print("0 | 1 | 2\n3 | 4 | 5\n6 | 7 | 8")

    while True:
        mostrar_tabuleiro()

        # Vez do jogador
        while True:
            try:
                jogada = int(input("Sua jogada (0-8): "))
                if 0 <= jogada <= 8 and tabuleiro[jogada] == " ":
                    break
                else:
                    print("Escolha inválida.")
            except:
                print("Digite um número válido.")

        tabuleiro[jogada] = "X"

        if venceu("X"):
            mostrar_tabuleiro()
            print("Você venceu!")
            break
        if empate():
            mostrar_tabuleiro()
            print("Empate!")
            break

        # Vez do computador
        print("O computador está pensando...")
        pos = melhor_jogada()
        tabuleiro[pos] = "O"

        if venceu("O"):
            mostrar_tabuleiro()
            print("O computador venceu!")
            break
        if empate():
            mostrar_tabuleiro()
            print("Empate!")
            break

# Inicia o jogo
jogar()
# Fim do código