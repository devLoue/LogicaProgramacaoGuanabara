# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

#solucao 1
'''par = []
impar = []

print('Digite alguns valores e eu os separarei por par ou impar.')
while True:
    n = int(input('Digite um valor:'))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    decisao = str(input('Deseja adicionar outro número? [S/N]')).strip().upper()[0]
    if decisao == 'N':
        break
    while decisao not in 'SN':
        decisao = str(input('Deseja adicionar outro número? [S/N]')).strip().upper()[0]
print(f'Lista de números pares: {par}')
print(f'Lista de números ímpares: {impar}')
par.sort()
print(f'Lista de números pares em ordem crescente: {par}')
par.sort(reverse=True)
print(f'Lista de números pares em ordem decrescente: {par}') '''

#solucao2
''' numeros = []
par2= []
impar2 = []

for n in range (1,8):
    numeros.append(int(input(f'digite o {n}o numero:')))
print(numeros)
for numero in numeros:
    if numero % 2 == 0:
        par2.append(numero)
    else:
        impar2.append(numero)
par2.sort()
print('Lista de par em ordem crescente:', par2)
impar2.sort()
print('Lista de impar em ordem crescente:', impar2) '''

numeros = [[], []]
valor = 0
for c in range (1, 8):
    valor = int(input(f'Digite o {c}o valor'))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
numeros[0].sort()
print(f'Números pares em ordem crescente: {numeros[0]}')
numeros[1].sort()
print(f'Números impares em ordem crescente: {numeros[1]}')