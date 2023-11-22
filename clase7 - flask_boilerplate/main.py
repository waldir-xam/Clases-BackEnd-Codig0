from psycopg2 import connect

connection = connect(
    host='localhost',
    port=5432,
    database='First_DB',
    user='postgres',
    password='ratatrampa'
)

cursor = connection.cursor()

#cursor.execute('SELECT * FROM area')
#cursor.execute('SELECT version();')
#fetchone ->debe usarse si se trae un solo registro
#fetchall -> debe usarse si se trae mas de un registro

#record=cursor.fetchone()
#print(record)

#Obligatorio cerrar la cesion y la cconexion
cursor.close()
connection.close()
