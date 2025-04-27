# Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros =('zero','um',' dois', 'tres',' quatro', 'cinco',' seis',' sete',' oito',' nove',' dez',' onze',' doze',' treze',' quatorze',' quinze',' dezesseis',' dezessete', 'dezoito', 'dezenove', 'vinte')
numero = int(input('Digite um número entre 0 e 20:'))
while True:
    if numero <= 20 and numero >= 0:
        print(f'A forma por extenso do número {numero} é: {numeros[numero]}')
        break
    else:
        print('Número inválido.')
        numero = int(input('Digite um número entre 0 e 20:'))