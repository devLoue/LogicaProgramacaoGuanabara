# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
from random import randint
contador = 0
print ('-'* 40)
print ('VAMOS JOGAR PAR OU IMPAR?' )
print ('-' * 40)
print ('MELHOR DE 3!')
print ('-' * 40)
print ('SE PREPARE...')
print ('-' * 40)
while True:
    computador = randint(1,10)
    print (computador)
    numero = int(input('Digite um valor:'))
    decisao = str(input('Par ou impar? [P\I]')).strip().upper()[0]
    soma = numero + computador
    while decisao not in 'PpIi':
        print('Opção inválida! Escolha par ou impar. [P\I]')
        decisao = str(input('Par ou impar? [P\I]')).strip().upper()[0]
    while decisao in 'PpIi':
        if soma % 2 == 0 and decisao == 'P':
            print (f'Você escolheu {numero} e o computador escolheu {computador}. Total de {soma} (PAR) \nVOCÊ GANHOU!')
            contador = contador + 1
            decisao = ' '
        if soma % 2 == 0 and decisao == 'I':
            print(f'Você escolheu {numero} e o computador {computador}. Total de {soma} (PAR) \nVOCÊ PERDEU!')
            break
        if soma % 2 == 1 and decisao == 'P':
            print (f'Você escolheu {numero} e o computador escolheu {computador}. Total de {soma} (IMPAR) \nVOCÊ PERDEU!')
            break
        if soma % 2 == 1 and decisao == 'I':
            print(f'Você escolheu {numero} e o computador {computador}. Total de {soma} (IMPAR) \nVOCÊ GANHOU!')
            contador = contador + 1
            decisao = ' '
print (f'GAME OVER. Você venceu {contador} vezes.')
