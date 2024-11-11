package Procesos;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.PriorityBlockingQueue;
import java.util.concurrent.atomic.AtomicInteger;

public class ConsumidorDePaquetes {
    private final ExecutorService consumidorExecutor;
    private final PriorityBlockingQueue<Paquete> colaDePedidos;
    private boolean produccionFinalizada = false;
    private final int numHilosConsumidores;
    private final AtomicInteger paquetesProcesados = new AtomicInteger(0);
    private final int durMinTarea;
    private final int durMaxTarea;


    public ConsumidorDePaquetes(ExecutorService consumidorExecutor, PriorityBlockingQueue<Paquete> colaDePedidos, int numHilosConsumidores, int durMinTarea, int durMaxTarea) {
        this.consumidorExecutor = consumidorExecutor;
        this.colaDePedidos = colaDePedidos;
        this.numHilosConsumidores = numHilosConsumidores;
        this.durMinTarea = durMinTarea;
        this.durMaxTarea = durMaxTarea;
    }


    public void iniciarConsumo() {
        for (int i = 0; i < numHilosConsumidores; i++) {
            consumidorExecutor.submit(() -> {
                try {
                    while (!produccionFinalizada || !colaDePedidos.isEmpty()) {
                        Paquete paquete;

                        synchronized (colaDePedidos) {
                            paquete = colaDePedidos.take();
                        }

                        paquetesProcesados.incrementAndGet();

                        System.out.println("Procesando paquete con ID: " + paquete.getEtiquetaID() + " en " + Thread.currentThread().getName());
                        ProcesarPago procesarPago = new ProcesarPago(paquete, durMinTarea, durMaxTarea);
                        boolean pagoAprobado = procesarPago.call();

                        if (pagoAprobado) {
                            EmpaquetarPedido empaquetarPedido = new EmpaquetarPedido(paquete, durMinTarea, durMaxTarea);
                            empaquetarPedido.call();

                            EnviarPedido enviarPedido = new EnviarPedido(paquete, durMinTarea, durMaxTarea);
                            enviarPedido.call();
                            System.out.println("Paquete con ID: " + paquete.getEtiquetaID() + " enviado con éxito a " + paquete.getSocioLogistico());
                        } else {
                            System.out.println("El paquete con ID: " + paquete.getEtiquetaID() + " fue descartado por errores de pago.");
                        }
                    }
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    System.out.println("Consumidor interrumpido.");
                } catch (Exception e) {
                    e.printStackTrace();
                }
            });
        }
    }

    public void setProduccionFinalizada(boolean produccionFinalizada) {
        this.produccionFinalizada = produccionFinalizada;
    }


    public int getPaquetesProcesados() {
        return paquetesProcesados.get();
    }
}
