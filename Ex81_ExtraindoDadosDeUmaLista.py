# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    n = int(input('Digite um valor a ser inserido na lista:'))
    lista.append(n)
    decisao = str(input('Deseja adicionar outro valor? [S/N] ')).strip().upper()[0]
    if decisao not in 'SsNn':
        decisao = str(input('Deseja adicionar outro valor? [S/N]')).strip().upper()[0]
    if decisao == 'N':
        break
print(f'Foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(f'Os números digitados em forma decrescente:', lista)
if 5 in lista:
    print(f'O valor 5 está presente na lista')
if 5 not in lista:
    print(f'O valor 5 não foi digitado!')