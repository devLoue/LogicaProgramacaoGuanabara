# incompleto

from random import randint
print ('-'*30)
print('          MEGA SENA          ')
print ('-'*30)
#declaracao
jogos = list()
lista = []
contador = 1
total = 1
quantidade = int(input('Digiite a quantidade de jogos que quer fazer:'))
#verificador de jogos:
while total <= quantidade:
    while True:
        aleatorio1 = randint (1, 60)
        if aleatorio1 not in lista:
            lista.append(aleatorio1)
            contador = contador + 1
            if contador > 6:
                break
    total = total + 1
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    contador = 1
    #final do programa / exibição de resultado
for l in jogos:
    print(f'jogo {contador}: {l}')
    contador += 1