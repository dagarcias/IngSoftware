
from flask import Flask, render_template, request, jsonify
import json
import socket

app = Flask(__name__)

# Cargar datos de los Pokenea desde el archivo JSON
with open('pokenea.json', 'r') as json_file:
    pokenea = json.load(json_file)

@app.route('/')
def index():
    return render_template('index.html', pokenea=pokenea)

@app.route('/getRandomPoke', methods=['GET'])
def get_random_poke():
    import random
    random_poke = random.choice(pokenea)
    random_poke['hostId'] = socket.gethostname()
    return jsonify(random_poke)

if __name__ == '__main__':
    app.run(debug=True)
