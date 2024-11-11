package Procesos;

import java.util.concurrent.atomic.AtomicLong;

public class Paquete {
    private boolean pagoValidado;
    private final boolean urgente;
    private final String etiquetaID;
    private String SocioLogistico;
    private final String[] articulos;
    private static final AtomicLong contadorID = new AtomicLong(0);

    public Paquete(boolean urgente, String[] articulos) {
        this.urgente = urgente;
        this.articulos = articulos;
        this.etiquetaID = "ETIQ-" + contadorID.incrementAndGet();
    }

    public boolean isUrgente() {
        return urgente;
    }

    public String getEtiquetaID() {
        return etiquetaID;
    }

    public String getSocioLogistico() {
        return SocioLogistico;
    }

    public boolean isPagoValidado() {
        return pagoValidado;
    }

    public void setPagoValidado(boolean pagoValidado) {
        this.pagoValidado = pagoValidado;
    }

    public void setSocioLogistico(String socioLogistico) {
        this.SocioLogistico = socioLogistico;
    }
}
