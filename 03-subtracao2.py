# recebendo o primeiro numero
x = input('Digite o x: ')

# convertendo numero em forma de texto para numero de fato
x = int(x)

# recebendo o segundo numero
y = input('Digite o y: ')

# convertendo numero em forma de texto para numero de fato
y = int(y)

# testar se x é maior que y
if y > x:
    z = y - x    
else:
    z = x - y

# imprimindo resultado na tela
print('O resultado é', z)