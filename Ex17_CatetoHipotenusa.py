#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
#Lembrando que o quadrado da hipotenusa é a soma do quadrado dos catetos ou seja raiz de hipotenusa = ca² . co² 


#Solução 1 de forma matemática
ca = float(input('Informe o comprimento do cateto adjascente:'))
co = float(input('Informe o comprimento do cateto oposto:'))
hipotenusa = (ca **2 + co**2) ** (1/2) #Elevar um número a 1/2 é equivalente a raiz quadrada do mesmo número.
print(f'A hipotenusa vai medir {hipotenusa}')


#Solução 2 Importando a biblioteca math
from math import hypot
ca = float(input('Informe o comprimento do cateto adjascente:'))
co = float(input('Informe o comprimento do cateto oposto:'))
print(f'A hipotenusa vai medir {hypot(ca, co)}')