#Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
temperaturac = float(input('Qual é a temperatura em C: '))
f = ((9*temperaturac)/5)+32
print(f'A temperatura é: {f} F')