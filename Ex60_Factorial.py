# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. 
#A resolução mais simples é importar factorial da biblioteca math

numero = int(input('Digite um número para ser calculado o fatorial: \n'))
fatorial = 1

for contador in range (numero, 0, -1):
    print ('{} x '.format(contador), end='')
    if contador == 1:
        print('= ', end='')
        print(fatorial)
    fatorial = fatorial * contador
print ('O fatorial de {} é: {}'.format(numero, fatorial))