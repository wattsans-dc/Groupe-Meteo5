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
    return 'degré reçu'

# Renvoi des données en temps réel
@app.route('/realtime', methods=['GET'])
def realtime():
    cnx = pymysql.connect(user='root', password='meteo', host='localhost', database='api')
    cursor = cnx.cursor()
    cursor.execute("SELECT degre,teaux_humidite FROM meteo_donnée ORDER BY id DESC LIMIT 1")
    result = cursor.fetchone()
    cnx.close()
    print(result)
#    socketio.emit('new_data', {"degré": result[0], "teaux_humidité": result[1]})
    #return jsonify({"degré": result[0], "teaux_humidité": result[1]})
    return {"degre": result[0], "teaux_humidite": result[1]}
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
    return 'Humidity data received'

#post donné capteur
@app.route('/data_from_sonde', methods=['POST'])
def data_from_sonde():
    cnx = pymysql.connect(user='root', password='meteo', host='localhost', database='api')
    cursor = cnx.cursor()
    data = request.json
    cursor.execute("INSERT INTO meteo_donnée (degre, teaux_humidite) VALUES (%s, %s)", (data['degre'], data['teaux_humidite']))
    cnx.commit()
    cursor.close()
    cnx.close()
    return "Data received and added to the database"
    return "kikoo"

CORS(app, resources={r"/*": {"origins": "192.168.137.187"}})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
