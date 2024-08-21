#Conversor de medidas
n = float(input('Digite a medida em metros:'))
cm = n*100
mm = n*1000
km = n/1000
print(f'{n} metros corresponde a {cm:.2f} cm, {mm:.2f}mm e {km:.2f}km')