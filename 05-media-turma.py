
notas = [10, 8, 6, 7, 10, 8, 0, 5, 10, 8.5, 7, 7, 7, 4, 8, 9, 10] 

soma = 0
quantidade_alunos = 0

for nota in notas:
    soma = soma + nota
    quantidade_alunos = quantidade_alunos + 1

media = soma / quantidade_alunos

print('média:', media)