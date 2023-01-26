import pymysql
from flask import Flask, request, jsonify
app = Flask(__name__)
from flask_cors import CORS
CORS(app)

# Connexion à la base de données MySQL
cnx = pymysql.connect(user='root', password='meteo', host='localhost', database='api')
cursor = cnx.cursor()

# Enregistrement des données de l'ESP
@app.route('/data', methods=['POST'])
def data():
    data = request.get_json()
    cursor.execute("INSERT INTO meteo_donnée (degré) VALUES (%s)", (data['degré'],))
    cnx.commit()
    return 'degré reçu'

# Renvoi des données en temps réel
@app.route('/realtime', methods=['GET'])
def realtime():
    cursor.execute("SELECT * FROM meteo_donnée ORDER BY id DESC LIMIT 1")
    result = cursor.fetchone()
    print(result)
    return jsonify(result)

# Renvoi des données historiques
@app.route('/history', methods=['GET'])
def history():
    cursor.execute("SELECT * FROM meteo_donnée")
    result = cursor.fetchall()
    return jsonify(result)

# Enregistrement des données d'humidité
@app.route('/humidity', methods=['GET'])
def humidity():
    data = request.get_json()
    cursor.execute("INSERT INTO humidité (teaux_humidité) VALUES (%s)", (data['teaux_humidité'],))
    cnx.commit()
    return 'Humidity data received'

CORS(app, resources={r"/*": {"origins": "192.168.137.187"}})

if __name__ == '__main__':
    app.run(host='192.168.137.187', debug=True)
