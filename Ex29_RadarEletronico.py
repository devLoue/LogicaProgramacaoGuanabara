# Exercício Python 029: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input('Qual é a velocidade do carro? (Km/h)'))
if v > 80:
    print("Você foi mutado!")
    print(f"Total a pagar R${(v-80)*7:.2f}")
elif v <80:
    print("Você não possui multas.")