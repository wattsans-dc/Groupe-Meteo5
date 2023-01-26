import mysql.connector

# Configuration de la connexion à la base de données
config = {
    'user': 'root',
    'password': 'meteo',
    'host': '192.168.137.187',
    'database': 'api',
    'raise_on_warnings': True,
}

try:
    # Connexion à la base de données
    cnx = mysql.connector.connect(**config)
    print("Connexion établie avec succès.")

except mysql.connector.Error as err:
    # Affiche un message d'erreur si la connexion échoue
    print("La connexion a échoué : {}".format(err))
