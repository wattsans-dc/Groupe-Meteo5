import pymysql
from flask import Flask, request, jsonify
app = Flask(__name__)
from flask_cors import CORS
CORS(app)
import time



# Enregistrement des données de température
@app.route('/temp', methods=['GET'])
def data():
    cnx = pymysql.connect(user='root', password='meteo', host='localhost', database='api')
    cursor = cnx.cursor()
    cursor.execute("SELECT degre FROM meteo_donnée ORDER BY id DESC")
    result = cursor.fetchall()
    cursor.close()
    cnx.close()
    return jsonify(result)


# Enregistrement des données de température
@app.route('/humide', methods=['GET'])
def humide():
    cnx = pymysql.connect(user='root', password='meteo', host='localhost', database='api')
    cursor = cnx.cursor()
    cursor.execute("SELECT teaux_humidite FROM meteo_donnée ORDER BY id DESC")
    result = cursor.fetchall()
    cursor.close()
    cnx.close()
    return jsonify(result)


# Renvoi des données en temps réel
@app.route('/realtime', methods=['GET'])
def realtime():
    cnx = pymysql.connect(user='root', password='meteo', host='localhost', database='api')
    cursor = cnx.cursor()
    cursor.execute("SELECT degre,teaux_humidite FROM meteo_donnée ORDER BY id DESC LIMIT 1")
    result = cursor.fetchone()
    cnx.close()
    print(result)
    return {"degre": result[0], "teaux_humidite": result[1]}


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
    return "reçu"

CORS(app, resources={r"/*": {"origins": "192.168.137.187"}})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
