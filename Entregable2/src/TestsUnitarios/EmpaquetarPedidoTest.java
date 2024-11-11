package TestsUnitarios;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import Procesos.Paquete;
import Procesos.EmpaquetarPedido;

public class EmpaquetarPedidoTest {

    @Test
    public void testEmpaquetarPedidoConPagoValidado() throws Exception {
        Paquete paquete = new Paquete(true, new String[]{"Articulo1"});
        paquete.setPagoValidado(true);
        EmpaquetarPedido empaquetarPedido = new EmpaquetarPedido(paquete, 10, 20);

        boolean resultado = empaquetarPedido.call();
        assertTrue(resultado);
    }

    @Test
    public void testEmpaquetarPedidoSinPagoValidado() throws Exception {
        Paquete paquete = new Paquete(true, new String[]{"Articulo1"});
        EmpaquetarPedido empaquetarPedido = new EmpaquetarPedido(paquete, 10, 20);

        boolean resultado = empaquetarPedido.call();
        assertFalse(resultado);
    }
}
