numero = 0
contador = 0
soma = 0
while numero != 999:
    numero = int(input('Digite um número \n [999 para parar]:'))
    contador = contador + 1
    soma = soma + numero
contador = contador - 1
soma = soma - 999
print('Você digitou {} números e a soma entre eles é: {} '.format(contador, soma))