import mysql.connector
from flask import Flask, request, jsonify
app = Flask(__name__)

# Connexion à la base de données MySQL
cnx = mysql.connector.connect(user='root', password='meteo', host='localhost', database='api')
cursor = cnx.cursor()

# Enregistrement des données de l'ESP
@app.route('/data', methods=['POST'])
def data():
    data = request.get_json()
    cursor.execute("INSERT INTO tablename (field1, field2, field3) VALUES (%s, %s, %s)", (data['field1'], data['field2'], data['field3']))
    cnx.commit()
    return 'Data received'

# Renvoi des données en temps réel
@app.route('/realtime', methods=['GET'])
def realtime():
    cursor.execute("SELECT * FROM tablename ORDER BY id DESC LIMIT 1")
    result = cursor.fetchone()
    return jsonify(result)

# Renvoi des données historiques
@app.route('/history', methods=['GET'])
def history():
    cursor.execute("SELECT * FROM tablename")
    result = cursor.fetchall()
    return jsonify(result)

# Enregistrement des données d'humidité
@app.route('/humidity', methods=['POST'])
def humidity():
    data = request.get_json()
    cursor.execute("INSERT INTO tablename (field1, field2, field3, field4) VALUES (%s, %s, %s, %s)", (data['field1'], data['field2'], data['field3'], data['field4']))
    cnx.commit()
    return 'Humidity data received'


if __name__ == '__main__':
    app.run(debug=True)
