import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
    private static final String FILE_NAME = "users.txt";

    public static void main(String[] args) {
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
        try (BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
             BufferedWriter writer = new BufferedWriter(new FileWriter(FILE_NAME, true))) { // Modalità append
             
            String username = in.readLine(); // Legge l'username
            String password = in.readLine(); // Legge la password

            if (username != null && password != null) {
                System.out.println("Ricevuto: " + username + " - " + password);
                writer.write(username + ":" + password);
                writer.newLine();
                writer.flush();
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
}