lista = []
decisao = ' '
while True:
    n = int(input('Digite um valor:'))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucecsso!')
    else:
        print('Este valor já está inserido na lista.')
        n = int(input('Digite outro valor:'))
        if n not in lista:
            lista.append(n)
            print('Valor adicionado com sucecsso!')
    decisao = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if decisao not in 'SsNn':
        decisao = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if decisao == 'N':
        break
print(lista)
lista.sort() #altera a lista, enquanto sorted(lista) apenas apresenta a lista em ordem
print(lista)