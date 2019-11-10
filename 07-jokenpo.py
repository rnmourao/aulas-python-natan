import random

jogador = input('Digite sua jogada (pedra/papel/tesoura): ')

opcoes = ['pedra', 'papel', 'tesoura']

computador = random.choice(opcoes)

if jogador == 'pedra':
    if computador == 'papel':
        vencedor = 'computador'
    elif computador == 'tesoura':
        vencedor = 'jogador'
    else:                          # computador == 'pedra'
        vencedor = 'empate'
elif jogador == 'tesoura':
    if computador == 'papel':
        vencedor = 'jogador'
    elif computador == 'tesoura':
        vencedor = 'empate'
    else:                          # computador == 'pedra'
        vencedor = 'computador'
else:                              # jogador == papel
    if computador == 'papel':
        vencedor = 'empate'
    elif computador == 'tesoura':
        vencedor = 'computador'
    else:                          # computador == 'pedra'
        vencedor = 'jogador'

print('Computador:', computador)
print('Resultado:', vencedor)