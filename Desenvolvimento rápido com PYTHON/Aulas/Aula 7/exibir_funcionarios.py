import pg8000

#Fazendo a conexão com o banco na minha máquina local
conexaobd = pg8000.connect(user="postgres",
                           password="123456",
                           host="localhost",
                           database="postgres"
                           )

print("conexaobd criado")

cursor = conexaobd.cursor()
cursor.execute("SELECT * FROM EMPREGADO")
retorno_dados = cursor.fetchall()
for row in retorno_dados:
    print(f'id {row[0]}, nome {row[1]}, data de nascimento {row[2]}.' )

print("Fechando cursor e fechando o banco...")
cursor.close()
conexaobd.close()

