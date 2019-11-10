# recebe nota da prova
nota = input('Digite uma nota de 0 a 10: ')

# tranforma texto recebido em numero
try:
    nota = float(nota)
except ValueError:
    print('Você deve digitar um número!')
    exit(1)

if nota > 10:
    print('Bem loco! Vc é impressionante!')
    exit(2)

# verifica se nota está acima da média da escola
if nota >= 6:
    print('Passou!')

# regra do senão
else:
    print('Recuperação!')

# imprime algo fora da condicional
# print('m')