while True:
    numero = int(input('Qual valor você quer ver a tabuada? \n'))
    if numero < 0:
        print ('Encerrando...')
        break
    print(numero)
    for c in range (1, 11):
        print(f'{numero} x {c} = {numero * c}')
        