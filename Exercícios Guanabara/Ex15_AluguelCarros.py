#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado

dias = int(input('por quantos dias o carro foi alugado?'))
km = float(input('Quantos km foram rodados? '))
somatotal = (dias*60) + (km*0.15)
print(f'O carro foi alugado por {dias} dia(s) e {km}km foram rodados. \nValor total R$ {somatotal:.2f}')