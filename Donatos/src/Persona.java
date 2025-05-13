
import java.util.ArrayList;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author simof
 */
public class Persona {
    String username;
    ArrayList<Frasi> frasiPubblicate;

    public Persona(String username) {
        this.username = username;
        this.frasiPubblicate = new ArrayList<>();
    }

    public String getUsername() {
        return username;
    }

    public void rimuoviFrase(Frasi frase){
        for(Frasi f : frasiPubblicate){
            if(f.getOraPubblicazione()==frase.oraPubblicazione && f.getTesto() == frase.testo)
                frasiPubblicate.remove(f);
        }
    }
    
}
