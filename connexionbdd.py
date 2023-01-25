import mysql.connector

cnx = mysql.connector.connect(user='root', password='meteo',
                              host="localhost",
                              database='api')

cursor = cnx.cursor()



cursor.execute("SELECT * FROM api WHERE id_sonde = 1")
results = cursor.fetchall()

for row in results:
    print(row)

cursor.close()
cnx.close()


