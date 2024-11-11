
import Procesos.ConsumidorDePaquetes;
import Procesos.Paquete;
import Procesos.ProductorDePaquetes;
import java.util.Comparator;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.PriorityBlockingQueue;
import jdk.jfr.Recording;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class PlantaDeProduccion {

    private static final int NUM_THREADS_CONS = 1000;
    private static final int NUM_THREADS_PROD = 200;
    private static final int MAX_OLAS_PEDIDOS = 5;
    private static final int DURACION_MIN_TAREA = 10;
    private static final int DURACION_MAX_TAREA = 20;

    private static final ExecutorService productorExecutor = Executors.newFixedThreadPool(NUM_THREADS_PROD);
    private static final ExecutorService consumidorExecutor = Executors.newFixedThreadPool(NUM_THREADS_CONS);
    private static final String separacion = "-------------------------------------------------------------------";

    private static final Comparator<Paquete> comparadorDePaquetes = (p1, p2) -> -Boolean.compare(p1.isUrgente(), p2.isUrgente());

    private static final PriorityBlockingQueue<Paquete> colaDePedidos = new PriorityBlockingQueue<>(10, comparadorDePaquetes);

    public static void main(String[] args) {

        try (Recording recording = new Recording()) {
            recording.start();

            long TiempoInicio = System.currentTimeMillis();

            ProductorDePaquetes productor = new ProductorDePaquetes(productorExecutor, colaDePedidos);
            ConsumidorDePaquetes consumidor = new ConsumidorDePaquetes(consumidorExecutor, colaDePedidos, NUM_THREADS_CONS, DURACION_MIN_TAREA, DURACION_MAX_TAREA);

            consumidor.iniciarConsumo();

            try {
                for (int contadorOlas = 0; contadorOlas < MAX_OLAS_PEDIDOS; contadorOlas++) {
                    int cantidadPaquetes = productor.generarNumeroDePaquetes();
                    System.out.println(separacion + "\nGenerando una ola de " + cantidadPaquetes + " paquetes...");
                    productor.enviarOlaDePaquetes(cantidadPaquetes);

                    int tiempoEspera = productor.generarTiempoDeEspera();
                    System.out.println("Esperando " + tiempoEspera / 1000 + " segundos antes de la siguiente ola...");
                    Thread.sleep(tiempoEspera);
                }

            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                System.out.println("Producción interrumpida.");

            } finally {
                productorExecutor.shutdown();
                consumidor.setProduccionFinalizada(true);
                System.out.println(separacion + "\nProducción de pedidos finalizada.");
                consumidorExecutor.shutdown();

                long TiempoFinal = System.currentTimeMillis();
                long TiempoTotal = (TiempoFinal - TiempoInicio) / 1000;

                System.out.println(separacion + "\nTiempo total de procesamiento: " + TiempoTotal + " segundos | " + consumidor.getPaquetesProcesados() + " paquetes procesados\n" + separacion);
            }

            Path registroPath = Paths.get("Registro6.jfr");
            Files.createFile(registroPath);
            recording.stop();
            recording.dump(registroPath);
            System.exit(0);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}