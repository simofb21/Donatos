import java.io.*;
import java.net.Socket;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        try (Socket socket = new Socket("localhost", 12345); // Connessione al server
             PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
             Scanner scanner = new Scanner(System.in)) {

            System.out.println("Inserisci username:");
            String username = scanner.nextLine();

            System.out.println("Inserisci password:");
            String password = scanner.nextLine();

            out.println(username); // Invia username
            out.println(password); // Invia password

            System.out.println("Dati inviati al server!");

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}