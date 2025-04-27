minutos = 0
while(True):
    for segundos in range (0, 60):
        if segundos == 60:
            minutos = minutos + 1
            segundos = 0
        print(f'{minutos}:{segundos}')