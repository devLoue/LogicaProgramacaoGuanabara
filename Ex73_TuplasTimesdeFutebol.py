#Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
times = ('corinthians', 'palmeiras', 'santos', 'grêmio', 'cruzeiro', 'flamengo', 'vasco', 'chapecoense', 'atletico', 'botafogo', 'atletico PR', 'bahia', 'sao Paulo', 'fluminense', 'sport', 'vitoria','coritiba','avai', 'ponte preta','atletico GO')
cont = 1
for t in times:
    print(cont,t)
    cont = cont + 1
#a)Os 5 primeiros times.
print(f'Os cinco primeiros times do brasileirão são: {times[0:5]}')
#b)Os últimos 4 colocados.
print(f'Os cinco últimos colocados são: {times[15:21]}') #Ou poderia começar do final da tupla utilizando o -, exemplo: [-4:]
#c) Times em ordem alfabética. 
print(f'Ordem alfabética dos times do brasileirão: {sorted(times)}')
#d) Em que posição está o time da Chapecoense.
posicao = times.index('chapecoense') #index é utilizado para descobrir a posicao da tupla
print(f'O chapecoense está na {posicao+1} posição')