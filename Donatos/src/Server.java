import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;

public class Server {
    private static final String UTENTI_FILE = "users.dat"; // File per salvare gli utenti
    private static ArrayList<Utente> utenti = new ArrayList<>(); // Lista degli utenti

    public static void main(String[] args) {
        // Carica l'elenco degli utenti dal file
        caricaUtenti();

        try (ServerSocket serverSocket = new ServerSocket(12345)) { // Porta 12345
            System.out.println("Server avviato e in attesa di connessioni...");
            while (true) {
                Socket clientSocket = serverSocket.accept(); // Accetta connessioni
                System.out.println("Client connesso: " + clientSocket.getInetAddress());

                // Gestisce la connessione in un thread separato
                new Thread(() -> handleClient(clientSocket)).start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void handleClient(Socket clientSocket) {
        try (BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()))) {
            String username = in.readLine(); // Legge l'username
            String password = in.readLine(); // Legge la password

            if (username != null && password != null) {
                synchronized (utenti) { // Sincronizzazione per accesso sicuro alla lista
                    if (!esisteUsername(username)) { // Verifica unicità username
                        Utente nuovoUtente = new Utente(username, password);
                        utenti.add(nuovoUtente); // Aggiunge il nuovo utente
                        salvaUtenti(); // Salva la lista aggiornata su file
                        System.out.println("Nuovo utente aggiunto: " + nuovoUtente);
                    } else {
                        System.out.println("Utente con username \"" + username + "\" già esistente.");
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                clientSocket.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    private static boolean esisteUsername(String username) {
        for (Utente utente : utenti) {
            if (utente.getUsername().equals(username)) {
                return true;
            }
        }
        return false;
    }

    private static void salvaUtenti() {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(UTENTI_FILE))) {
            oos.writeObject(utenti); // Scrive l'intera lista su file
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void caricaUtenti() {
        File file = new File(UTENTI_FILE);
        if (file.exists()) { // Se il file esiste, carica gli utenti
            try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(file))) {
                utenti = (ArrayList<Utente>) ois.readObject();
                System.out.println("Utenti caricati: " + utenti);
            } catch (IOException | ClassNotFoundException e) {
                e.printStackTrace();
            }
        }
    }
}