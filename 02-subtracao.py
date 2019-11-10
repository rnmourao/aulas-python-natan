# recebendo o primeiro numero
minuendo = input('Digite o minuendo: ')

# convertendo numero em forma de texto para numero de fato
minuendo = int(minuendo)

# recebendo o segundo numero
subtraendo = input('Digite o subtraendo: ')

# convertendo numero em forma de texto para numero de fato
subtraendo = int(subtraendo)

# testar se minuendo é maior que subtraendo
if subtraendo > minuendo:
    print('O minuendo tem que ser maior ou igual ao subtraendo!')
    exit(1)

# cria nova variavel que é a diferença dos dois número recebidos
subtracao = minuendo - subtraendo

# imprimindo resultado na tela
print('O resultado é', subtracao)