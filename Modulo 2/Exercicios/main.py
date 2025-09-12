import sqlite3

# CRIAR A CONEXAO COM O BANCO E GARDAMOS NA VARIAVEL 'BANCO'
banco = sqlite3.connect('ricardaofather.db')


# CRIAMOS A VARIAVEL CURSOR E COLOCAMOS EM UMA VARIAVEL 
cursor = banco.cursor()

# UPDATE
cursor.execute("UPDATE funcionarios SET departamento = 'TI'  WHERE id = 1 ")



# INSERINDO NA TABELA DESEJADAS OS VALORES 
# cursor.execute("INSERT INTO empresa VALUES(6,'paracetamol', ,'20/07/2026')")


# ENVIANDO DADOS
banco.commit()

# PRINTAR A INFORMAÇAO
# cursor.execute("SELECT * FROM funcionarios WHERE nome = 'Carla'")
# cursor.execute("SELECT salario FROM  funcionarios  ")
# print(cursor.fetchall())