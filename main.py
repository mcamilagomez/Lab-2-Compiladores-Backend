import json
from flask import Flask, jsonify
from flask_cors import CORS
from functionn import procesar_regex, procesar_regex2 # Importa todas las funciones de functions.py

app = Flask(__name__)
CORS(app)

@app.route('/api1/<regex>', methods=['GET'])
def procesar1(regex):
    procesar_regex(regex) 
    with open('appi1.json', 'r') as json_file:
        data = json.load(json_file)
    return jsonify(data)

@app.route('/api2/<regex>/<cadena>', methods=['GET'])
def procesar2(regex,cadena):
    procesar_regex2(regex,cadena) 
    with open('appi2.json', 'r') as json_file:
        data = json.load(json_file)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=3600)
    