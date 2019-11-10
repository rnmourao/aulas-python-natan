import random

# 1) computador gera um numero aleatório

opcoes = [1,2,3,4,5,6,7,8,9]

numero_computador = random.choice(opcoes)

chances = 3

while True:

    # 2) perguntar um numero de 1 a 9
    numero_jogador = int(input('Digite um número de 1 a 9 (0 para sair do jogo): '))
    chances = chances - 1

    # jogador digita 0 (zero) para sair do jogo
    if numero_jogador == 0:
        print('falooooooooooooooooooooooooooouuuuuuuuuuuuuuuuuuuusssssssssssss')
        break

    # 3) verificar se o numero está correto
    if numero_jogador == numero_computador:       # A = B
        print('venceu')
    # 5) se acertar, finalize o jogo        
        break
    elif numero_jogador <  numero_computador:     # A < B
        print('muito baixo')
    else:                                         # A > B
        print('muito alto')
        
    # 4) se errou, verifica se o jogador ainda tem jogadas
    #    se tiver, volta para o passo 2)
    #    se não tiver, perde o jogo e finaliza
    if chances == 0:
        print('perdeu playboy')
        break




