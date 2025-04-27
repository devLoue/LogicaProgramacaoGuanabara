# Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
#minha resolucao

print ('Gerador de PA \n')
primeiro = int(input('Digite o primeiro número da PA \n'))
razao = int(input('Digite a razao da PA \n'))
termo = primeiro
contador = 1
escolha1 = 'S'
quantidade = 0
while contador <= 10:
    print(termo)
    termo = termo + razao
    contador = contador + 1
termo = termo - primeiro
while escolha1 == 'S':
    escolha2 = str(input('Você deseja mais termos? \ns ou n? \n')).strip().upper()
    if escolha2 == 'S':
        contador = 1
        quantidade = int(input('Digite quantos termos você quer \n'))
        while contador <= quantidade:
            contador = contador +1
            termo = termo + razao
            print(termo)
    if escolha2 == 'N':
        escolha1 = 'N'
        print('Encerrando...')
