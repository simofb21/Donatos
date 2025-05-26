#eseguendo questo script , # si registrerà un nuovo utente, effettuerà il login e invierà una frase al server Flask.
#dopo aver fatto la post di registrazione commentare quella parte perchè non serve più
import requests

BASE_URL = "http://192.168.1.5:5000" #mettere ip del server

# le credenziali dell'utente , a meno che l' username sia usato , mettere qualsiasi cosa, poi se si vuole  si può cambiare utente e password
username = "username"
password = "password123"

# 1. post per registrazione
response = requests.post(f"{BASE_URL}/registrati", json={
    "username": username,
    "password": password
})
print("Registrazione:", response.json())    

# 2. post per login
response = requests.post(f"{BASE_URL}/login", json={
    "username": username,
    "password": password
})
print("Login:", response.json())

# post per inviare frase
if response.json().get("success"):
    # 3. Invio frase
    frase = "Frase inviata da script realizzato in python"
    response = requests.post(f"{BASE_URL}/aggiungi_frase", json={
        "username": username,
        "frase": frase
    })
    print("Aggiunta frase:", response.json())
else:
    print("Login fallito. Interrotto invio frase.")

