from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# gestione della registrazione
@app.route('/registrati', methods=['GET'])
def registrati_page():
    return render_template('registrati.html')

@app.route('/registrati', methods=['POST'])
def registrati():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'success': False, 'message': 'Username o password mancanti'}), 400 #se ha ricevuto dati sbagliati manda errore

    #legge dal file utenti.json
    if os.path.exists('utenti.json'):
        with open('utenti.json', 'r', encoding='utf-8') as f:
            utenti = json.load(f)
    else:
        utenti = [] #se il file non esiste crea una lista vuota

    # controlla se l' utenbte c'è già e resitutisce errore
    for utente in utenti:
        if utente['username'] == username:
            return jsonify({'success': False, 'message': 'Username già esistente'}), 409
    #altrimenti aggiunte utente alla lista
    utenti.append({'username': username, 'password': password})

    with open('utenti.json', 'w', encoding='utf-8') as f:
        json.dump(utenti, f, ensure_ascii=False, indent=2) #scrivo utente nel file
 
    return jsonify({'success': True, 'message': 'Registrazione avvenuta'}), 201

#  gestione del login
@app.route('/login', methods=['GET'])
def login_page():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'success': False, 'message': 'Username o password mancanti'}), 400

    if os.path.exists('utenti.json'):
        with open('utenti.json', 'r', encoding='utf-8') as f:
            utenti = json.load(f)
    else:
        utenti = []

    for utente in utenti:
        if utente['username'] == username and utente['password'] == password:
            return jsonify({'success': True, 'message': 'Login riuscito'}), 200

    return jsonify({'success': False, 'message': 'Credenziali non valide'}), 401

@app.route('/aggiungi_frase', methods=['POST'])
def aggiungi_frase():
    data = request.get_json()
    username = data.get('username', 'anonimo')
    frase = data.get('frase', '')
    if not frase:
        return jsonify({'success': False, 'message': 'Frase mancante'}), 400

    dataora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    nuova_frase = {
        "username": username,
        "dataora": dataora,
        "frase": frase
    }

    if os.path.exists('frasi.json'):
        with open('frasi.json', 'r', encoding='utf-8') as f:
            frasi = json.load(f)
    else:
        frasi = []

    frasi.append(nuova_frase)

    with open('frasi.json', 'w', encoding='utf-8') as f:
        json.dump(frasi, f, ensure_ascii=False, indent=2)

    return jsonify({'success': True, 'frase': nuova_frase}), 201

@app.route('/cancella_frase', methods=['POST'])
def cancella_frase():
    data = request.get_json()
    username = data.get('username')
    dataora = data.get('dataora')
    frase = data.get('frase')

    if not (username and dataora and frase):
        return jsonify({'success': False, 'message': 'Dati mancanti'}), 400

    if os.path.exists('frasi.json'):
        with open('frasi.json', 'r', encoding='utf-8') as f:
            frasi = json.load(f)
    else:
        return jsonify({'success': False, 'message': 'Nessuna frase trovata'}), 404

    # Rimuovi la frase che corrisponde a tutti e tre i campi
    nuove_frasi = [
        f for f in frasi
        if not (f['username'] == username and f['dataora'] == dataora and f['frase'] == frase)
    ]

    with open('frasi.json', 'w', encoding='utf-8') as f:
        json.dump(nuove_frasi, f, ensure_ascii=False, indent=2)

    return jsonify({'success': True, 'message': 'Frase cancellata'}), 200

@app.route('/frasi', methods=['GET'])
def frasi():
    if os.path.exists('frasi.json'):
        with open('frasi.json', 'r', encoding='utf-8') as f:
            frasi = json.load(f)
    else:
        frasi = []
    return jsonify(frasi), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')