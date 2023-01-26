
import pymysql
from flask import Flask, request, jsonify
app = Flask(__name__)
from flask_cors import CORS
CORS(app)
import time
#from flask_socketio import SocketIO
#socketio = SocketIO(app)
# Connexion à la base de données MySQL
#cnx = pymysql.connect(user='root', password='meteo', host='localhost', database='api')
#cursor = cnx.cursor()

# Enregistrement des données de l'ESP
@app.route('/temp', methods=['POST'])
def data():
    cnx = pymysql.connect(user='root', password='meteo', host='localhost', database='api')
    cursor = cnx.cursor()
    data = request.get_json()
    cursor.execute("INSERT INTO meteo_donnée (degré) VALUES (%s)", (data['degré'],))
    cnx.commit()
    return 'Données degré reçu'

# Renvoi des données en temps réel
@app.route('/realtime', methods=['GET'])
def realtime():
    cnx = pymysql.connect(user='root', password='meteo', host='localhost', database='api')
    cursor = cnx.cursor()
    cursor.execute("SELECT degré,teaux_humidité FROM meteo_donnée ORDER BY id DESC LIMIT 1")
    result = cursor.fetchone()
    cnx.close()
    print(result)
#    socketio.emit('new_data', {"degré": result[0], "teaux_humidité": result[1]})
    #return jsonify({"degré": result[0], "teaux_humidité": result[1]})
    return {"degré": result[0], "teaux_humidité": result[1]}
# Renvoi des données historiques
@app.route('/history', methods=['GET'])
def history():
    cursor.execute("SELECT * FROM meteo_donnée")
    result = cursor.fetchall()
    return jsonify(result)

# Enregistrement des données d'humidité
@app.route('/humidity', methods=['POST'])
def humidity():
    data = request.get_json()
    cursor.execute("INSERT INTO meteo_donnée (teaux_humidité) VALUES (%s)", (data['teaux_humidité'],))
    cnx.commit()
    return 'Données humidité reçues'

#post donné capteur
@app.route('/data_from_sonde', methods=['POST'])
def data_from_sonde():
    cnx = pymysql.connect(user='root', password='meteo', host='localhost', database='api')
    cursor = cnx.cursor()
    data = request.json
    cursor.execute("INSERT INTO meteo_donnée (degré, teaux_humidité) VALUES (%s, %s)", (data['degré'], data['teaux_humidité']))
    cnx.commit()
    cursor.close()
    cnx.close()
    return "Donées reçues et envoyées dans la base de données "

    return "Correct"

CORS(app, resources={r"/*": {"origins": "192.168.137.187"}})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

