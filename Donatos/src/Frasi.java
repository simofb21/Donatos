/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

import java.time.LocalDateTime;
/**
 *
 * @author simof
 */
public class Frasi {
    String testo;
    LocalDateTime oraPubblicazione;

    public String getTesto() {
        return testo;
    }

    public void setTesto(String testo) {
        this.testo = testo;
    }

    public LocalDateTime getOraPubblicazione() {
        return oraPubblicazione;
    }

    public void setOraPubblicazione(LocalDateTime oraPubblicazione) {
        this.oraPubblicazione = oraPubblicazione;
    }

    public Frasi(String testo, LocalDateTime oraPubblicazione) {
        this.testo = testo;
        this.oraPubblicazione = oraPubblicazione;
    }
    
}
