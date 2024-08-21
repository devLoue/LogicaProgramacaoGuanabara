# Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
#Vamos utilizar a função sin, cos, tang e radians da biblioteca math
from math import sin, cos, tan, radians

angulo = float(input('Digite o angulo a ser calculado (seno, coseno e tangente):'))
print(f'Seno: {sin(radians(angulo)):.2f} \nCoseno: {cos(radians(angulo)):.2f} \nTangente: {tan(radians(angulo)):.2f}')