package TestsUnitarios;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;
import Procesos.Paquete;
import Procesos.ProcesarPago;

public class ProcesarPagoTest {

    @Test
    public void testProcesarPagoAprobado() throws Exception {
        Paquete paquete = new Paquete(true, new String[]{"Articulo1"});
        ProcesarPago procesarPago = new ProcesarPago(paquete, 10, 20);

        boolean resultado = procesarPago.call();

        if (resultado) {
            assertTrue(paquete.isPagoValidado());
        } else {
            assertFalse(paquete.isPagoValidado());
        }
    }
}
