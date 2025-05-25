# Donatos  
**Documentazione tecnica**

## 1. Introduzione  
Il progetto **Donatos** è un sito che nasce con l'obiettivo di condividere dei momenti, ricordi, e qualsiasi altra informazione si voglia, attraverso delle frasi , che è possibile salvare sul nostro sito.

## 2. Team di sviluppo  
Il progetto è stato sviluppato da un team di quattro studenti del corso di **4IC Informatica**:

| Nome                     | Competenze e attività principali   |
|--------------------------|------------------------------------|
|Cornetti Andrea| Sviluppo logo, pagina css per l' homePage, presentazione,documento di progettto|
|Donato Riccardo|Pagina css per il login, presentazione,documento di progetto, decisione sulla grafica per tutto il sito|
|Fusar Bassini Simone| Comunicazione con il server lato front-end e cooperazione nello sviluppo del server|
|D'Elia Raffaele| Sviluppo del server lato front-end e cooperazione nello sviluppo del front-end|

* Il progetto si trova su Github al seguente link https://github.com/simofb21/Donatos 
## 3. Requisiti

### 3.1 Requisiti Funzionali 
- server accessibile da altri utenti(solo della nostra stessa rete)
- Gli utenti possono registrarasi e accedere al sistema
- Gli utenti possono fare il logout
- Gli utenti possono scrivere delle frasi
- Gli utenti possono cancellare delle frasi
- Gli utenti possono vedere frasi altrui

### 3.2 Requisiti Non Funzionali
- L'interfaccia utente è intuitiva e facile da usare.
- Stile adattato per funzionare sia su computer ma anche su mobile
- (Teoricamente sarebbe funzionale, ma per le nostre competenze iniziali no) **crittografia** per non salvare le password in chiaro sul file
- possibilità di cancellare utenti/frasi da amministratore(lo può fare solo chi accede al server, editando i 2 file)

## 4. Analisi del Sistema

### Descrizione dei moduli principali
- **Modulo autenticazione**
  
## 5. Architettura del Software

### Tecnologie utilizzate
- **Frontend**:   html,css, **js**  con Ajax per effettuare le richieste al server
- **Backend**: Python(flask)
- **Salvataggio delle informazioni** : File Json

## 6. Implementazione

### Struttura 
```
/src
  /templates         # Cartella che contiene le pagine HTML
  /static            # Contiene i file statici (CSS, immagini)
    /css             # Fogli di stile CSS
    /img             # Immagini del sito
  server.py          # File principale del server (es. Flask)
```
Per vedere meglio la struttura basta entrare nella cartella src all' interno del repository
### Funzionalità chiave
Lato server :  python
```python
@app.route('/') #consetnte di accedere alla index, procedimento analogo per tutte le altre pagine
def home():
    return render_template('index.html')
@app.route('/frasi', methods=['GET']) #rotta che restituisce le frasi
def frasi():
    return jsonify(frasi), 200 #retorna le frasi in formato JSON
@app.route('/registrati', methods=['POST'])#rotta che gestisce registrazione  , aggiunge utente al file utenti
def registrati():
    return jsonify({'success': True, 'message': 'Registrazione avvenuta'}), 201
@app.route('/login', methods=['POST'])
def login():# rotta per il login che restiituisce come è andato
@app.route('/aggiungi_frase', methods=['POST'])
def aggiungi_frase(): #riceve la frase via post e la aggiunge al file con le frasi
@app.route('/cancella_frase', methods=['POST'])#rotta per cancellare le frasi , con richiesta post, se va bene , le rimuove dal file 
def cancella_frase(): 
```
JS per dialogare con server : 
```javascript

async function caricaFrasi(){ // fa richiesta per ottenere le frasi , e le scrive sulla pagina 
Questa è diciamo la funzione principale , ovvero quella che prende le frasi, e le scrive nell' html che avevamo preparato.
Vi sono però ovviamente anche altre funzioni importanti , per esempio per completare il login quando clicca , perr cambiare le pagine ecc...

```


## 7. Installazione e configurazione
È possibile eseguire il server su un Raspberry Pi oppure su un computer normale (Windows, macOS, Linux).
### Come eseguire il server Flask su Raspberry Pi o su un computer normale

È possibile eseguire il server su un Raspberry Pi oppure su un computer normale (Windows, macOS, Linux).

---

### ✅ Esecuzione su Raspberry Pi

Se utilizzi un Raspberry Pi con Python già installato, l’esecuzione è molto semplice.

Apri il terminale ed esegui i seguenti comandi:

```bash
git clone https://github.com/simofb21/Donatos.git    # Clona la repository
cd Donatos/src                                       # Vai nella cartella del progetto
python3 server.py                                    # Avvia il server
```
Se compare un errore vuol dire che non hai flask installato, quindi :
```bash
pip install flask #adesso hai scaricato la librerai
python3 server.py #afesso puoi eseguire al codice
```
Ora i dispositivi sulla tua rete possono accedere al sito visitando IP_TUO_IP_RASPBERRY:5000

Parte per eseguire su windows/linux  , ambiente virtuale (fa bomber)

**NB: noi diamo per scontato che i dispositivi abbiano già installato python, su linux, e quindi sul raspberry è già installato, ma da altri OS , andrebbe scaricato**

## 8. Manuale Utente
Innanzitutto bisogna connettersi all' indirizzo IP del server, questo rimanderà alla pagina di Login
Quindi andare su un browser e digitare IP:50000  # questo perchè flask usa la porta 50000
### Registrazione  
Se non sei registrato clicca su "Registrati", compilare i campi username e password

![image](https://github.com/user-attachments/assets/7ab5f83c-3a3f-4c30-84fe-a3123c9e2887)

### Login  
Se ti sei registrato inserisci le tue credenziali

![image](https://github.com/user-attachments/assets/e1792ff7-46a8-4fd9-b727-022274c3cf0b)

## 8. Manutenzione e Sviluppo Futuro
- possibilità di rendere il servizio accessibile a tutti e non solo da pc sulla nostra stessa rete
- possibilità di esportare tutte le frasi
- possibilità di cancellare un utente esistente
- funzione per cambiare la password
- funzione per password dimenticata
- migliorare la pagina esplora : non mostrare solo randomicamente tutte le frasi di tutti gli utenti, ma mostrare per esempio le frasi più opportune per determinati utenti, quelle più simili, quelle di  persone che potresti conoscere ecc

## 9. Conclusioni 
Il progetto ha raggiunto gli obiettivi principali. Le sfide maggiori sono state [...]. È stato utile per migliorare le competenze in [...].

## 10. Riferimenti e Bibliografia
 . https://gitlab.com/4i3785803/Telecomunicazioni/-/blob/master/laboratorio/LAB1_FLASK.md?ref_type=heads TUTORIAL DEL PROF DI TELECOMUNICAZIONI PER REALIZZARE SERVER CON FLASK, DOPO DI CHE ABBIAMO APPROFONDITO NOI INDIVIDUALMENTE
 . mentre per fare le fetch da 

## 11. Appendici

- Codice sorgente: vedi cartella `/src`
- Glossario dei termini tecnici
- Screenshot dell’interfaccia in ordine cronologico
