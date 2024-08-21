# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

n1 = int(input('Digite um valor:'))
n2 = int(input('Digite um valor:'))
n3 = int(input('Digite um valor:'))
n4 = int(input('Digite um valor:'))
tupla = (n1, n2, n3, n4)
count = 0

print(f'Você digitou os seguintes números: {tupla} ')

#A) Quantas vezes apareceu o valor 9.
if 9 in tupla:
    print(f'O número 9 apareceu {tupla.count(9)} vezes')
if 9 not in tupla:
    print('O número 9 não foi digitado')
#B) Em que posição foi digitado o primeiro valor 3.
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1} posição')
else:
    print('O número 3 não foi digitado em nenhuma posição ')
#C) Quais foram os números pares.
for n in tupla:
    if n % 2 == 0:
        print(f'{n} é par')