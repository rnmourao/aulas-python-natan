import random
from sprites_forca import SPRITES


def escolher_palavra(arquivo):
    # ler arquivo
    with open(arquivo, 'r') as arq:
        lista = arq.readlines()

    # escolher palavra aleatoriamente
    palavra = random.choice(lista)

    # retirar quebra de linha do arquivo
    palavra = palavra.replace('\n', '')
    
    # devolver palavra
    return palavra


def mostrar_forca():
  # mostra forca e tracos atualizados
  print(SPRITES[erros])
  tracos_bonitos = ' '.join(tracos)
  print('\n', tracos_bonitos, '\n')


# escolher uma palavra aleatoriamente
palavra = escolher_palavra("forca.txt")

# transformar palavra em lista de letras
palavra = list(palavra)

# criar lista de underlines do tamanho da palavra
tracos = ["_"] * len(palavra)

erros = 0

TOTAL_ERROS = 6


mostrar_forca()

# loop infinito
while True:

  # receber uma letra do jogador
  letra = input("Digite uma letra: ")

  # transformar a letra em maiusculo
  letra = letra.upper()

  # variavel para identificar se acertou uma ou mais letras
  acertou = False

  # verifica letra por letra da palavra
  for i, p in enumerate(palavra):

    # se a letra coincide
    if letra == p:
      # marca acerto
      acertou = True

      # substitui traco por letra
      tracos[i] = letra

  # mostra mensagem de acerto ou erro
  if acertou:
    print("acertou miseravel")
  else:
    erros = erros + 1
    print("te zuei kekeke")

  mostrar_forca()

  # verifica se os tracos foram todos substistuidos
  if "_" not in tracos:
    print("VOCÊ GANHOU!")

    # para o loop infinito
    break

  # verifica se ja errou maximo de vezes
  if erros >= TOTAL_ERROS:
    print("VOCE CAIU NA TRAP DO RELAMPAGO MARQUINHOS")
    
    # para o loop infinito
    break