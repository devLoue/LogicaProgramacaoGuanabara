import pg8000

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
    print(row)


cursor.close()
conexaobd.close()
