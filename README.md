# Donatos  
**Documentazione tecnica**
## Indice dei contentui
- [1. Introduzione](#1-introduzione)
- [2. Team di sviluppo](#2-team-di-sviluppo)
- [3. Requisiti](#3-requisiti)
- [4. Analisi del Sistema](#4-analisi-del-sistema)
- [5. Architettura del Software](#5-architettura-del-software)
- [6. Implementazione](#6-implementazione)
- [7. Installazione e configurazione](#7-installazione-e-configurazione)
- [8. Manuale Utente](#8-manuale-utente)
- [9. Sviluppi Futuri](#9-sviluppi-futuri)
- [10. Conclusioni](#10-conclusioni)
- [11. Riferimenti e bibliografia](#11-Riferimenti-e-Bibliografia)
- [12. Appendici](#12-appendici)  


## 1. Introduzione  
Il progetto **Donatos** è un sito che nasce con l'obiettivo di condividere dei momenti, ricordi, e qualsiasi altra informazione si voglia, attraverso delle frasi , che è possibile salvare sul nostro sito. Il nome Donatos è ispirato dal cognome di uno dei membri del nostro gruppo, Riccardo Donato, e suona molto bene per un social network di successo.
## 2. Team di sviluppo  
Il progetto è stato sviluppato da un team di quattro studenti del corso di **4IC Informatica**:

| Nome                     | Competenze e attività principali   |
|--------------------------|------------------------------------|
| Cornetti Andrea   | Sviluppo logo, pagina css per l' homePage, presentazione,documento di progettto                            |
| Donato Riccardo       | Pagina css per il login, presentazione,documento di progetto, decisione sulla grafica per tutto il sito                  |
| Fusar Bassini Simone        | Comunicazione con il server lato front-end e cooperazione nello sviluppo del server|
|D'Elia Raffaele|Sviluppo del server lato front-end e cooperazione nello sviluppo del front-end|

> 💡 Se usato Git: [Link al repository GitHub](https://github.com/simofb21/Donatos.git)

## 3. Requisiti

### 3.1 Requisiti Funzionali 
- server accessibile da altri utenti(solo della nostra stessa rete)
- Gli utenti possono registrarsi e accedere al sistema
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
![image](https://github.com/user-attachments/assets/69c3e0e4-2999-430e-971d-e8c754dc5a47)


## Casi d'Uso 

### Attori Coinvolti
- **User**: Utente generico che può registrarsi, accedere e gestire frasi.
- **Admin**: Amministratore che può intervenire direttamente sui file.
---

## UC1 - Registrarsi
- **Attore**: User  
- **Descrizione**: L’utente può registrarsi al sistema inserendo i propri dati.  
- **Precondizione**: Nessuna  
- **Postcondizione**: I dati vengono salvati per consentire futuri login.
---

### UC2 - Effettuare login
- **Attore**: User  
- **Descrizione**: L’utente inserisce credenziali per accedere al sistema.  
- **Precondizione**: L’utente deve essere già registrato.  
- **Postcondizione**: Se le credenziali sono corrette, accede al sistema.
---
### UC3 - Vedere tutte le frasi
- **Attore**: User  
- **Descrizione**: Il sistema mostra tutte le frasi salvate.  
- **Precondizione**: L’utente deve essere loggato.  
- **Postcondizione**: Le frasi vengono mostrate all’utente.
---
### UC4 - Aggiungere/Cancellare frase
- **Attore**: User  
- **Descrizione**: L’utente può aggiungere nuove frasi o rimuovere quelle esistenti.  
- **Precondizione**: L’utente deve essere loggato.  
- **Postcondizione**: Le frasi vengono aggiornate nel sistema.
---
### UC5 - Cancellare frasi/utenti direttamente dal file
- **Attore**: Admin  
- **Descrizione**: L’amministratore accede direttamente al file e gestisce frasi o utenti.  
- **Precondizione**: Bisogna essere sulla macchina che sta eseguendo il file server.py 
- **Postcondizione**: Il file viene aggiornato
---
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
### Come eseguire il server Flask su Raspberry Pi o su un computer normale

È possibile eseguire il server su un Raspberry Pi oppure su un computer normale (Windows, macOS, Linux).

---
### ✅ Di seguito i comandi per farlo
Apri il terminale ed esegui i seguenti comandi:

```bash
git clone https://github.com/simofb21/Donatos.git    # Clona la repository
cd Donatos/src                                       # Vai nella cartella del progetto
python3 server.py                                    # Avvia il server
```
Se compare un errore vuol dire che non hai flask installato, quindi :
```bash
pip install flask #adesso hai scaricato la libreria
python3 server.py #adesso puoi eseguire il codice
```
Ora i dispositivi sulla tua rete possono accedere al sito visitando IP_TUO_IP_RASPBERRY:5000

**NB: noi diamo per scontato che i dispositivi abbiano già installato python, su linux, e quindi sul raspberry è già installato, ma da altri OS , andrebbe scaricato, all'inizio di tutto**

## 8. Manuale Utente
Innanzitutto bisogna connettersi all' indirizzo IP del server, questo rimanderà alla pagina di Login
Quindi andare su un browser e digitare IP:50000  # questo perchè flask usa la porta 50000
### Registrazione  
Se non sei registrato clicca su "Registrati", compilare i campi username e password

![image](https://github.com/user-attachments/assets/7ab5f83c-3a3f-4c30-84fe-a3123c9e2887)

### Login  
Se ti sei registrato inserisci le tue credenziali

![image](https://github.com/user-attachments/assets/e1792ff7-46a8-4fd9-b727-022274c3cf0b)

### Home Page
Una volta loggato ci accedi a /homePage
Qua puoi vedere tutte le tue frasi 
![image](https://github.com/user-attachments/assets/0c1d9e2d-71d5-4e27-b0db-7a61999c2151)
Ne puoi aggiungere una oppure, cliccando sulla X rossa puoi cancellarla
### Esplora page
Una volta loggato ci accedi a /esplora
Su questa pagina puoi vedere le pagine di tutti gli utenti, cercare le frasi specifiche per utente
![image](https://github.com/user-attachments/assets/39d0342a-bdaa-4852-a082-0c7db0ae8ad3)

## 9.Sviluppi futuri
- ☐ Rendere il sito accessibile da internet (non solo da rete locale)
- ☐ Esportazione frasi
- ☐ Cancellazione utenti via interfaccia
- ☐ Funzione "cambia password"
- ☐ Recupero password dimenticata
- ☐ Migliorare la pagina "Esplora" con suggerimenti personalizzati

## 10. Conclusioni 
Il progetto Donatos ha raggiunto gli obiettivi principali: creare una piattaforma semplice e intuitiva per scrivere, salvare e condividere frasi personali. Durante lo sviluppo, ci siamo confrontati con diverse sfide, come la gestione dei dati, l'autenticazione degli utenti e l'organizzazione del codice tra frontend e backend.
Questo ci ha permesso di approfondire l'utilizzo di Flask per il server, migliorare le nostre competenze con JavaScript , e curare l’aspetto grafico del sito con HTML e CSS. Abbiamo imparato a collaborare in gruppo, dividendo i compiti e coordinando le decisioni di design e sviluppo.
Siamo consapevoli che ci sono ancora molte funzionalità da implementare e miglioramenti possibili, ma siamo soddisfatti di quanto realizzato. Donatos rappresenta per noi non solo un sito funzionante, ma anche un’esperienza concreta di progettazione e sviluppo software, che ci ha avvicinati ancora di più al mondo della programmazione web.
## 11. Riferimenti e Bibliografia
 . https://gitlab.com/4i3785803/Telecomunicazioni/-/blob/master/laboratorio/LAB1_FLASK.md?ref_type=heads TUTORIAL DEL PROF DI TELECOMUNICAZIONI PER REALIZZARE SERVER CON FLASK, DOPO DI CHE ABBIAMO APPROFONDITO NOI INDIVIDUALMENTE
 . mentre per fare le fetch da js abbiamo usato ajax 
 . Il codice utilizza la libreria werkzeug.security per la crittografia (hashing) delle password , che è inclusa nel framework di flask


## 12. Appendici
- Per vedere il sorgente clicca sulla cartella src. Se ci sono dubbi invitiamo a contattarci.
