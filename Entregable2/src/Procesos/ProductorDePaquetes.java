package Procesos;

import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.PriorityBlockingQueue;

public class ProductorDePaquetes {
    private final ExecutorService productorExecutor;
    private final PriorityBlockingQueue<Paquete> colaDePedidos;
    private final Random RANDOM = new Random();
    private static final String separacion = "-------------------------------------------------------------------";

    public ProductorDePaquetes(ExecutorService productorExecutor, PriorityBlockingQueue<Paquete> colaDePedidos) {
        this.productorExecutor = productorExecutor;
        this.colaDePedidos = colaDePedidos;
    }

    public void enviarOlaDePaquetes(int cantidadP) {
        productorExecutor.submit(() -> {
            for (int i = 0; i < cantidadP; i++) {
                boolean urgente = i % 2 == 0;
                Paquete paquete = new Paquete(urgente, new String[]{"Artículo" + i});
                colaDePedidos.put(paquete);
            }
            System.out.println(separacion + "\nPedidos añadidos por " + Thread.currentThread().getName() + "\n" + separacion);
        });
    }

    public int generarNumeroDePaquetes() {
        return RANDOM.nextInt(3000, 5001);
    }

    public int generarTiempoDeEspera() {
        return RANDOM.nextInt(5000, 7001);
    }
}
