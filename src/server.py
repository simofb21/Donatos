'''
Server in flask che gestisce la registrazione, il login e la gestione delle frasi.
'''
from flask import Flask, render_template, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import json
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register')
def serve_register():
    return render_template('registrati.html')

@app.route('/esplora')
def serve_explore():
    return render_template('esplora.html') 

@app.route('/homePage')
def serve_home_page():
    return render_template('homePage.html')
@app.route('/robots.txt') #piccolo robo a caso per far vedere che ho fatto le olicyber
def serve_robots():
    return "User-agent: *\nDisallow: /\n\n# c3BlcmlhbW8gaW4gdW4gYmVsIHZvdG8==", 200, {'Content-Type': 'text/plain'}#decodificare per ottenere informazioni segrete

@app.route('/frasi', methods=['GET'])
def frasi():
    if os.path.exists('frasi.json'):
        with open('frasi.json', 'r', encoding='utf-8') as f:
            frasi = json.load(f)
    else:
        frasi = []

    return jsonify(frasi), 200 #retorna le frasi in formato JSON

#gestione della registrazione
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
    password_hash = generate_password_hash(password) # uso la funzione di libreria per creare l'hash della password
    utenti.append({'username': username, 'password': password_hash})

    with open('utenti.json', 'w', encoding='utf-8') as f:
        json.dump(utenti, f, ensure_ascii=False, indent=2) #scrivo utente nel file
 
    return jsonify({'success': True, 'message': 'Registrazione avvenuta'}), 201

#  gestione del login
@app.route('/login', methods=['POST'])
def login():
    # mi prendo i dati arrivati  dalla post
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'success': False, 'message': 'Username o password mancanti'}), 400
    # apro il file utenti.json e leggo gli utenti
    if os.path.exists('utenti.json'):
        with open('utenti.json', 'r', encoding='utf-8') as f:
            utenti = json.load(f)
    else:
        utenti = []

    for utente in utenti: #controollo se l'utente esiste e se la password è corretta
        if utente['username'] == username and check_password_hash(utente['password'], password): #uso la funzione di libreria per controllare la password
            # Se l'utente esiste e la password è corretta, ritorno un messaggio di successo
            return jsonify({'success': True, 'message': 'Login riuscito'}), 200

    return jsonify({'success': False, 'message': 'Credenziali non valide'}), 401

@app.route('/aggiungi_frase', methods=['POST'])
def aggiungi_frase():
    data = request.get_json()
    username = data.get('username', 'anonimo')
    frase = data.get('frase', '')
    if not frase:
        return jsonify({'success': False, 'message': 'Frase mancante'}), 400

    dataora = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #ottenere la data e l'ora attuale in formato stringa
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

# Route per cancellare una frase: questa pagina viene fatta la richiesta POST per cancellare una frase
@app.route('/cancella_frase', methods=['POST'])
def cancella_frase(): 
    #mi prendo i dati dalla richiesta
    data = request.get_json()
    username = data.get('username')
    dataora = data.get('dataora')
    frase = data.get('frase')
    #controllo che i dati siano stati inviati
    if not (username and dataora and frase):
        return jsonify({'success': False, 'message': 'Dati mancanti'}), 400

    if os.path.exists('frasi.json'):
        with open('frasi.json', 'r', encoding='utf-8') as f:
            frasi = json.load(f)
    else:
        return jsonify({'success': False, 'message': 'Nessuna frase trovata'}), 404 

    # se non è la frase che voglio cancellare, la aggiungo alla nuova lista , che è quella che poi vado a salvarmi sul file
    nuove_frasi = []
    for f in frasi:
        if not (f['username'] == username and f['dataora'] == dataora and f['frase'] == frase):
            nuove_frasi.append(f)
    

    with open('frasi.json', 'w', encoding='utf-8') as f:
        json.dump(nuove_frasi, f, ensure_ascii=False, indent=2) #scrivo le frasi aggiornate nel file

    return jsonify({'success': True, 'message': 'Frase cancellata'}), 200
#route per vedere le frasi : a questa pagina viene fatta la richiesta GET per ottenere le frasi

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=True)