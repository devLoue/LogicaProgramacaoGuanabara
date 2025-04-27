#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

#Para que os três segmentos formem um triângulo, existe o que conhecemos como condição de existência, que é a seguinte: a soma de dois lados é sempre menor que o terceiro lado.

n1 = float(input('Primeiro segmento de reta:'))
n2 = float(input('Segundo segmento de reta:'))
n3 = float(input('Terceiro segmento de reta:'))

if (n1 < n2+n3) and (n2 < n1+n3) and n3 < n1+n2:
    print('O triângulo pode ser formado!')
else: 
    print('O triângulo não pode ser formado')