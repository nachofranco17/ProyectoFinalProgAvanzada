package TestsUnitarios;
import org.junit.jupiter.api.Test;
import java.util.concurrent.PriorityBlockingQueue;
import Procesos.Paquete;
import Procesos.ProductorDePaquetes;
import static org.junit.jupiter.api.Assertions.*;

public class ProductorDePaquetesTest {

    @Test
    public void testEnviarOlaDePaquetes() {
        PriorityBlockingQueue<Paquete> colaDePedidos = new PriorityBlockingQueue<>();
        ProductorDePaquetes productor = new ProductorDePaquetes(null, colaDePedidos);

        productor.enviarOlaDePaquetes(5);
        assertEquals(5, colaDePedidos.size());
    }
}
