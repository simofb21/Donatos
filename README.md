# Donatos  
**Documentazione tecnica**

## 1. Introduzione  
Il progetto **Donatos** è un social network che nasce con l'obiettivo di condividere dei momenti con delle frasi.

## 2. Team di sviluppo  
Il progetto è stato sviluppato da un team di tre studenti del corso di **4IC Informatica**:

| Nome                     | Competenze e attività principali   |
|--------------------------|------------------------------------|
| D'Elia, Fusar Bassini    | Backend                            |
| Donato, Cornetti         | Frontend, css                      |
| Donato, Cornetti         | documentazione                     |

> 💡 Se usato Git: [Link al repository GitHub](https://github.com/utente/progetto)

## 3. Requisiti

### 3.1 Requisiti Funzionali 
- L’utente può registrarsi e accedere al sistema.
- Gli utenti possono scrivere delle frasi
- Gli utenti possono vedere frasi altrui
- Gli utenti possono fare il logout 

### 3.2 Requisiti Non Funzionali
- Il sistema deve rispondere entro 2 secondi.
- Compatibile con i browser moderni.

## 4. Analisi del Sistema  
### Diagramma dei casi d’uso     
![Casi d'uso](path/to/casoduso.png)

### Descrizione dei moduli principali
- **Modulo autenticazione**  
- **Modulo gestione dati**

## 5. Architettura del Software

### Tecnologie utilizzate
- **Frontend**:   html,css,js
- **Backend**: python (flask)

### Pattern architetturali
- MVC (Model-View-Controller)

## 6. Implementazione

### Struttura delle cartelle
```
/src
  /template
  /static
    /css
    /img
```

### Funzionalità chiave
```js
loginUser(email, password)
createReport(data)
```

## 7. Installazione e Configurazione

1. Clonare il repository:  
   ```bash
   git clone https://github.com/utente/progetto.git
   ```

2. Installare le dipendenze:  
   ```bash
   npm install
   ```

3. Creare il file `.env` con le variabili richieste.

4. Avviare il server:  
   ```bash
   npm start
   ```

## 8. Manuale Utente

### Registrazione  
Cliccare su "Sign up", compilare i campi...

### Inserimento dati  
Accedere alla sezione "Nuovo record", compilare il modulo...

![Screenshot interfaccia](path/to/interfaccia.png)

## 9. Test e Validazione

### Test eseguiti
- Test unitari con Jest
- Test di integrazione con Postman

### Copertura del codice
- 85%

## 10. Manutenzione e Sviluppo Futuro

- **Bug noti**: problema di rendering su Safari  
- **Funzionalità previste**: esportazione in PDF, notifiche push

## 11. Conclusioni  
Il progetto ha raggiunto gli obiettivi principali. Le sfide maggiori sono state [...]. È stato utile per migliorare le competenze in [...].

## 12. Riferimenti e Bibliografia

- [Documentazione ufficiale di React](https://reactjs.org)
- *Clean Code* di Robert C. Martin

## 13. Appendici

- Codice sorgente: vedi cartella `/src`
- Glossario dei termini tecnici
- Screenshot dell’interfaccia in ordine cronologico
