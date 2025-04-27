# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Eu sorteei os valores', numeros)
for n in numeros:
    print(n, end = ' ')
print('\n')

#Dentro das duplas existe uma funcionalidade chamada MAX que identifica qual é o maior valor da tupla.
print (f'O maior valor sorteado foi {max(numeros)}')

#Também existe o contrário, o comando MIN
print(f'O menor valor sorteado foi {min(numeros)}')