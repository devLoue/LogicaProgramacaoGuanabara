import pg8000
#Definindo a função criar empregado, que na vdd é um insert into no Postgre



def inserir_empregado(matricula, nome_empregado, data_nasc):
    conexaobd = pg8000.connect(user='postgres',password='123456',host='localhost', database='postgres')
    cursor.execute(
        "INSERT INTO EMPREGADO (matricula, nome_empregado, data_nasc) VALUES (%s,%s, %s)"
        ,(matricula,nome_empregado,data_nasc)
    )

cursor.close()
conexaobd.c

