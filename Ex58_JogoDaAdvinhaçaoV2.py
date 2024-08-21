# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
print ('Seja bem vindo ao jogo da advinhação! \nVocê tem 3 tentativas para descobrir um número de 1 a 10 \nBoa sorte! \n')
numero_sorteado = randint(1,10)
numero_digitado = int(input('Digite um número: \n'))
tentativa = 1

while tentativa <=3:
    if numero_digitado == numero_sorteado:
        print('Parabéns! Você acertou! \n O número sorteado é {} e você acertou com {} tentativas.'.format(numero_sorteado, tentativa))
        break
    if numero_digitado != numero_sorteado and numero_digitado < numero_sorteado:
        print('Você errou! {} é menor do que o número sorteado \nTente denovo!'.format(numero_digitado))
        tentativa = tentativa + 1
        numero_digitado = int(input('Digite um número: \n'))
    if numero_digitado != numero_sorteado and numero_digitado > numero_sorteado:
        print('Você errou! {} é maior do que o número sorteado \nTente denovo!'.format(numero_digitado))
        numero_digitado = int(input('Digite um número: \n'))