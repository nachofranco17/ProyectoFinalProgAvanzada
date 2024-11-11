package Procesos;

import java.util.Random;
import java.util.concurrent.Callable;

public class EnviarPedido implements Callable<Boolean> {
    private final Paquete paquete;
    private final int Tmin;
    private final int Tmax;

    public EnviarPedido(Paquete paquete, int Tmin, int Tmax) {
        this.paquete = paquete;
        this.Tmin = Tmin;
        this.Tmax = Tmax;
    }

    @Override
    public Boolean call() throws Exception {
        if (!paquete.isPagoValidado()) {
            System.out.println("El pago no ha sido validado. No se puede enviar el pedido.");
            return false;
        }

        Thread.sleep(new Random().nextInt(Tmin, Tmax));

        String socioLogistico = asignarSocioLogistico();
        paquete.setSocioLogistico(socioLogistico);
        return true;
    }

    private String asignarSocioLogistico(){
        String[] sociosLogisticos = {"DHL", "Fedex", "UPS", "Correos"};
        int index = (int) (Math.random() * sociosLogisticos.length);
        return sociosLogisticos[index];
    }
}
