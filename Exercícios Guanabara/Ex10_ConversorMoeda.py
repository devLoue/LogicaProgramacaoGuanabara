#Conversor de Moeda
n = float(input('Quanto dinheiro você tem na carteira?:'))
dolar = 4.95
print(f'Com R${n:.2f} você pode comprar U$ {(n / dolar):.2f}')