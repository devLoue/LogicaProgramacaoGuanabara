# Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
numero = 0
soma = 0
contador = 0
while True:
    numero = int(input('Digite um valor [999 para parar]: \n'))
    if numero == 999:
        break
    soma = soma + numero
    contador = contador + 1
print(f'Você digitou {contador} números e a soma dos números é {soma} \nEncerrando... ')