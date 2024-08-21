# Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

#Solução 1 (Remova """ no inicio e no fim do código """)
""" from random import randint
print("Vou pensar em um número entre 1 e 6, tente advinhar...")
n_random = randint(1,6)
print(n_random)
n = int(input('Em qual número eu pensei?'))
if n > 6 or n < 1:
    print('Inválido. Insira um número de 1 a 6. ')
if n != n_random and (n > 6 or n < 1)== False :
    print(f'Você errou hahaha pensei no número {n_random} e você arriscou {n}')
if n == n_random:
    print(f'Parabéns! Odeio adimitir, mas você ganhou :( ') """ 


#Solução 2 (melhor soluçao): 
from random import randint
print("Vou pensar em um número entre 1 e 6, tente advinhar...")
n_random = randint(1,6)
print(n_random)
while True:
    n = int(input('Tente adivinhar: em qual número eu pensei?'))
    if n >6 or n <= 0: 
        print('Inválido. Insinira um número de 1 a 6.')
    if n != n_random and (n >6 or n <= 0) == False:
        print(f'Você errou hahahaha pensei no número {n_random} e você arriscou o número {n}. Eu ganhei!')
        break
    if n == n_random:
        print(f'Parabéns! Odeio adimitir, mas você ganhou :( ')
        break