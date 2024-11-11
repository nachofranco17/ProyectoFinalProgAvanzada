package TestsUnitarios;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import Procesos.Paquete;
import Procesos.EnviarPedido;

public class EnviarPedidoTest {

    @Test
    public void testEnviarPedidoConPagoValidado() throws Exception {
        Paquete paquete = new Paquete(true, new String[]{"Articulo1"});
        paquete.setPagoValidado(true);
        EnviarPedido enviarPedido = new EnviarPedido(paquete, 10, 20);

        boolean resultado = enviarPedido.call();
        assertTrue(resultado);
        assertNotNull(paquete.getSocioLogistico());
    }

    @Test
    public void testEnviarPedidoSinPagoValidado() throws Exception {
        Paquete paquete = new Paquete(true, new String[]{"Articulo1"});
        EnviarPedido enviarPedido = new EnviarPedido(paquete, 10, 20);

        boolean resultado = enviarPedido.call();
        assertFalse(resultado);
    }
}
