# minha solução errada kkk
'''matriz = [[], [], []]
contador = 0
for valor in range (0,3):
    matriz[0].append(int(input(f'Digite um valor para [{contador}, {valor}] ')))
contador = 1
for valor in range (0,3):
    matriz[1].append(int(input(f'Digite um valor para [{contador}, {valor}] ')))
contador = 2
for valor in range(0,3):
    matriz[2].append(int(input(f'Digite um valor para [{contador}, {valor}] ')))
print(matriz)
print(matriz[0])
print(matriz[1])
print(matriz[2])'''

#solução do guanabara

matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para {[l,c]}'))
        print(matriz)
print('final', matriz)