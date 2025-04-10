# Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.
somadospares = 0
somadaterceira = 0
maiorvalor = 0
contador = 0
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para {[l,c]}'))
        if matriz [l][c] % 2 == 0:
            somadospares = somadospares + matriz [l][c]
        if maiorvalor == 0 and matriz[1][c]:
            maiorvalor = maiorvalor + matriz[l][c]
print('final', matriz)
print('Soma de todos os números pares: ', somadospares)
for l in range (0,3):
    somadaterceira = somadaterceira + matriz[l][2]
print('Soma da terceira coluna: ',somadaterceira )
for c in range(0,3):
    if matriz[1][c] > maiorvalor:
        maiorvalor = matriz[1][c]
print('O maior valor da segunda linha é: ', maiorvalor)