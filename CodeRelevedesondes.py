import requests
import mysql.connector
from sonde import temp, humid

"""MOYENNE DES 5 DERNIERES VALEURS POUR LA TEMPERATURE ET L'HUMIDITE"""
i = 0
ValeurTemp = 0
ValeurHumid = 0
moyenneTemp = 0
moyenneHumid = 0

while i < 4:
    ReceptionTemp = requests.get(temp)
    ReceptionHumid = requests.get(humid)
    ValeurTemp = ValeurTemp + ReceptionTemp
    ValeurHumid = ValeurHumid + ReceptionHumid
    i = i + 1
moyenneTemp = ValeurTemp / 5
moyenneHumid = ValeurHumid / 5


"""IMPORT DANS LA BDD DE CES MOYENNES"""
baseDeDonnees = mysql.connector.connect(user='root',
                                        password='meteo',
                                        host='192.168.137.187',
                                        database='api')
curseur = baseDeDonnees.cursor()
curseur.execute("INSERT INTO api (degré, teaux_humidité) VALUES (%s, %s)", (moyenneTemp, moyenneHumid))
baseDeDonnees.commit()
baseDeDonnees.close()










