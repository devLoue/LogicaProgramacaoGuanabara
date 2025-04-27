#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.


#Solução1: Utilizando a biblioteca de matemática (math) do python
from math import trunc
n=float(input('Digite um número:\n'))
print(f'O número digitado foi {n} e sua parte inteira é {trunc(n)}')


#Solução2 sem importar biblioteca (módulos)

n=float(input('Digite um número:\n'))
print(f'O número digitado foi {n} e sua parte inteira é {int(n)}')