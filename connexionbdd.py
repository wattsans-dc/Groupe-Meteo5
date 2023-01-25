import mysql.connector

db = mysql.connector.connect(
    host="192.168.137.187",
    user="root",
    password="meteo",
    database="Sonde"
)

print(Sonde.Temperature)

db.close()