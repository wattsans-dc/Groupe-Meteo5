import requests
import mysql.connector

cnx = mysql.connector.connect(user='nom_d_utilisateur', password='mot_de_passe',
                              host='192.168.137.187',
                              database='nom_de_la_bdd')


moyenne = 0
Valeur = 0
Valeur1 = sonde.value
i = 0

while i < 4:
    i =+ 1
    Valeur = Valeur + Valeur1
    time.sleep(2)
    Valeur1 = sonde.value
moyenne = Valeur / 5


