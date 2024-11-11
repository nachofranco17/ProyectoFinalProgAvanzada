package TestsUnitarios;

import static org.junit.jupiter.api.Assertions.*;

import Procesos.Paquete;
import org.junit.jupiter.api.Test;

public class PaqueteTest {

    @Test
    public void testPaqueteInicializacion() {
        Paquete paquete = new Paquete(true, new String[]{"Articulo1", "Articulo2"});

        assertTrue(paquete.isUrgente());
        assertNotNull(paquete.getEtiquetaID());
        assertFalse(paquete.isPagoValidado());
    }

    @Test
    public void testSetPagoValidado() {
        Paquete paquete = new Paquete(true, new String[]{"Articulo1"});
        paquete.setPagoValidado(true);

        assertTrue(paquete.isPagoValidado());
    }

    @Test
    public void testSetSocioLogistico() {
        Paquete paquete = new Paquete(false, new String[]{"Articulo1"});
        paquete.setSocioLogistico("DHL");

        assertEquals("DHL", paquete.getSocioLogistico());
    }
}
