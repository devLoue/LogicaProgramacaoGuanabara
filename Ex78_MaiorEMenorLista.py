lista = []
maior = 0
menor = 0
posmenor = 0
posmaior = 0
for c in range (0,5):
    n = int(input(f'Digite o valor na posição {c}: '))
    lista.append(n)
    if c == 0:
        maior = n
        menor = n
    if n >= maior:
        maior = n
    if n <= menor:
        menor = n
print(f'Você digitou os valores: {lista}')
print(f'O maior valor digitado foi {maior}', end = ' ')
for i, v in enumerate(lista):
    if v == maior:
        print(f'na posição {i}')
print(f'O menor valor digitado foi {menor}', end = ' ')
for i, v in enumerate(lista):
    if v == menor:
        print(f'na posição {i}')